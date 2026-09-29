# Document Knowledge Base

## Purpose

This repository is a document knowledge base containing source Word/PDF files and AI-readable extracted representations.

The primary purpose is to let Claude Code search, read, compare, summarize, cross-reference, and reason over the document collection while preserving the original files as the source of truth.

## Repository structure

```text
/
├── CLAUDE.md
├── originals/
│   ├── *.docx
│   └── *.pdf
├── extracted/
│   ├── *.md
│   └── assets/
└── scripts/
    └── extract_documents.py
```

### `originals/`

Contains the original Word and PDF documents.

Rules:
- Treat files in `originals/` as source documents.
- Do not modify, rename, overwrite, or delete source documents unless the user explicitly asks.
- When a factual claim needs verification, use the corresponding original document as the authoritative source.
- Preserve the relationship between each source file and its extracted Markdown file.

### `extracted/`

Contains AI-readable Markdown representations generated from files in `originals/`.

Use these files as the primary working/search representation because they are easier to search, compare, and process than DOCX/PDF binaries.

Important:
- Do not assume that an extracted Markdown file contains every visual or layout detail of the original.
- If a question depends on a table layout, image, diagram, formatting, or other information that may have been lost during extraction, inspect the corresponding original document and/or extracted asset.
- Do not invent missing content.

### `extracted/assets/`

Contains images extracted from Word/PDF documents.

Images may contain information that is not fully represented in Markdown. When relevant, inspect the associated image rather than relying only on the extracted text.

### `scripts/`

Contains document-processing scripts.

`extract_documents.py` converts DOCX/PDF files from `originals/` into Markdown files under `extracted/`.

When source documents change or new documents are added, the extraction script may need to be run again.

## Document-reading workflow

When answering a question about this knowledge base:

1. Search `extracted/` first for relevant content.
2. Identify the source document(s) corresponding to the relevant Markdown.
3. Use the original DOCX/PDF when verification requires information that may have been lost or distorted during extraction.
4. Inspect relevant extracted images when visual information may contain important evidence.
5. When multiple documents discuss the same subject, compare them explicitly rather than assuming they agree.
6. Distinguish information stated by a document from conclusions inferred from multiple documents.
7. If the documents do not contain enough evidence to answer confidently, say what is missing instead of filling the gap with an assumption.

## Source attribution

When reporting information from this repository, identify the source document whenever practical.

Prefer references such as:

- `originals/contract-a.docx`
- `originals/report-2025.pdf`

If a statement comes specifically from an extracted representation, identify the corresponding original source as well.

## Handling extracted text

The extraction process is intentionally conservative.

### Word documents

The extractor attempts to preserve:
- paragraph text
- Word tables as Markdown tables
- embedded images
- ASCII/text diagrams

ASCII diagrams and other whitespace-sensitive text should not be reformatted casually. Preserve their structure when modifying or quoting them.

### PDF documents

The extractor preserves page-oriented text and extracts embedded images where possible.

PDF tables may remain as text rather than becoming Markdown tables. Do not infer a table structure merely because the text visually resembles columns. If exact row/column relationships matter, inspect the original PDF.

## Editing policy

Do not modify `originals/` merely to improve readability for Claude.

If a cleaned, reorganized, summarized, or transformed version is needed, create it under an appropriate non-source location such as `extracted/`, `notes/`, or another directory requested by the user.

When editing generated files, remember that they may be regenerated from the originals.

## Re-extraction

The standard extraction command, run from the repository root, is:

```bash
python scripts/extract_documents.py
```

On Windows, this may also be:

```bash
py scripts/extract_documents.py
```

Do not run the command from inside `originals/`.

After adding or changing source documents, re-run the extractor before relying on the corresponding extracted Markdown.

## Git

The repository is version-controlled with Git.

Before making large or destructive changes:
- inspect the current repository state
- avoid modifying source documents unless explicitly requested
- keep generated changes distinguishable from source changes

Useful commands:

```bash
git status
git add .
git commit -m "Describe the change"
```

## General reasoning rules

- Prefer evidence from the documents over assumptions.
- Preserve document-specific terminology.
- When documents conflict, report the conflict and identify the respective sources.
- Do not silently merge contradictory statements into one claim.
- Keep dates, names, numbers, units, definitions, and document versions attached to their source context.
- For summaries, preserve important qualifications, exceptions, conditions, and scope.
- For comparisons, make the comparison criteria explicit.
- For requests involving the entire knowledge base, search across all relevant extracted documents rather than relying on a single file.

## Important limitation

The Markdown files in `extracted/` are representations of the originals, not replacements for them.

For high-precision questions, especially those involving:
- tables
- figures
- diagrams
- scanned pages
- formatting-dependent meaning
- footnotes
- headers/footers
- exact wording

verify against the original DOCX/PDF and relevant extracted assets.
