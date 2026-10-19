# A — Rà soát phần mở đầu (DN 2, dn2:0–15)

**Tệp rà soát:**

- `00-title.md` — dn2:0.1–0.2
- `00-gioi-thieu.md` — lời giới thiệu, không có marker
- `01-ministers.md` — dn2:1.0–7.5 (37 đoạn)
- `02-jivaka.md` — dn2:8.0–10.12 (25 đoạn)
- `03-question.md` — dn2:11.0–15.5 (26 đoạn)

**Nguồn đối chiếu:** `nguon/sections/00-title.md`, `01-ministers.md`, `02-jivaka.md`, `03-question.md` (PLI, EN Sujato, NOTE); `HUONG-DAN-DICH.md`; `ban-dich/bang-thuat-ngu.md`. Đối chiếu trực tiếp với PLI, không chỉ bản EN.

**Ngày:** 2026-10-19.

## 1. Kiểm tra tự động

| Tệp | Marker / segment | Kết quả |
|---|---:|---|
| 00-title.md | 2/2 | ĐẠT |
| 01-ministers.md | 37/37 | ĐẠT |
| 02-jivaka.md | 25/25 | ĐẠT |
| 03-question.md | 26/26 | ĐẠT |
| **Tổng** | **90/90** | **4/4 ĐẠT** |

- `00-gioi-thieu.md` không có marker; đã đọc và đối chiếu toàn bộ 114 dòng.
- Các công thức khóa trong `01-ministers.md` còn nguyên: câu im lặng 6 lần, câu "Một vị quan đại thần khác…" 5 lần.
- Không có marker nào bị đổi, thêm, bớt; không có dấu `…` trong chính văn.

## 2. Lỗi đã sửa

| Vị trí | Vấn đề | Đã sửa thành / Đề xuất |
|---|---|---|
| `00-gioi-thieu.md` §1 (trích lời vua) | `bho` bị dịch "Này các ngài"; `HUONG-DAN-DICH.md` quy định "thưa ngài", không dùng "này ông". | Đã sửa: "Thưa các ngài…" |
| `00-gioi-thieu.md` §4, bảng mục 1 | "Nhà vua lần lượt hỏi các quan đại thần" — vua chỉ nêu một câu hỏi chung (1.6), các quan lần lượt trả lời, không phải vua hỏi từng người. | Đã sửa: "Nhà vua nêu câu hỏi; sáu vị quan đại thần lần lượt giới thiệu…" |
| `00-gioi-thieu.md` §4, bảng mục 5 | "Đức Phật nhận lời" sau khi vua quy y — Đức Phật nhận lời thú nhận (100.2), không phải nhận lời quy y; lời nhận xét cuối là với các tỳ-kheo sau khi vua ra về (102.1–102.7). | Đã sửa: "Nhà vua xin quy y và thú nhận lỗi giết cha. Đức Phật nhận lỗi ấy; sau khi vua ra về, Ngài nói thêm một lời tiếc thương với các tỳ-kheo." |
| `00-gioi-thieu.md` §5, bảng Nigaṇṭha | "bốn loại khổ hạnh tự chế" — `cātuyāmasaṃvara` là "sự thu thúc bốn mặt", không phải bốn loại khổ hạnh; `08-nigantha.md` dùng "sự thu thúc bốn mặt". | Đã sửa: "Sống thu thúc bằng sự thu thúc bốn mặt…" |
| `00-gioi-thieu.md` §6, đoạn kết | "nhà vua quy y, Đức Phật nhận lời" — cùng lỗi trình tự; lời cuối của Đức Phật là sau khi vua ra về. | Đã sửa: "nhà vua quy y và thú nhận lỗi lầm, Đức Phật nhận lỗi ấy — rồi sau khi vua ra về…" |
| `00-gioi-thieu.md` §7 | "khi vừa tới khu vườn" — PLI `avidūre ambavanassa` = "khi đến gần khu vườn", không phải "vừa tới". | Đã sửa: "khi đến gần khu vườn" |
| `00-gioi-thieu.md` §7 | "có ai phục kích không" / "sợ phục kích" — bản kinh không nói phục kích; vua hỏi Jīvaka có lừa dối, phản bội hay nộp mình cho kẻ thù không (10.4–10.6). | Đã sửa: "có phải thầy thuốc đang lừa dối, phản bội hay nộp ông cho kẻ thù không" / "sợ bị phản bội, bị nộp cho kẻ thù" |
| `00-gioi-thieu.md` §7 | "Bài kinh không kết luận gì thêm" — sai: 102.1–102.7 có lời Đức Phật với các tỳ-kheo sau khi vua ra về. | Đã sửa: "Bài kinh không thêm một lời khuyên nào cho nhà vua." |
| `00-gioi-thieu.md` §9 | "mục 4/3/5" dễ bị hiểu là mục của phần giới thiệu, không phải mục của bài kinh. | Đã sửa: "mục 4/3/5 của bài kinh" (3 chỗ). |
| `00-gioi-thieu.md` §9 | "mục 5 — đoạn cuối, ngắn nhất" — mục 5 có 796 từ, mục 2 có 765 từ (tính cả chú thích), nên không phải ngắn nhất về độ dài văn bản. | Đã sửa: "ngắn gọn". |
| `01-ministers.md` 1.2 | "tại Rājagaha (Vương Xá)" — bảng thuật ngữ quy định `Rājagaha` → `Vương Xá`; các tệp khác đã dùng "Vương Xá". | Đã sửa: "tại Vương Xá (Rājagaha)". |
| `01-ministers.md` chú thích 5.2 | "phủ nhận khả năng có hành động cùng quả báo của nó" — "của nó" lơ lửng, tối nghĩa. | Đã sửa: "phủ nhận khả năng hành động có quả báo". |
| `02-jivaka.md` 10.1 | "vua rời Rājagaha" — không nhất quán với `Vương Xá`. | Đã sửa: "vua rời Vương Xá". |

