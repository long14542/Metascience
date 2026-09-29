#!/usr/bin/env python3
"""
Extract DOCX and PDF documents into Markdown for AI/search use.

Expected repository structure:

    repo/
    ├── originals/          # source DOCX/PDF files
    ├── extracted/          # generated Markdown + extracted images
    └── scripts/
        └── extract_documents.py

Usage:
    python scripts/extract_documents.py

Optional:
    python scripts/extract_documents.py --clean
        Remove generated files under extracted/ before rebuilding.

Notes:
- DOCX:
    * paragraphs are preserved in order
    * Word tables become Markdown tables
    * embedded images are extracted to extracted/assets/<document>/
    * paragraph text, including ASCII diagrams, is preserved as text
- PDF:
    * text is extracted page-by-page
    * embedded images are extracted when possible
    * PDF tables remain text unless their layout can be inferred reliably;
      this script deliberately does not invent table structure
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from pathlib import Path

import fitz  # PyMuPDF
from docx import Document


IMAGE_EXTENSIONS = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/gif": ".gif",
    "image/bmp": ".bmp",
    "image/tiff": ".tiff",
    "image/x-emf": ".emf",
    "image/x-wmf": ".wmf",
}


def safe_name(name: str) -> str:
    """Make a filesystem-safe name while keeping it readable."""
    name = re.sub(r"[^\w\-. ]+", "_", name, flags=re.UNICODE)
    name = re.sub(r"\s+", "_", name.strip())
    return name or "document"


def unique_filename(folder: Path, filename: str) -> Path:
    """Avoid overwriting an existing extracted asset."""
    target = folder / filename
    if not target.exists():
        return target

    stem = target.stem
    suffix = target.suffix
    i = 2
    while True:
        candidate = folder / f"{stem}_{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def markdown_escape_cell(value: str) -> str:
    value = value.replace("\n", "<br>")
    value = value.replace("|", r"\|")
    return value.strip()


def table_to_markdown(table) -> str:
    """Convert a python-docx table to a simple Markdown table."""
    rows = []
    for row in table.rows:
        cells = [markdown_escape_cell(cell.text) for cell in row.cells]
        rows.append(cells)

    if not rows:
        return ""

    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]

    lines = [
        "| " + " | ".join(rows[0]) + " |",
        "| " + " | ".join("---" for _ in range(width)) + " |",
    ]

    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def extract_docx(path: Path, output_root: Path) -> Path:
    document = Document(path)

    stem = safe_name(path.stem)
    output_md = output_root / f"{stem}.md"
    asset_dir = output_root / "assets" / stem
    asset_dir.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []

    lines.append("---")
    lines.append(f"source: originals/{path.name}")
    lines.append("type: docx")
    lines.append("---")
    lines.append("")
    lines.append(f"# {path.stem}")
    lines.append("")

    # Extract paragraphs and tables in the order exposed by python-docx.
    # Tables are also handled separately below when they are not represented
    # in paragraph flow. This gives a useful, conservative representation.
    body = document.element.body

    table_map = {table._tbl: table for table in document.tables}

    for child in body.iterchildren():
        tag = child.tag.rsplit("}", 1)[-1]

        if tag == "p":
            # Find the matching paragraph object.
            text = ""
            for paragraph in document.paragraphs:
                if paragraph._p is child:
                    text = paragraph.text
                    break

            if text:
                lines.append(text)
                lines.append("")

        elif tag == "tbl":
            table = table_map.get(child)
            if table is not None:
                md = table_to_markdown(table)
                if md:
                    lines.append(md)
                    lines.append("")

    # Extract embedded images.
    image_counter = 0
    for rel in document.part.rels.values():
        target = getattr(rel, "target_part", None)
        if target is None:
            continue

        content_type = getattr(target, "content_type", "")
        if not content_type.startswith("image/"):
            continue

        blob = target.blob
        image_counter += 1

        digest = hashlib.sha1(blob).hexdigest()[:10]
        extension = IMAGE_EXTENSIONS.get(content_type, ".bin")
        filename = f"image_{image_counter:03d}_{digest}{extension}"
        asset_path = unique_filename(asset_dir, filename)
        asset_path.write_bytes(blob)

        relative = Path("assets") / stem / asset_path.name
        lines.append(f"![Embedded image]({relative.as_posix()})")
        lines.append("")

    output_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return output_md


def extract_pdf(path: Path, output_root: Path) -> Path:
    stem = safe_name(path.stem)
    output_md = output_root / f"{stem}.md"
    asset_dir = output_root / "assets" / stem
    asset_dir.mkdir(parents=True, exist_ok=True)

    pdf = fitz.open(path)

    lines: list[str] = []
    lines.append("---")
    lines.append(f"source: originals/{path.name}")
    lines.append("type: pdf")
    lines.append(f"pages: {len(pdf)}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {path.stem}")
    lines.append("")

    image_counter = 0

    for page_number, page in enumerate(pdf, start=1):
        lines.append(f"## Page {page_number}")
        lines.append("")

        # "text" is intentionally used rather than aggressive table
        # reconstruction. It preserves the document's textual content
        # without inventing rows/columns when PDF layout is ambiguous.
        text = page.get_text("text")

        if text.strip():
            lines.append(text.rstrip())
            lines.append("")
        else:
            lines.append("_No text layer detected on this page._")
            lines.append("")

        # Extract embedded images when present.
        for image in page.get_images(full=True):
            xref = image[0]
            try:
                extracted = pdf.extract_image(xref)
            except Exception:
                continue

            image_counter += 1
            image_bytes = extracted["image"]
            extension = "." + extracted["ext"]

            digest = hashlib.sha1(image_bytes).hexdigest()[:10]
            filename = f"page_{page_number:03d}_image_{image_counter:03d}_{digest}{extension}"
            asset_path = unique_filename(asset_dir, filename)
            asset_path.write_bytes(image_bytes)

            relative = Path("assets") / stem / asset_path.name
            lines.append(f"![Embedded image]({relative.as_posix()})")
            lines.append("")

    pdf.close()

    output_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return output_md


def clean_generated(output_root: Path) -> None:
    if output_root.exists():
        for child in output_root.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract DOCX/PDF to Markdown.")
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove existing generated content under extracted/ first.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    originals = repo_root / "originals"
    extracted = repo_root / "extracted"

    if not originals.exists():
        raise SystemExit(
            f"ERROR: originals folder not found:\n  {originals}\n"
            "Create originals/ and put your DOCX/PDF files there."
        )

    extracted.mkdir(parents=True, exist_ok=True)

    if args.clean:
        clean_generated(extracted)
        extracted.mkdir(parents=True, exist_ok=True)

    files = sorted(
        p for p in originals.rglob("*")
        if p.is_file() and p.suffix.lower() in {".docx", ".pdf"}
    )

    if not files:
        print(f"No DOCX/PDF files found in {originals}")
        return

    success = 0

    for path in files:
        try:
            if path.suffix.lower() == ".docx":
                output = extract_docx(path, extracted)
            else:
                output = extract_pdf(path, extracted)

            print(f"[OK] {path.relative_to(repo_root)} -> {output.relative_to(repo_root)}")
            success += 1

        except Exception as exc:
            print(f"[ERROR] {path.relative_to(repo_root)}: {exc}")

    print()
    print(f"Extracted {success}/{len(files)} document(s).")
    print(f"Output: {extracted}")


if __name__ == "__main__":
    main()
