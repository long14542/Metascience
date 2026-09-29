---
source: originals/Framework hiểu và xử lý kiến thức.docx
type: docx
---

# Framework hiểu và xử lý kiến thức

Framework hiểu và xử lý kiến thức

Framework có hai bộ phận khác bản chất:

                         FRAMEWORK

                             │

             ┌───────────────┴────────────────┐

             ↓                                ↓

    CẤU TRÚC CẦN HIỂU                  CƠ CHẾ XỬ LÝ BẾ TẮC

             │                                │

             ↓                                ↓

   kiến thức cần được                    khi quá trình hiểu

   cấu tạo như thế nào                   bị nghẽn thì xử lý ra sao

Cấu trúc cần hiểu xác định người học phải xây dựng mô hình nhận thức nào.

Cơ chế xử lý bế tắc không phải một phần nội dung của kiến thức. Nó là cơ chế điều khiển: khi phát hiện một phần của mô hình chưa hình thành hoặc chưa vận hành được, chỉ mở đúng phần cần thiết để xử lý nút đó.

Vì vậy không được biến toàn bộ framework thành:

Bước 1

↓

Bước 2

↓

Bước 3

↓

...

Framework là một cấu trúc nhiều tầng, trong đó một số quan hệ là dependency, một số là phương tiện biểu diễn, một số là tiêu chuẩn kiểm tra và một số là cơ chế điều khiển.

I. Bối cảnh: kiến thức này xuất hiện để làm gì?

Đây là tầng xác định vai trò của kiến thức trong vấn đề đang xét.

VẤN ĐỀ

   │

   ↓

MỤC TIÊU

   │

   ↓

CÁCH HIỆN TẠI

   │

   ↓

GIỚI HẠN CỦA CÁCH HIỆN TẠI

   │

   ↓

PHẦN CHƯA ĐƯỢC GIẢI QUYẾT

   │

   ↓

KIẾN THỨC MỚI

Ở đây cần phân biệt rất rõ giới hạn và phần chưa được giải quyết.

GIỚI HẠN CỦA CÁCH HIỆN TẠI là đặc điểm của cách cũ: nó không thể làm được một việc nào đó cần thiết để đạt mục tiêu.

PHẦN CHƯA ĐƯỢC GIẢI QUYẾT là hệ quả của việc xác định giới hạn: chính xác cái gì vẫn còn thiếu đối với mục tiêu.

Do đó:

GIỚI HẠN

    │

    └──→ xác định

             ↓

      PHẦN CHƯA ĐƯỢC GIẢI QUYẾT

Không nên coi GIỚI HẠN và KHOẢNG TRỐNG là hai node độc lập ngang hàng. Nếu dùng thuật ngữ khoảng trống, nó phải được hiểu là phần thiếu được xác định từ giới hạn, không phải một thành phần mới được thêm vào danh sách. Nguồn gốc mô tả chính xác chuỗi “cách hiện tại làm được gì → không làm được gì → khoảng trống xuất hiện ở đâu”.

Tầng này trả lời:

Đang giải quyết vấn đề gì?

        ↓

Muốn đạt cái gì?

        ↓

Cách hiện tại thiếu ở đâu?

        ↓

Phần nào vì thế cần được giải quyết?

        ↓

Kiến thức hiện tại có vai trò gì?

Đây là động cơ của kiến thức, không phải toàn bộ kiến thức.

II. Vị trí của kiến thức trong hệ thống

Động cơ và vị trí hệ thống có liên hệ nhưng không trùng nhau.

ĐỘNG CƠ → Vì sao kiến thức này cần thiết cho vấn đề hiện tại?

VỊ TRÍ HỆ THỐNG → Kiến thức này nằm ở đâu trong toàn bộ hệ thống tri thức?

Quan hệ hệ thống có thể biểu diễn:

KIẾN THỨC TRƯỚC

       │

       ↓

KIẾN THỨC HIỆN TẠI

       │

       ↓

KHẢ NĂNG ĐƯỢC MỞ RA

       │

       ↓