**Tổng: 13 lỗi.** Trong đó `00-gioi-thieu.md` 10 lỗi, `01-ministers.md` 2 lỗi, `02-jivaka.md` 1 lỗi. `00-title.md` và `03-question.md` không có lỗi nghĩa phải sửa.

## 3. Đề xuất chưa áp dụng

| Vị trí | Vấn đề | Đề xuất |
|---|---|---|
| `03-question.md` 14.4; cùng công thức ở `04-purana.md`–`09-sanjaya.md` và `10-first-fruit.md` | "chín thành quả an vui" là cách nói theo sát `sukhavipāka`; "chín" dễ bị đọc thành số "chín" hoặc "chín [thành quả]". Câu còn lặp "đưa đến cõi trời … dẫn tới cõi trời". | "chín muồi thành quả an vui" hoặc "có quả báo an vui"; có thể rút gọn vế lặp. Không sửa lẻ vì công thức lặp ở 03–10; đề nghị sửa đồng loạt (xem thêm `B-sau-vi-thay.md` mục 4). |

## 4. Điểm mạnh

- Bản dịch 01–03 bám sát PLI, giữ đủ 1.250 tỳ-kheo, đêm hội Komudī, trình tự sáu vị thầy, sáu học thuyết, chi tiết nhà vua sợ và câu kết về tội giết cha.
- Xưng hô nhất quán: `Bệ hạ` / `Đại vương` / `Tâu Bệ hạ` / `Bạch Đức Thế Tôn`; `Vương Xá`, `sa-môn`, `bà-la-môn`, `Ni-kiền-tử` đúng bảng thuật ngữ.
- Chú thích đặt đúng sau đoạn được chú thích, nội dung sát NOTE của Sujato; chú thích 5.2 sau khi sửa đã rõ nghĩa.
- `00-title.md` sạch; `03-question.md` rất sát PLI, chỉ còn một điểm wording thuộc công thức lặp.
- Không có marker sai, không có dấu `…` trong chính văn, không có câu tiếng Anh chưa dịch.

## 5. Ghi nhận

- **Thứ tự sáu vị thầy:** bảng §5 của phần giới thiệu theo thứ tự giáo thuyết ở mục 3 (Nigaṇṭha 3.5, Sañjaya 3.6); ở mục 1, Sañjaya được giới thiệu trước Nigaṇṭha (6.2, 7.2). Đây là đặc điểm của bản kinh, không phải lỗi; bảng đã đúng với mục 3.
- **Ngoài phạm vi:** `ban-dich/nguon-tham-khao.md` dòng 25 ghi 長阿含經 số 20, Đại Chánh Tạng 1, 202c–205c. Đối chiếu SuttaCentral, 沙門果經 là DA 27, Đại Chánh Tạng 1, 107a–109c. Đề nghị người phụ trách kiểm tra lại; không sửa vì ngoài phạm vi.

## 6. Kết luận

**ĐẠT.**

Đã sửa 13 lỗi tại `00-gioi-thieu.md`, `01-ministers.md`, `02-jivaka.md`. Các tệp có marker đều in `==> ĐẠT`: `01-ministers.md` 37/37, `02-jivaka.md` 25/25; `03-question.md` 26/26 và `00-title.md` 2/2 vẫn đạt (không sửa). Còn 1 đề xuất tinh chỉnh công thức "chín thành quả an vui" ở 03–10; không chặn nội dung.
