# E — Rà soát Lời giới thiệu, Bảng thuật ngữ, Nguồn tham khảo

**Ngày rà:** 2026-10-19 (UTC) · **Không sửa file nào trong `ban-dich/`.** Báo cáo chỉ đọc và đối chiếu.

## Bản chụp và phạm vi

| File | md5 | mtime (UTC) | bytes |
|---|---|---|---|
| `ban-dich/00-gioi-thieu.md` | `4250b985ac3f9503d8414c49c78ea96f` | 2026-10-19 06:51:38 | 14.365 |
| `ban-dich/bang-thuat-ngu.md` | `e9582bbe436641f022bc15a5c13755f3` | 2026-10-19 06:51:31 | 10.067 |
| `ban-dich/nguon-tham-khao.md` | `0365d70de0acfd535b157efe7b3a7b51` | 2026-10-19 06:51:31 | 4.963 |
| `Kinh-Pham-Vong.md` (bản gộp, dùng đối chiếu) | `a59fc38dc29482490b5b7fbffe7d74b2` | 2026-10-19 06:52:18 | 250.057 |

**Lưu ý về phiên bản.** Các file đã được chỉnh liên tục trong lúc rà (06:34 → 06:52). Toàn bộ lỗi nặng và trung bình ghi nhận ở các bản trước — nhan đề *Brahmajāla* dịch hai cách, 9/27 neo Mục lục hỏng, gán sai nhan đề Sujato, link ATI 404, sơ đồ "bốn phần" lệch 5 mục, "The Supreme Raft of Brahmā", xuất xứ đoạn Bodhi — **đã được sửa trong bản 06:51–06:52 và đã kiểm lại**. Báo cáo dưới đây chỉ giữ lỗi còn hiện hành; các mục đã sửa được ghi ở phần "Những điểm đã kiểm tra" để đối chiếu, không tính là lỗi.

**Phạm vi:** ba file được giao, đối chiếu với bản gộp `Kinh-Pham-Vong.md`, `nguon/sections/*.md`, `nguon/sc_pli.json` và các file `nguon/res_*.txt`. Các yêu cầu: số liệu, Mục lục/neo, thuật ngữ, mâu thuẫn nội bộ, chính tả/định dạng.

## Tóm tắt

| Mức | Số mục | Nội dung chính |
|---|---|---|
| **NGHIÊM TRỌNG** | 0 | Không còn lỗi nặng |
| **TRUNG BÌNH** | 0 | Không còn lỗi trung bình |
| **NHẸ** | 1 | Mục lục lặp hai mục "Bảng thuật ngữ" và "Nguồn tham khảo" ở cuối |

**Kết luận ngắn:** sau khi các lỗi nặng/trung bình được sửa, phần số liệu cốt lõi và thư mục đều khớp: DN 1 là bài đầu của 34 bài; 62 = 18 + 44; các nhóm con 4+4+4+4+2 và 16+8+8+7+5; năm tên ở 3.74.3; 662 đoạn khớp thứ tự; nhan đề nay nhất quán; 30/30 neo Mục lục đúng; glossary đã có đủ 10 thuật ngữ từng thiếu; các link chính đều 200. Lỗi còn lại chỉ là hai cặp dòng trùng trong Mục lục.

## Danh sách lỗi

### [NHẸ] `ban-dich/00-gioi-thieu.md` — Mục lục lặp hai mục ở cuối

- **Hiện tại:** cuối `## Mục lục` có bốn dòng, trong đó hai mục bị lặp:
  - `- [Bảng thuật ngữ](#bảng-thuật-ngữ)`
  - `- [Nguồn tham khảo](#nguồn-tham-khảo)`
  - `- [Bảng thuật ngữ](#bảng-thuật-ngữ)`
  - `- [Nguồn tham khảo](#nguồn-tham-khảo)`
- **Đúng ra:** mỗi heading chỉ nên có một dòng trong Mục lục. Hai mục này đã xuất hiện một lần ngay trước đó; bốn dòng cuối thực chất là hai cặp trùng. Mục lục hiện có **30 liên kết nhưng chỉ 28 mục duy nhất**.
- **Đề xuất:** xóa một trong hai cặp, giữ đúng hai dòng:
  - `- [Bảng thuật ngữ](#bảng-thuật-ngữ)`
  - `- [Nguồn tham khảo](#nguồn-tham-khảo)`

## Bảng kiểm mục lục