KIẾN THỨC PHÍA SAU

Nhưng bốn quan hệ này không phải bốn bước ngang hàng. Chúng là các quan hệ khác nhau mà kiến thức hiện tại có thể có:

KIẾN THỨC HIỆN TẠI

    │

    ├── dựa trên cái gì?

    │

    ├── giải quyết vấn đề nào?

    │

    ├── làm xuất hiện khả năng nào?

    │

    └── trở thành tiền đề cho cái gì?

Động cơ giải thích sự cần thiết trong ngữ cảnh hiện tại.

Vị trí hệ thống giải thích quan hệ của kiến thức với mạng lưới tri thức lớn hơn.

Vì vậy không được gộp chúng thành một mục, nhưng cũng không được biến bốn quan hệ của vị trí thành bốn “tầng hiểu” độc lập. Nguồn xác định rõ vị trí là quan hệ của kiến thức hiện tại với phần trước và phần sau của hệ thống.

III. Cấu trúc nội tại của kiến thức

Đây mới là phần trả lời câu hỏi: KIẾN THỨC NÀY GỒM NHỮNG GÌ VÀ CÁC THỨ ĐÓ LIÊN HỆ VỚI NHAU NHƯ THẾ NÀO?

                         KIẾN THỨC

                             │

             ┌───────────────┴───────────────┐

             ↓                               ↓

       THÀNH PHẦN                           QUAN HỆ

             │                               │

       ┌─────┼─────┐                         ↓

       ↓     ↓     ↓                     DEPENDENCY

    object  function  ...                    │

                                             ↓

                                    A phụ thuộc vào B

                                    A tác động lên B

                                    A tạo ra B

                                    A được suy ra từ B

THÀNH PHẦN trả lời: Có những đối tượng, cấu trúc, phép toán, function, điều kiện hoặc thành phần nào?

QUAN HỆ trả lời: Các thành phần đó liên hệ với nhau thế nào?

DEPENDENCY không phải một mục ngang hàng với quan hệ. Nó là một loại quan hệ, đặc biệt quan trọng vì nó cho biết thứ tự phụ thuộc trong việc xây dựng và hiểu kiến thức.

Vì vậy:

QUAN HỆ

   │

   └──→ DEPENDENCY

chứ không phải:

THÀNH PHẦN

QUAN HỆ

DEPENDENCY

ba node ngang hàng.

Nguồn cũng phân biệt chính xác hai bế tắc:

Không biết từng thành phần là gì → thiếu THÀNH PHẦN

Biết từng thành phần nhưng không biết chúng liên hệ thế nào → thiếu QUAN HỆ

IV. Phân biệt tầng của các thành phần

Đây không phải một “tầng hiểu” mới đứng sau cấu trúc. Đây là quy tắc để cấu trúc không bị lẫn tầng.

ĐỐI TƯỢNG

    │

    ↓

GIÁ TRỊ CỦA ĐỐI TƯỢNG

    │

    ↓

PHÉP TOÁN / FUNCTION TÁC ĐỘNG

    │

    ↓

KẾT QUẢ

    │

    ↓

TÍNH CHẤT CỦA KẾT QUẢ

Ví dụ, không được coi:

Object và giá trị của object là cùng một loại thực thể.

Tương tự function không đồng nhất với giá trị đầu ra của function                          và kết quả không đồng nhất với tính chất của kết quả

Đây là quy tắc phân tầng của cấu trúc, không phải một mục mới trong framework. Nếu tách nó thành một “dạng hiểu” ngang hàng với quan hệ, ta lại tạo ra chính lỗi phân loại mà framework cần tránh. Nguồn nhấn mạnh việc phân biệt object, function, phép toán, giá trị và vai trò của từng thành phần.

V. Cơ chế vận hành

Sau khi biết cấu trúc, cần biết cấu trúc đó làm việc như thế nào.

MỤC TIÊU

   │

   ↓

CẦN ĐẠT ĐƯỢC GÌ?

   │

   ↓

