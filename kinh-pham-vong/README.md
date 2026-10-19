# Kinh Phạm Võng — *Brahmajāla Sutta*

> Bài kinh số 1 trong Trường Bộ Kinh (*Dīgha Nikāya*), kinh tạng Pali.

**Đọc bản dịch hoàn chỉnh: [`Kinh-Pham-Vong.md`](Kinh-Pham-Vong.md)**

---

## Về bài kinh

Đức Phật đang đi giữa Vương Xá và Nāḷandā cùng 500 tỳ-kheo. Trên cùng con đường ấy, du sĩ Suppiya liên tục chê bai Phật – Pháp – Tăng, còn người học trò Brahmadatta lại hết lời ca ngợi. Thầy một đằng, trò một nẻo, công khai chống nhau suốt dọc đường.

Từ chuyện nhỏ ấy, Đức Phật mở ra một trong những bản đồ tư tưởng đồ sộ nhất của Ấn Độ cổ đại: **62 quan điểm** về bản chất con người và thế giới — 18 quan điểm suy đoán về **quá khứ**, 44 quan điểm suy đoán về **tương lai** — tất cả được phân loại, mổ xẻ, và chỉ ra chỗ sai.

Rồi Ngài kết luận bằng một câu ngắn gọn đến mức khó tin: **tất cả 62 quan điểm ấy đều khởi lên từ xúc** (sự tiếp xúc giữa giác quan, đối tượng và nhận thức), và đều nằm gọn trong vòng duyên khởi.

| Nhóm | Số lượng |
|---|---|
| Suy đoán về **quá khứ** | 18 (4 + 4 + 4 + 4 + 2) |
| Suy đoán về **tương lai** | 44 (16 + 8 + 8 + 7 + 5) |
| **Tổng** | **62** |

Bài kinh cũng là nơi Đức Phật tự đặt **năm tên** cho bài pháp của mình (đoạn 3.74.3): *Atthajāla* (Lưới ý nghĩa), *Dhammajāla* (Lưới Pháp), *Brahmajāla* (Lưới tối thượng), *Diṭṭhijāla* (Lưới quan điểm), và *Anuttara saṅgāmavijaya* (Chiến thắng vô song nơi chiến trường).

### Về nhan đề

*Brahmajāla* ghép từ *brahma* + *jāla*. Có hai cách hiểu *brahma*:

1. **danh từ riêng** — Phạm thiên (Brahmā): "tấm lưới của Phạm thiên";
2. **tính từ** — tối thượng, cao quý: "tấm lưới tối thượng".

Bản dịch này chọn cách thứ hai, theo hướng của Bhikkhu Bodhi (*The All-embracing Net of Views*), Maurice Walshe (*The Supreme Net*) và Bhikkhu Sujato (*The Divine Net*), nhưng vẫn giữ tên quen thuộc **Kinh Phạm Võng** trong tiếng Việt. Lý do được trình bày đầy đủ ở mục 1 của Lời giới thiệu.

---

## Con số

| | |
|---|---|
| Đoạn văn (segment) | **662** — khớp 100% với nguồn SuttaCentral |
| Từ (chính văn, không kể chú thích) | **36.088** |
| Ký tự toàn tệp | **194.626** |
| Chương / mục lớn | 5 mục, 62 tiểu mục quan điểm |
| Liên kết mục lục | 28 — đã kiểm tra, không có liên kết hỏng |
| Vòng rà soát độc lập | 5 |

---

## Cấu trúc thư mục