**Cách kiểm:** lấy toàn bộ liên kết trong `## Mục lục` của `00-gioi-thieu.md`, so với heading trong bản gộp `Kinh-Pham-Vong.md`; tính slug theo quy tắc GitHub (bỏ dấu câu, em dash bị xóa, mỗi dấu cách thành `-`, không gộp các gạch nối). Cột "Neo" chỉ đánh giá **trong bản gộp**; trong file riêng, các liên kết tới mục 1–5 vẫn chết vì heading nằm ở file khác — đó là vấn đề đóng gói, không phải neo sai.

| # | Mục trong Mục lục | Có mặt | Neo | Ghi chú |
|---|---|---|---|---|
| 1 | Lời giới thiệu | Có | Đúng | — |
| 2 | Kinh Phạm Võng — Trường Bộ Kinh, bài kinh số 1 | Có | Đúng | Trỏ tới `## Trường Bộ Kinh — bài kinh số 1: Kinh Phạm Võng` (bản gộp dòng 141) |
| 3 | 1. Chuyện về những du sĩ | Có | Đúng | — |
| 4 | 2. Giới hạnh | Có | Đúng | — |
| 5 | 2.1. Giới hạnh ngắn (*Cūḷasīla*) | Có | Đúng | — |
| 6 | 2.2. Giới hạnh trung (*Majjhimasīla*) | Có | Đúng | — |
| 7 | 2.3. Giới hạnh rộng lớn (*Mahāsīla*) | Có | Đúng | — |
| 8 | 3. Quan điểm | Có | Đúng | — |
| 9 | 3.1. Những người suy đoán về quá khứ (18 quan điểm) | Có | Đúng | — |
| 10 | 3.1.1. Thuyết trường tồn | Có | Đúng | — |
| 11 | 3.1.2. Thuyết bán trường tồn | Có | Đúng | — |
| 12 | 3.1.3. Thuyết hữu biên – vô biên | Có | Đúng | — |
| 13 | 3.1.4. Thuyết quanh co | Có | Đúng | — |
| 14 | 3.1.5. Thuyết ngẫu nhiên sinh | Có | Đúng | — |
| 15 | 3.2. Những người suy đoán về tương lai (44 quan điểm) | Có | Đúng | — |
| 16 | 3.2.1. Thuyết hữu tưởng | Có | Đúng | — |
| 17 | 3.2.2. Thuyết vô tưởng | Có | Đúng | — |
| 18 | 3.2.3. Thuyết phi tưởng phi phi tưởng | Có | Đúng | — |
| 19 | 3.2.4. Thuyết đoạn diệt | Có | Đúng | — |
| 20 | 3.2.5. Thuyết Niết-bàn ngay đời này | Có | Đúng | — |
| 21 | 4. Những căn cứ để khẳng định về "cái tôi" và thế giới | Có | Đúng | — |
| 22 | 4.1. Sự dao động và vùng vẫy | Có | Đúng | — |
| 23 | 4.2. Tất cả đều do xúc mà có | Có | Đúng | — |
| 24 | 4.3. Điều không thể xảy ra | Có | Đúng | — |
| 25 | 4.4. Tất cả đều nằm trong vòng duyên khởi | Có | Đúng | — |
| 26 | 5. Bước ra khỏi vòng luân hồi | Có | Đúng | — |
| 27 | Bảng thuật ngữ | Có | Đúng | — |
| 28 | Nguồn tham khảo | Có | Đúng | — |
| 29 | Bảng thuật ngữ (lặp) | Có | Đúng | **Trùng mục 27** — xem lỗi NHẸ |
| 30 | Nguồn tham khảo (lặp) | Có | Đúng | **Trùng mục 28** — xem lỗi NHẸ |

**Tổng hợp:** 28 mục duy nhất, tất cả có heading thật; **30/30 neo đúng**; **2 dòng lặp** (mục 29–30 trùng 27–28). Không còn heading cấp 2 nào của phần chính bị bỏ khỏi Mục lục: heading `## Trường Bộ Kinh — bài kinh số 1: Kinh Phạm Võng` đã được thêm ở vị trí 2.

## Thuật ngữ thiếu trong bảng

**Kết quả: không còn thuật ngữ quan trọng nào thiếu.** Mười từ từng thiếu đã được thêm vào `bang-thuat-ngu.md`, vị trí và định nghĩa khớp thân bài:

| Thuật ngữ | Trạng thái hiện tại |
|---|---|
| kamma | Đã có (dòng 29): "nghiệp — việc làm có chủ ý, và kết quả của nó trải qua nhiều đời" |
| dukkha | Đã có (dòng 35): "khổ — sự không toại nguyện, bất an; đi cặp với *sukha*" |
| saṃsāra | Đã có (dòng 51): "luân hồi — vòng tái sinh tiếp diễn không dứt" |
| avijjā | Đã có (dòng 39): "vô minh — sự không hiểu biết đúng như thật; mắt xích đầu của chuỗi duyên khởi" |
| bhava | Đã có (dòng 42): "sự tồn tại tiếp diễn — mắt xích thứ mười của chuỗi duyên khởi" |
| jāti | Đã có (dòng 43): "tái sinh — sự sinh ra một đời sống mới" |
| saḷāyatana | Đã có (dòng 40): "sáu lĩnh vực xúc — sáu giác quan và đối tượng của chúng" |
| upekkhā | Đã có (dòng 48): "tâm xả — sự bình thản quân bình; một chi của thiền" |
| pīti | Đã có (dòng 47): "niềm vui (hỷ) — niềm vui trong thiền" |
| sukha | Đã có (dòng 36): "dễ chịu (lạc) — cảm giác dễ chịu; một chi của thiền" |

### Thuật ngữ có trong bảng nhưng cách dùng không khớp

**Không còn mục nào lệch rõ.** Các mục từng lệch đã được sửa: `diṭṭhi` → "quan điểm" (bỏ "tà kiến"); `saññā` → "nhận biết (tưởng)"; `vedanā` → "thọ (cảm giác)"; `jhāna` → "thiền-na / tầng thiền"; `vijjā` → "môn thuật — trong kinh này chỉ ở dạng *tiracchānavijjā*"; `samaṇa` → định nghĩa mềm ("nói chung, thường chỉ..."); `loka` → đã có giải thích; `āsava` → đã bỏ (0 lần trong bài). `bhonto` nay ghi "gốc là dạng hô cách của *bhavant*; trong kinh dùng làm chủ ngữ kính trọng" — phù hợp với cách dùng `bhonto samaṇabrāhmaṇā` (chủ ngữ kính trọng) trong kinh.

## Những điểm đã kiểm tra và xác nhận đúng

Phần này chỉ ghi những gì đã kiểm tra và thấy khớp, để phân biệt với lỗi; không phải lời khen.