DÙNG NHỮNG GÌ ĐÃ CÓ?

   │

   ↓

CẦN TẠO / BIẾN ĐỔI CÁI GÌ?

   │

   ↓

CONSTRUCTION

   │

   ↓

KẾT QUẢ

   │

   ↓

TẠI SAO KẾT QUẢ ĐÚNG / TẤT YẾU?

   │

   ↓

HỆ QUẢ

Ở đây phải sửa một điểm quan trọng của bản trước: CONSTRUCTION, KẾT QUẢ, TÍNH TẤT YẾU, HỆ QUẢ không phải bốn thành phần ngang hàng của framework.

Chúng tạo thành một dependency:

CONSTRUCTION

      │

      ↓

   KẾT QUẢ

      │

      ↓

TÍNH TẤT YẾU CỦA KẾT QUẢ

      │

      ↓

    HỆ QUẢ

Còn mục tiêu và các thành phần đã biết cung cấp điều kiện đầu vào cho construction. Vì vậy cấu trúc đầy đủ là:

MỤC TIÊU + CÁI ĐÃ BIẾT + RÀNG BUỘC

                    │

                    ↓

              CONSTRUCTION

                    │

                    ↓

                 KẾT QUẢ

                    │

                    ↓

           VÌ SAO KẾT QUẢ ĐÚNG?

                    │

                    ↓

                 HỆ QUẢ

CƠ CHẾ là tên của toàn bộ quan hệ vận hành này.

Nguồn cũng xác định cơ chế là quan hệ giữa mục tiêu, các thành phần đã có, construction, kết quả và hệ quả; vì vậy không nên tách chúng thành những node ngang hàng.

VI. Construction

CONSTRUCTION là phần đặc biệt quan trọng khi kiến thức yêu cầu xây dựng một đối tượng, cấu trúc hoặc lập luận.

CẦN TẠO RA CÁI GÌ?

        │

        ↓

CÓ NHỮNG GÌ ĐÃ CÓ?

        │

        ↓

CÁC RÀNG BUỘC

        │

        ↓

CÓ THỂ XÂY DỰNG NHƯ THẾ NÀO?

        │

        ↓

CONSTRUCTION

        │

        ↓

ĐỐI TƯỢNG / CẤU TRÚC ĐƯỢC TẠO RA

Bế tắc ở construction có nghĩa:

Biết mục tiêu

+

biết các thành phần

+

biết điều kiện cần thỏa

nhưng chưa biết cách

xây dựng cái cần có.

Đây là một loại bế tắc trong cơ chế, không phải một “tầng hiểu” độc lập ngang với động cơ.

VII. Tính tất yếu

Sau construction còn một câu hỏi khác:

Đã biết construction

        ↓

Đã có kết quả

        ↓

Tại sao kết quả đó phải đúng?

Do đó:

CONSTRUCTION → làm thế nào tạo ra kết quả?

TÍNH TẤT YẾU → tại sao kết quả đó bắt buộc đúng từ những điều kiện đã có?

Hai câu hỏi này không được nhập vào nhau.

Không biết cách xây → bế tắc construction.

Biết cách xây nhưng không biết vì sao kết quả đúng → bế tắc tính tất yếu.

Nguồn phân biệt trực tiếp hai trường hợp này.

VIII. Hệ quả

HỆ QUẢ cũng không phải một node ngang hàng với KẾT QUẢ.

CONSTRUCTION

      ↓

KẾT QUẢ TRỰC TIẾP

      ↓

ĐIỀU GÌ TRỞ NÊN KHẢ DỤNG?

      ↓

HỆ QUẢ

Kết quả là cái construction trực tiếp tạo ra.

Hệ quả là cái có thể suy ra, sử dụng hoặc xây dựng tiếp nhờ kết quả đó.

Vì vậy:

Kết quả → cái vừa được tạo ra.

Hệ quả → cái trở nên đúng / khả dụng sau khi có kết quả.