```
kinh-pham-vong/
├── Kinh-Pham-Vong.md      ← BẢN DỊCH HOÀN CHỈNH — đọc tệp này
├── README.md              ← tệp này
├── HUONG-DAN-DICH.md      ← quy chuẩn dịch (bắt buộc đọc nếu muốn dịch tiếp)
│
├── ban-dich/              ← 28 tệp: bản dịch từng phần
│   ├── 00-gioi-thieu.md       Lời giới thiệu (7 mục)
│   ├── 00-title.md            Nhan đề
│   ├── 01-wanderers.md        Mục 1 — Chuyện về những du sĩ
│   ├── 02–05-*.md             Mục 2 — Giới hạnh (3 tầng)
│   ├── 06–07-*.md             Mở đầu phần quan điểm
│   ├── 08–12-*.md             Mục 3.1 — 18 quan điểm về quá khứ
│   ├── 13–18-*.md             Mục 3.2 — 44 quan điểm về tương lai
│   ├── 19–24-*.md             Mục 4–5 — Nguồn gốc chung & bước ra
│   ├── bang-thuat-ngu.md      Bảng thuật ngữ (5 nhóm)
│   └── nguon-tham-khao.md     Nguồn tham khảo & ghi nhận
│
├── nguon/                 ← dữ liệu gốc để đối chiếu
│   ├── sections/              25 tệp, mỗi đoạn có PLI / EN / NOTE
│   ├── sc_pli.json            nguyên bản Pali theo đoạn
│   └── README.md              mô tả nguồn và giấy phép
│
├── ra-soat/               ← 5 báo cáo rà soát độc lập
│   ├── A-01-03.md             mục 1
│   ├── B-05.md                mục 2
│   ├── C-08-12.md             mục 3.1
│   ├── D-19-24.md             mục 3.2
│   └── E-gioi-thieu.md        lời giới thiệu, thuật ngữ, nguồn
│
├── ghep.py                ← ghép ban-dich/ thành Kinh-Pham-Vong.md
├── kiem-tra-marker.py     ← kiểm tra một tệp có đủ & đúng thứ tự đoạn
└── tien-do.py             ← báo cáo tiến độ dịch
```

---

## Định dạng của `nguon/sections/`

Mỗi tệp trong `nguon/sections/` chứa các đoạn như sau:

```markdown
## dn1:1.1.1

- **PLI**: Evaṁ me sutaṁ — ekaṁ samayaṁ bhagavā antarā ca rājagahaṁ ...
- **EN**: So I have heard. At one time the Buddha was traveling along the road ...
- **NOTE**: (chú thích của Bhikkhu Sujato, nếu có)
```

Mã `dn1:1.1.1` là mã đoạn của SuttaCentral — dán mã này vào `https://suttacentral.net/dn1/pli/ms` để mở đúng đoạn gốc.

Bản dịch trong `ban-dich/` mang đúng các mã ấy dưới dạng `<!-- seg: dn1:1.1.1 -->`, nhờ vậy có thể đối chiếu tự động từng câu.

---

## Làm lại bản hoàn chỉnh

```bash
cd kinh-pham-vong

# 1. Kiểm tra một tệp có đủ đoạn không
python3 kiem-tra-marker.py ban-dich/08-eternalism.md

# 2. Ghép tất cả thành Kinh-Pham-Vong.md
python3 ghep.py

# 3. Xem tiến độ
python3 tien-do.py
```

`ghep.py` đọc danh sách `ORDER` (25 tệp nội dung), ghép theo đúng thứ tự, chèn dấu phân cách, chuẩn hóa dấu ngoặc kép, rồi ghi ra `Kinh-Pham-Vong.md`.

---

## Quy ước dịch quan trọng

Toàn bộ quy ước nằm trong [`HUONG-DAN-DICH.md`](HUONG-DAN-DICH.md). Vài điểm cốt lõi:

- **Công thức lặp phải dịch giống hệt nhau ở mọi chỗ.** Kinh này được truyền miệng, mỗi khuôn câu lặp lại hàng chục lần; dịch mỗi lần một kiểu sẽ phá vỡ nhịp điệu và gây khó hiểu.
- **Không viết tắt bằng dấu `…` trong chính văn.** Chỗ Pali ghi *peyyāla* (`pe…`), bản dịch **viết đầy đủ ra**, và ghi chú lại trong `[Chú thích: …]`.
- **Thuật ngữ Hán-Việt khó hiểu được thay bằng tiếng Việt thường ngày**; thuật ngữ quen thuộc thì giữ và giải thích ngay trong ngoặc ở lần đầu xuất hiện.
- **"Cái tôi" luôn đặt trong ngoặc kép** — vì đó là một *quan niệm* đang được tranh luận, không phải thực thể có thật theo cách Đức Phật công nhận.

---

## Giấy phép

Bản dịch tiếng Việt: **CC BY-SA 4.0**. Nguyên bản Pali: phạm vi công cộng. Bản dịch tiếng Anh của Bhikkhu Sujato: **CC0**. Xem [`../LICENSE`](../LICENSE).