- **DN 1 / 34 bài:** Lời giới thiệu dòng 7 nói "bài kinh đầu tiên trong Trường Bộ Kinh, bộ kinh gồm 34 bài kinh dài". Khớp với `res_252fb4.txt` ("first of 34 suttas") và với danh sách DN hiện hành.
- **62 = 18 + 44:** thân bài 3.1/3.2 và chú thích Sujato trong `nguon/sections/07-past-intro.md` ("eighteen grounds") và `13-future-intro.md` ("forty-four grounds") khớp. Các nhóm con đúng: 4 + 4 + 4 + 4 + 2 = 18; 16 + 8 + 8 + 7 + 5 = 44. Bản dịch cũng nói rõ "mười tám căn cứ", "bốn", "hai", "mười sáu", "tám", "bảy", "năm".
- **Năm tên ở 3.74.3:** Pali `atthajālantipi ... dhammajālantipi ... brahmajālantipi ... diṭṭhijālantipi ... anuttaro saṅgāmavijayotipi`; bản dịch 3.74.3 có đủ năm tên, đúng thứ tự.
- **Nhan đề nay nhất quán:** Lời giới thiệu (dòng 18), 0.2 và 3.74.3 đều dùng "tấm lưới tối thượng"/"Lưới tối thượng"; Lời giới thiệu trình bày cả hai cách hiểu và nói rõ vì sao chọn cách thứ hai; chú thích 3.74.3 dẫn Bodhi/Walshe/Sujato, không còn lập luận "đứng ngang hàng". Câu "trùng tên" ở dòng 67 cũng đã sửa thành "cùng ghép từ *brahma* (Phạm) và *jāla* (lưới)".
- **662 đoạn:** bản gộp có 662 thẻ `<!-- seg: dn1:... -->`; `nguon/sc_pli.json` có 662 khóa trong `keys_order`; hai danh sách **trùng khớp từng phần tử, cùng thứ tự, không thiếu, không thừa, không trùng lặp**. Lời tuyên bố trong `nguon-tham-khao.md` §5 là đúng.
- **Đoạn trích Bhikkhu Bodhi:** khớp nguyên văn với `res_252fb4.txt` dòng 10, chỉ khác `Brahmajála`/`Brahmajāla` và có dấu ba chấm thay cho mệnh đề giữa. Bản dịch tiếng Việt trong Lời giới thiệu trung thành với đoạn này. Nguồn đã sửa đúng thành "Introduction to *The Discourse on the Fruits of Recluseship* (BPS, 2008), được *Encyclopedia of Buddhism* dẫn lại".
- **`jāla` = "cái lưới", không phải "cái bè":** kết luận chính đúng; note 06:51 đã sửa thành "trong ngữ cảnh nhan đề, *jāla* là 'cái lưới'; còn 'cái bè' là nghĩa của những từ khác hẳn (*kulla*, *nāvā*)", và Nguồn tham khảo đã sửa "The Supreme Raft" → "Raft of Brahmā", khớp `res_38e177.txt`.
- **Thư mục:** Sujato nay là *The Divine Net*; Bodhi 1978 có phụ đề "Commentarial Exegesis"; Rhys Davids thuộc *Sacred Books of the Buddhists*; link ATI `dn.01.0.bodh.html` trả 200; link Phật Sự Online là URL bài viết, trả 200; link dhammatalks.org của Thanissaro trả 200.
- **Các liên kết còn lại:** `https://suttacentral.net/dn1/pli/ms`, `https://suttacentral.net/dn1/en/sujato`, `https://encyclopediaofbuddhism.org/wiki/Brahmajāla_Sutta`, `https://en.wikipedia.org/wiki/Brahmajāla_Sutta` đều trả HTTP 200.
- **"Không phải ai thời Đức Phật cũng tin vào tái sinh":** luận điểm này có cơ sở từ chính thân bài — nhóm đoạn diệt (3.2.4) và nhóm ngẫu nhiên sinh (3.1.5) — đúng như Lời giới thiệu nói; không phải lỗi.
- **Bối cảnh mở đầu:** 500 tỳ-kheo, đường Vương Xá–Nāḷandā, Ambalaṭṭhikā, gian nhà tròn (`maṇḍalamāḷa`), Suppiya và Brahmadatta — khớp `nguon/sections/01-wanderers.md`.
- **Sơ đồ "bốn phần":** dòng 39 nay ghi rõ "bốn phần lớn, ứng với năm mục... phần 1–3 lần lượt là mục 1, 2, 3; phần 4 gộp mục 4 và mục 5"; dòng 94 chỉ "mục 5 (Bước ra khỏi vòng luân hồi)". Không còn mâu thuẫn.

## Ghi chú phương pháp và hạn chế

- **Cách làm:** đọc toàn bộ ba file; đọc bản gộp `Kinh-Pham-Vong.md` để đối chiếu thân bài; đọc `nguon/sections/*.md` cho Pali/EN/NOTE; đọc `nguon/res_252fb4.txt`, `res_38e177.txt`, `res_acda34.html` cho các trích dẫn; kiểm tra liên kết bằng `curl` (HTTP status); kiểm tra 662 đoạn bằng cách so `keys_order` của `sc_pli.json` với danh sách thẻ `seg` trong bản gộp.
- **Slug:** dùng quy tắc GitHub: chữ thường, bỏ ký tự không phải chữ/số/`_`/`-`/dấu cách, đổi dấu cách thành `-`, **không gộp** các gạch nối liên tiếp. Đã kiểm lại toàn bộ 30 liên kết; 0 neo sai.
- **Giới hạn:** báo cáo không rà toàn bộ chất lượng dịch thuật từng câu (việc đó thuộc các báo cáo theo phần); chỉ tập trung vào các yêu cầu: số liệu, Mục lục/neo, thuật ngữ, mâu thuẫn nội bộ, chính tả/định dạng.
- **Phiên bản:** báo cáo tính theo bản chụp ở mục 0 (06:51:31–06:52:18). Trong lúc rà, các file đã đổi nhiều lần (06:34 → 06:52); bản cuối đã sửa toàn bộ lỗi nặng/trung bình. Nếu file tiếp tục đổi, các mục có số dòng cụ thể cần kiểm lại.
- **Không sửa file:** mọi thay đổi đề xuất chỉ nằm trong báo cáo này; không có file nào trong `ban-dich/` bị chỉnh.