Nếu bỏ phân biệt này, phần “cơ chế” sẽ lại trộn output với consequence.

IX. Trực giác, ví dụ và pattern

Ba thứ này cũng không thể đặt ngang hàng với động cơ, cấu trúc, cơ chế.

Chúng thuộc về cách biểu diễn và nén cấu trúc đã hiểu.

                 CẤU TRÚC ĐÃ XÁC ĐỊNH

                         │

             ┌───────────┼───────────┐

             ↓           ↓           ↓

          VÍ DỤ       TRỰC GIÁC    NÉN / PATTERN

             │           │           │

             └───────────┴───────────┘

                         ↓

                 BIỂU DIỄN DỄ VẬN HÀNH

VÍ DỤ giữ lại một instance cụ thể của cấu trúc.

TRỰC GIÁC cung cấp một mô hình dễ hình dung về quan hệ đang vận hành.

PATTERN / NÉN loại bỏ chi tiết không cần thiết để giữ lại cấu trúc chung giữa nhiều trường hợp.

Do đó:

Ví dụ → cụ thể hóa.

Trực giác → hình dung hóa.

Pattern / nén → khái quát hóa và giảm độ phức tạp.

Không phải lúc nào cũng cần cả ba. Chúng được dùng khi chúng giải quyết một khó khăn nhận thức cụ thể. Nguồn xác định trực tiếp rằng trực giác, pattern và ví dụ là phương tiện hỗ trợ cấu trúc, không phải các node ngang hàng với động cơ hay cấu trúc.

X. Kiểm tra cấu trúc đã hiểu

Sau khi cấu trúc đã được xây dựng, có một lớp khác:

CẤU TRÚC ĐÃ HIỂU

        │

        ├────────→ TÁI TẠO

        │

        ├────────→ TRANSFER

        │

        ├────────→ GENERATIVITY

        │

        └────────→ ROBUSTNESS

Đây là các phép kiểm tra, không phải các tầng nội dung phải đi tuần tự.

Tái tạo

Đã xem construction

        ↓

bỏ lời giải

        ↓

tự dựng lại

Mục tiêu là phân biệt:

nhận diện lời giải với có khả năng tự suy luận lại.

Nguồn nhấn mạnh rằng cảm giác quen thuộc với lời giải không chứng minh construction đã trở thành tri thức; phải bỏ lời giải và tự tái tạo.

Transfer

Cấu trúc đã hiểu

        ↓

thay đổi instance / điều kiện / ngữ cảnh

        ↓

vẫn vận dụng được cấu trúc

Transfer kiểm tra khả năng giữ lại cấu trúc khi biểu hiện cụ thể thay đổi.

Generativity

Cấu trúc đã hiểu

        ↓

suy luận tiếp

        ↓

kết quả mới

Generativity kiểm tra khả năng dùng nguyên lý để sinh ra suy luận hoặc kết quả mới.

Robustness

Cấu trúc đã hiểu

        ↓

điều kiện thay đổi / có dữ liệu bất thường

        ↓

cấu trúc còn hoạt động không?

Robustness kiểm tra độ bền của mô hình, không chỉ khả năng áp dụng vào một trường hợp mới.

Transfer, generativity và robustness vì vậy không phải ba “bước sau tái tạo”. Chúng là ba kiểu kiểm tra khác nhau trên cùng một cấu trúc. Nguồn cũng quy định rằng không phải kiến thức nào cũng cần cả ba.

XI. Mức độ kiểm tra không cố định

Không được biến các phép kiểm tra thành một chuỗi bắt buộc:

Tái tạo

↓

Transfer

↓

Generativity

↓

Robustness

Cấu trúc đúng là:

                  CẤU TRÚC ĐÃ HIỂU

                         │

          ┌──────────────┼──────────────┐

          ↓              ↓              ↓

       TÁI TẠO        TRANSFER     GENERATIVITY

          │              │              │

          └──────────────┼──────────────┘

                         ↓

                    ROBUSTNESS

