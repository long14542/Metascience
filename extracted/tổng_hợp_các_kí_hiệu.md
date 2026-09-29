---
source: originals/tổng hợp các kí hiệu.docx
type: docx
---

# tổng hợp các kí hiệu

1. Ký hiệu tập hợp & logic cơ bản

| Ký hiệu | Tên gọi | Ý nghĩa trong khung của bạn | Ví dụ |
| --- | --- | --- | --- |
| R | Reality | Tập vũ trụ khảo sát — toàn bộ thực tại có thể quan sát | x ∈ R |
| PERSPECTIVES | Tập các Góc nhìn | Tập hợp tất cả các góc nhìn khả dĩ | P ∈ PERSPECTIVES |
| Phen(P) | Hiện tượng của P | Tập con của R mà góc nhìn P "mở ra" | Phen(P) ⊆ R |
| ∀ | Lượng từ phổ quát | "Với mọi..." | ∀P ∈ PERSPECTIVES |
| ∃ | Lượng từ tồn tại | "Tồn tại ít nhất một..." | ∃x ∈ Phen(P) |
| ∈ | Thuộc về | Phần tử thuộc tập hợp | x ∈ Phen(P) |
| ⊆ | Tập con (có thể bằng) | Một tập nằm trong hoặc bằng tập kia | Phen(P) ⊆ R |
| ⊂ | Tập con thực sự | Nằm trong nhưng không bằng | A ⊂ R |
| ⇒ | Kéo theo (implication) | Nếu trái đúng thì phải đúng | P ≠ Q ⇒ Phen(P) ≠ Phen(Q) |
| ↔ | Tương đương logic | Hai mệnh đề cùng đúng/sai | A ↔ B |
| ∧, ∨ | Và / Hoặc | Liên kết mệnh đề | x ∈ A ∧ x ∈ B |
| ¬ | Phủ định | "Không..." | ¬(x ∈ Phen(P)) |

🔗 2. Ký hiệu quan hệ, hàm & suy luận

| Ký hiệu | Tên gọi | Ý nghĩa trong khung | Ví dụ |
| --- | --- | --- | --- |
| f: A → B | Ánh xạ / Hàm | f gán mỗi phần tử của A cho một phần tử của B | Phen: PERSPECTIVES → ℘(R) |
| ℘(R) | Tập lũy thừa | Tập tất cả các tập con của R | Phen(P) ∈ ℘(R) |
| Constituent: Phenomenon → ℘(R) | Hàm cấu thành | Mỗi hiện tượng ánh xạ tới tập các thành phần cơ bản | Constituent(x) = {c₁, c₂, ...} |
| Laws(P) | Tập quy luật trong P | Các regularity hoặc relation ổn định dưới góc nhìn P | L ∈ Laws(P) |
| ⊢ | Suy ra (syntactic entailment) | Từ tiền đề, ta suy ra kết luận theo quy tắc | Theory T ⊢ Phenomenon y |
| ⊨ | Thỏa mãn (semantic entailment) | Một mô hình làm cho mệnh đề đúng | Model M ⊨ φ |
| L(x₁,...,xₙ) | Quan hệ n-ngôi | Luật dưới dạng quan hệ giữa các đối tượng | L(a,b,c) |

🌀 3. Ký hiệu modal & epistemic (dùng sau này)

| Ký hiệu | Tên gọi | Ý nghĩa | Ví dụ áp dụng |
| --- | --- | --- | --- |
| ◻φ | Tất yếu (necessity) | φ đúng trong mọi thế giới khả hữu / mọi góc nhìn liên quan | ◻(Law L holds) |
| ◇φ | Khả hữu (possibility) | φ đúng trong ít nhất một thế giới khả hữu | ◇(New Perspective emerges) |
| Kₐφ | Agent a biết rằng φ | Epistemic logic: tri thức của một quan sát viên | K_observer(Phenomenon x) |
| [α]φ | Sau hành động α, φ đúng | Dynamic logic: cập nhật tri thức | [Observe]Kₐ(Phen(P)) |

⚠️ Lưu ý: Nhóm này chưa cần dùng ngay. Chỉ kích hoạt khi bạn bắt đầu mô hình hóa "không gian các góc nhìn khả dĩ".

🏗️ 4. Ký hiệu category theory (dự phòng nâng cao)

| Ký hiệu | Tên gọi | Ý nghĩa trong khung | Ví dụ |
| --- | --- | --- | --- |
| Obj(𝒞) | Đối tượng của category 𝒞 | Các nút trong mạng khái niệm | Obj(PerspCat) = PERSPECTIVES |
| Hom(P,Q) hoặc P → Q | Morphism từ P đến Q | Phép chuyển đổi / ánh xạ giữa hai góc nhìn | f: P → Q |
| F: 𝒞 → 𝒟 | Functor | Ánh xạ bảo toàn cấu trúc giữa hai category | F: PerspCat → Set, F(P) = Phen(P) |
| F(f): F(P) → F(Q) | Ảnh của morphism qua functor | Cách hiện tượng biến đổi khi đổi góc nhìn | F(f): Phen(P) → Phen(Q) |

✂️ 5. Ký hiệu cho "Khoanh vùng tự nhiên" (Natural Cut)

| Ký hiệu | Ý nghĩa | Điều kiện "tự nhiên" |
| --- | --- | --- |
| {A, B} | Phân hoạch của R | A ∪ B = R, A ∩ B = ∅ |
| Cross(A,B) | Tập các luật/cạnh nối giữa A và B | `Cross(A,B) = {L |
| "Natural Cut" | Lát cắt tự nhiên | ` |
