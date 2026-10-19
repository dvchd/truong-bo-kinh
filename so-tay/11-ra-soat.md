# Đã rà soát những gì, và kết quả

*Trang này ghi lại các lần kiểm tra tự động trên toàn bộ 34 bài, để người đọc biết chỗ nào đã được soi
kỹ và chỗ nào chưa.*

---

## 1. Phạm vi

| Hạng mục | Số lượng |
|---|---|
| Bài kinh | 34 |
| Tệp văn bản trong `ban-dich/` | 458 |
| Đoạn văn có số hiệu (`<!-- seg: -->`) | 16.401 |
| Từ | 626.908 |
| Chú thích của người dịch | 2.282 |

## 2. Những gì đã kiểm tra tự động

| Kiểm tra | Cách làm | Kết quả |
|---|---|---|
| Từ bị cấm | Tìm 10 từ trong danh sách của `HUONG-DAN-CHUNG.md` | 0 chỗ |
| Ngoặc kép cong | Tìm bốn ký tự ngoặc kép cong | 0 chỗ |
| Ba chấm ngoài chú thích | Tìm `...`, loại trừ phần nằm trong `[Chú thích: ...]` | 0 chỗ |
| Ký hiệu chưa dịch | Tìm `TODO`, `XXX`, `FIXME`, `???` | 0 chỗ |
| Số hiệu đoạn trong sổ tay | Đối chiếu 16.401 số hiệu có thật trong bản dịch | 0 số hiệu sai |
| Link nội bộ trong sổ tay | Kiểm từng đường dẫn `.md` | 0 link hỏng |
| Chín danh hiệu Đức Thế Tôn | So khớp từng chữ giữa 23 lần xuất hiện | 1 cách viết duy nhất |
| Công thức "khéo thuyết giảng" | So khớp 18 lần xuất hiện | **5 cách viết** — đã ghi nhận, chưa sửa |

Hai script dùng để kiểm: [`cong-cu/ra-soat-toan-bo.py`](../cong-cu/ra-soat-toan-bo.py) và
[`cong-cu/kiem-tra-so-tay.py`](../cong-cu/kiem-tra-so-tay.py). Cả hai chạy được bất cứ lúc nào.

## 3. Những gì **chưa** kiểm tra

Nói rõ để không hiểu quá mức:

- **Chất lượng văn chương**: máy không đánh giá được câu nào hay, câu nào lủng củng. Việc này do người
  đọc và người biên tập làm.
- **Độ chính xác so với nguyên bản Pali**: mới đối chiếu từng đoạn với bản dịch tiếng Anh của Bhikkhu
  Sujato, chưa đối chiếu toàn bộ với chú giải Pali.
- **Tính nhất quán của các công thức lặp**: đã phát hiện một công thức có 5 cách viết (xem
  [`01-cong-thuc-lap-lai.md`](01-cong-thuc-lap-lai.md) §3.2), chưa thống nhất.
- **Các chỗ còn tranh luận trong giới nghiên cứu**: sổ tay ghi nhận, không tự quyết (xem
  [`05-mau-thuan.md`](05-mau-thuan.md) và [`06-doc-them.md`](06-doc-them.md) §4).

## 4. Nếu bạn tìm thấy lỗi

Mở issue trên kho kèm số hiệu đoạn (`dnN:x.y`) — mọi chỗ trong bản dịch đều có số hiệu để tra cứu.