Việc chọn phép kiểm tra phụ thuộc vào vai trò của kiến thức:

kiến thức thông thường → mức hiểu cần thiết.

kiến thức quan trọng → cần thêm tái tạo.

kiến thức nền tảng → cần thêm transfer / generativity.

kiến thức cần độ bền → cần robustness.

Vì vậy không được lấy “đủ tất cả các tầng” làm tiêu chuẩn chung. Nguồn xác định rõ mức độ cần thiết phụ thuộc vào vai trò của kiến thức.

XII. Toàn bộ cấu trúc hiểu

Sau khi loại các phần trùng và sửa các quan hệ không ngang hàng, cấu trúc tổng thể nên là:

                              KIẾN THỨC

                                  │

              ┌───────────────────┼───────────────────┐

              ↓                   ↓                   ↓

          BỐI CẢNH             CẤU TRÚC          VỊ TRÍ HỆ THỐNG

              │                   │                   │

       ┌──────┴──────┐      ┌─────┴─────┐       trước / hiện tại / sau

       ↓             ↓      ↓           ↓

     VẤN ĐỀ        MỤC TIÊU  THÀNH PHẦN  QUAN HỆ

                       │         │           │

                       ↓         ↓       DEPENDENCY

                 GIỚI HẠN      vai trò

                       │

                       ↓

              PHẦN CHƯA GIẢI QUYẾT

                       │

                       ↓

                  KIẾN THỨC MỚI

                       │

                       ↓

                    CƠ CHẾ

                       │

                 ┌─────┴─────┐

                 ↓           ↓

           CONSTRUCTION    ĐÃ CÓ GÌ?

                 │

                 ↓

              KẾT QUẢ

                 │

                 ↓

          TÍNH TẤT YẾU

                 │

                 ↓

              HỆ QUẢ

                       │

                       ↓

              BIỂU DIỄN / NÉN

                       │

             ┌─────────┼─────────┐

             ↓         ↓         ↓

           VÍ DỤ    TRỰC GIÁC  PATTERN

                       │

                       ↓

               CẤU TRÚC ĐÃ HIỂU

                       │

          ┌────────────┼────────────┐

          ↓            ↓            ↓

       TÁI TẠO      TRANSFER   GENERATIVITY

                                      │

                                      ↓

                                  ROBUSTNESS

Điểm quan trọng nhất của sơ đồ này là các loại quan hệ đã được tách ra:

BỐI CẢNH → tại sao kiến thức cần thiết.

CẤU TRÚC → kiến thức gồm gì và các phần liên hệ thế nào.

CƠ CHẾ → cấu trúc vận hành thế nào.

BIỂU DIỄN / NÉN → làm cấu trúc dễ hình dung và khái quát thế nào.

KIỂM TRA → cấu trúc đã hiểu có thực sự vận hành được không.

VỊ TRÍ HỆ THỐNG → kiến thức này nằm ở đâu trong mạng lưới tri thức.

Đây là lý do không nên gom tất cả thành “10 dạng” hoặc “10 bước”. Các thành phần cũ không cùng một loại nên không thể được liệt kê như một dãy ngang hàng.

XIII. Cơ chế xử lý bế tắc

Đây là một hệ thống khác, đặt lên trên cấu trúc hiểu.

                       CẤU TRÚC HIỂU

                            │

                            ↓

                    PHÁT HIỆN BẾ TẮC

                            │

                            ↓

                   XÁC ĐỊNH NODE THIẾU

                            │

                            ↓

                XÁC ĐỊNH LOẠI BẾ TẮC

                            │

          ┌─────────────────┼─────────────────┐

          ↓                 ↓                 ↓

       BỐI CẢNH          CẤU TRÚC          CƠ CHẾ

          │                 │                 │

          ↓                 ↓                 ↓

       động cơ       thành phần / quan hệ  construction /

                                             tất yếu

          │                 │                 │

          └─────────────────┼─────────────────┘

                            ↓

                       XỬ LÝ ĐÚNG NODE

                            │

                            ↓

                       KIỂM TRA LẠI

                            │

                 ┌──────────┴──────────┐

                 ↓                     ↓

               ĐỦ                    CHƯA ĐỦ

                 │                     │

                 ↓                     ↓

            ĐÓNG NHÁNH              MỞ SÂU HƠN

Bản chất của chu trình không phải luôn luôn đi từ tầng 1 đến tầng cuối mà là:

BẾ TẮC Ở ĐÂU

      ↓

MỞ ĐÚNG PHẦN ĐÓ

      ↓

GIẢI QUYẾT

      ↓

KIỂM TRA

      ↓

ĐỦ THÌ ĐÓNG

Đây là nguyên tắc điều khiển xuyên suốt của framework: chỉ mở thêm tầng khi tầng hiện tại chưa đủ để giải quyết vấn đề, và đóng lại khi đã đủ.

XIV. Bản đồ các loại bế tắc

Vì bế tắc là chẩn đoán trên cấu trúc, nó cũng không được biểu diễn thành một dãy ngang hàng đơn giản.

                         BẾ TẮC

                            │

          ┌─────────────────┼─────────────────┐

          ↓                 ↓                 ↓

      BỐI CẢNH           CẤU TRÚC          CƠ CHẾ

          │                 │                 │

          ↓           ┌─────┴─────┐     ┌─────┴─────┐

       động cơ        ↓           ↓     ↓           ↓

                   thành phần   quan hệ construction

                                                   │

                                                   ↓

                                             tính tất yếu

                            │

                            ↓

                     KHẢ NĂNG VẬN HÀNH

                            │

                 ┌──────────┼──────────┐

                 ↓          ↓          ↓

              tái tạo    transfer   generativity

                                         │

                                         ↓

                                     robustness

                            +

                     VỊ TRÍ HỆ THỐNG

Các bế tắc này có bản chất khác nhau:

Bối cảnh → không hiểu vì sao kiến thức cần thiết.

Thành phần → không biết chính xác các thành phần / vai trò.

Quan hệ → biết các thành phần nhưng không biết chúng liên hệ thế nào.

Construction → biết cần tạo gì nhưng không biết cách xây.

Tính tất yếu → biết construction nhưng không biết vì sao kết quả bắt buộc đúng.

Tái tạo → nhận ra lời giải nhưng không tự dựng lại được.

Transfer → hiểu trường hợp cũ nhưng không vận dụng được khi cấu trúc xuất hiện trong trường hợp mới.

Generativity → không dùng được cấu trúc để sinh ra suy luận mới.

Robustness → cấu trúc sụp đổ khi điều kiện thay đổi hoặc xuất hiện dữ liệu bất thường.

Vị trí hệ thống → hiểu kiến thức cục bộ nhưng không biết nó liên hệ thế nào với hệ thống lớn.

Các dạng này không phải mười bước liên tiếp. Chúng là những vị trí khác nhau mà quá trình hiểu có thể bị nghẽn.

XV. Tiêu chuẩn kết thúc

Không có tiêu chuẩn:

đã đi qua hết mọi mục

→ coi như hiểu.

Tiêu chuẩn đúng là:

NÚT BẾ TẮC ĐÃ ĐƯỢC GIẢI QUYẾT

            │

            ↓

CẤU TRÚC CẦN THIẾT ĐÃ HÌNH THÀNH

            │

            ↓

MỨC KIỂM TRA PHÙ HỢP VỚI VAI TRÒ KIẾN THỨC

            │

            ↓

ĐÓNG NHÁNH

            │

            ↓

QUAY LẠI MẠCH HỌC CHÍNH

Mức tối thiểu:

biết vấn đề đang giải quyết

+

biết vai trò của kiến thức

+

hiểu cấu trúc và cơ chế cần thiết

+

không còn bế tắc hiện tại

Nếu kiến thức quan trọng:

+

tự tái tạo được

Nếu kiến thức nền tảng:

+

transfer / generativity

Nếu cần kiểm tra độ bền:

+

robustness

Sau khi đạt mức cần thiết thì đóng nhánh. Không tiếp tục đào chỉ vì vẫn có thể đặt thêm câu hỏi.

Cấu trúc cuối cùng, rút về đúng các tầng

Nếu cần một sơ đồ duy nhất để giữ làm khung chuẩn, thì nên dùng:

                              KIẾN THỨC

                                  │

        ┌─────────────────────────┼─────────────────────────┐

        ↓                         ↓                         ↓

     BỐI CẢNH                  CẤU TRÚC              VỊ TRÍ HỆ THỐNG

        │                         │                         │

        ↓                  ┌──────┴──────┐                  ↓

 Vấn đề / Mục tiêu         Thành phần   Quan hệ        Trước / Sau

        │                         │          │

        ↓                         │      Dependency

 Cách hiện tại                   │

        │                         │

        ↓                         │

     Giới hạn                    │

        │                         │

        ↓                         │

 Phần chưa giải quyết             │

        │                         │

        └──────────────┬──────────┘

                       ↓

                    CƠ CHẾ

                       │

              ┌────────┴────────┐

              ↓                 ↓

        CONSTRUCTION         Cái đã có

              │

              ↓

           KẾT QUẢ

              │

              ↓

       TÍNH TẤT YẾU

              │

              ↓

           HỆ QUẢ

                       │

                       ↓

                BIỂU DIỄN / NÉN

                       │

              ┌────────┼────────┐

              ↓        ↓        ↓

            Ví dụ   Trực giác  Pattern

                       │

                       ↓

                CẤU TRÚC ĐÃ HIỂU

                       │

          ┌────────────┼────────────┐

          ↓            ↓            ↓

       Tái tạo      Transfer    Generativity

                                     │

                                     ↓

                                 Robustness

        ─────────────────────────────────────

                 CƠ CHẾ ĐIỀU KHIỂN

        ─────────────────────────────────────

      Phát hiện bế tắc

             ↓

      Xác định node thiếu

             ↓

      Mở đúng phần cần thiết

             ↓

      Xử lý

             ↓

      Kiểm tra

          ↙     ↘

       đủ       chưa đủ

        ↓          ↓

      đóng      mở sâu hơn

Như vậy, những gì trước đây bị viết thành các mục ngang hàng đã được trả về đúng tầng:

GIỚI HẠN

→ dẫn tới phần chưa giải quyết, không ngang hàng độc lập.

DEPENDENCY

→ thuộc QUAN HỆ.

CONSTRUCTION

→ thuộc CƠ CHẾ.

KẾT QUẢ

→ đầu ra của CONSTRUCTION.

TÍNH TẤT YẾU

→ giải thích vì sao KẾT QUẢ đúng.

HỆ QUẢ

→ phát sinh từ KẾT QUẢ.

VÍ DỤ / TRỰC GIÁC / PATTERN

→ phương tiện biểu diễn và nén, không phải tầng nội dung ngang hàng.

TÁI TẠO / TRANSFER / GENERATIVITY / ROBUSTNESS

→ phép kiểm tra trên cấu trúc đã hiểu, không phải chuỗi bước bắt buộc.

VỊ TRÍ HỆ THỐNG

→ quan hệ của kiến thức với toàn bộ hệ thống, không phải bước cuối.

XỬ LÝ BẾ TẮC

→ cơ chế điều khiển nằm trên toàn bộ framework, không phải một phần của nội dung kiến thức.

Đây là điểm sửa căn bản so với bản trước: không còn lấy mọi khái niệm đúng về mặt nội dung rồi xếp chúng thành một danh sách ngang hàng. Mỗi thành phần được đặt vào đúng vai trò của nó: node nội dung, quan hệ, dependency, quan hệ vận hành, phương tiện biểu diễn, phép kiểm tra hoặc cơ chế điều khiển. Cấu trúc này mới phù hợp với yêu cầu “đầy đủ nhưng không thừa, không lẫn tầng, không biến framework thành checklist”.
