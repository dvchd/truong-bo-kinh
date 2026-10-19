# Rà soát B — mục 2 và mục 3 (hai trang liệt kê)

## Tóm tắt

Phạm vi: `ban-dich/02-sonadanda.md` (dn4:4.0–5.22, 30 đoạn, 11 lý lẽ của
500 bà-la-môn) và `ban-dich/03-buddha.md` (dn4:6.0–6.47, 48 đoạn, hơn 20 lý lẽ
của Soṇadaṇḍa).

Đối chiếu từng đoạn với `PLI` trong `nguon/sections/02-sonadanda.md` và
`nguon/sections/03-buddha.md`; dùng thêm `api_dn4.json` (`root_text`,
`translation_text`, `comment_text`, `variant_text`) và các đoạn song song trong
`ban-dich/05-brahmin.md` (13.6–13.8, 14.7–14.8). EN của Sujato có chỗ rút gọn
bằng dấu ba chấm nên chỉ dùng để tham khảo, không dùng làm chuẩn.

Kết quả chính:

- **13 chỗ đã sửa trực tiếp.** Ba chỗ đáng kể nhất: 5.4 (mệnh đề nguyên nhân bị
  treo), 6.8 (thêm "bạc" không có trong Pali), 6.29 ("danh tiếng ấy" mâu thuẫn
  với "Trái lại"). Mười chỗ còn lại là thuật ngữ, công thức lặp, số ít/số nhiều
  và vài từ dịch thoát.
- **Điệp khúc:** mục 2 có đúng **12** câu đầy đủ; mục 3 có đúng **27** câu đầy
  đủ, cộng hai cặp tách đôi 6.5/6.6 và 6.41/6.42, thành **29** vế bắt đầu bằng
  "Chỉ vì lẽ ấy...". Câu chữ của 12 và 27 câu đầy đủ giống hệt nhau từng chữ.
- **Không còn lỗi nặng về nghĩa.** Các điểm hay bị hiểu sai (5.10, 5.14,
  5.15–5.16, 6.15, 6.24, 6.28, 6.43–6.44) đều đã kiểm tra; kết quả ở dưới.
- **Marker:** cả hai tệp `==> ĐẠT` (30/30 và 48/48). Không có ngoặc kép cong,
  không có `...` hay `…`, ngoặc kép cân bằng, không HTML, không "Đức Phật",
  "ngươi", "mày".

Kết luận: **ĐẠT**, với một bảo lưu nhỏ về cách diễn ý 5.21 (xem mục "Chỗ chưa
chắc").

## Lỗi đã sửa

| Đoạn | PLI (trích) | Câu cũ (trích) | Câu mới (trích) | Lý do |
|---|---|---|---|---|
| 5.4 | `Yampi ... yaso hāyissati ... imināpaṅgena na arahati ... upasaṅkamituṁ;` | "Vì danh tiếng của ngài Soṇadaṇḍa sẽ hao mòn, còn danh tiếng của sa-môn Gotama sẽ tăng lên**.**" | "Vì danh tiếng của ngài Soṇadaṇḍa sẽ hao mòn, còn danh tiếng của sa-môn Gotama sẽ tăng lên**,**" | Pali 5.4 là vế nguyên nhân, mệnh đề chính nằm ở 5.5. Dấu chấm cũ làm câu treo lơ lửng; đổi thành dấu phẩy để nối sang câu điệp khúc 5.5. |
| 5.10 | `sanighaṇḍukeṭubhānaṁ ... lokāyatamahāpurisalakkhaṇesu anavayo` | "cùng với từ vựng và nghi lễ ... khoa luận thuyết thế giới" | "cùng với từ vựng và nghi lễ tế tự ... khoa luận thuyết về thế giới" | `keṭubha` là nghi lễ tế tự; `lokāyata` là "khoa luận thuyết về thế giới". Đồng bộ với 13.6 và 14.7. |
| 5.11 | `abhirūpo ... paramāya vaṇṇapokkharatāya samannāgato brahmavaṇṇī brahmavacchasī akhuddāvakāso dassanāya` | "khả ái, đầy đủ sắc vóc tuyệt đẹp; ngài có sắc vóc và ánh sáng như Phạm thiên" | "dễ mến, sắc vóc thanh tú tột bậc, sắc diện như Phạm Thiên, hào quang như Phạm Thiên" | Pali có hai vế riêng `brahmavaṇṇī` (sắc diện như Phạm Thiên) và `brahmavacchasī` (hào quang như Phạm Thiên); bản cũ gộp thành "sắc vóc và ánh sáng". Đồng bộ với 6.11. |
| 5.12 | `sīlavā vuddhasīlī vuddhasīlena samannāgato` | "có giới hạnh, là người có giới hạnh đã trưởng thành, đầy đủ giới hạnh đã trưởng thành" | "có giới, giới đã trưởng thành, thành tựu giới đã trưởng thành" | `sīla` phải dịch là "giới"; đồng bộ với 13.8. Bản cũ dùng "giới hạnh" ba lần. |
| 6.2 | `mamapi suṇātha` | "xin hãy nghe tôi nói đây" | "xin hãy nghe cả tôi nói đây" | `api` = "cũng/cả"; bản cũ bỏ mất sắc thái "nghe cả tôi nữa". |
| 6.8 | `pahūtaṁ hiraññasuvaṇṇaṁ` | "rất nhiều vàng bạc" | "rất nhiều vàng" | `hirañña` và `suvaṇṇa` đều là vàng; "bạc" là thêm vào, không có trong Pali. |
| 6.11 | `akhuddāvakāso dassanāya` | "ai nhìn cũng không thấy chán" | "đáng để người ta chiêm ngưỡng" | Bản cũ thêm phản ứng của người nhìn; bản mới sát nghĩa "không tầm thường để nhìn", và đồng bộ với 5.11. |
| 6.12 | `sīlavā ariyasīlī kusalasīlī kusalasīlena samannāgato` | "có giới hạnh, giữ giới hạnh của bậc thánh, giữ giới hạnh thiện lành, và đầy đủ giới hạnh thiện lành" | "có giới, giữ giới của bậc thánh, giữ giới thiện lành, và đầy đủ giới thiện lành" | `sīla` phải dịch là "giới"; bốn lần "giới hạnh" là sai thuật ngữ. |
| 6.13 | `kalyāṇavāco ... vissaṭṭhāya anelagalāya atthassa viññāpaniyā` | "giọng nói thanh nhã, trôi chảy, không vấp váp, có khả năng làm rõ ý nghĩa" | "giọng nói tao nhã, rõ ràng, trôi chảy, không ngọng nghịu, đủ sức truyền đạt ý nghĩa" | Cùng công thức với 5.13; bản cũ bỏ `vissaṭṭhāya` ("rõ ràng, phóng khoáng") và dùng từ lỏng hơn. Nay 5.13 và 6.13 giống nhau từng chữ, chỉ khác chủ thể. |
| 6.19 | `tiroraṭṭhā tirojanapadā pañhaṁ pucchituṁ āgacchanti` | "đến hỏi sa-môn Gotama những câu hỏi" | "đến đặt câu hỏi cho sa-môn Gotama" | Pali dùng số ít `pañhaṁ`; bản cũ đổi thành số nhiều và lặp "hỏi ... câu hỏi". |
| 6.29 | `Atha kho anuttarāya vijjācaraṇasampadāya ... yaso samudāgato` | "Trái lại, sa-môn Gotama có được danh tiếng ấy, thưa quý vị, là nhờ..." | "Trái lại, danh tiếng của sa-môn Gotama, thưa quý vị, có được là nhờ..." | "Danh tiếng ấy" trỏ về danh tiếng của các vị sáng lập khác, mâu thuẫn với "Trái lại". Pali nói danh tiếng của chính Gotama khởi lên nhờ trí tuệ và hạnh tu viên mãn. |
| 6.43 | `ettake ... vaṇṇe pariyāpuṇāmi` | "tôi chỉ nhớ được đến chừng ấy lời ca ngợi" | "tôi chỉ học thuộc được đến chừng ấy lời ca ngợi" | `pariyāpuṇāmi` là "học thuộc, nắm được", không chỉ "nhớ"; Sujato dịch "memorized". |
| 6.44 | `aparimāṇavaṇṇo hi so bhavaṁ gotamo` | "Vì lời ca ngợi ngài Gotama là vô hạn." | "Vì ngài Gotama có lời ca ngợi vô hạn." | Pali lấy Gotama làm chủ thể ("Ngài là bậc có lời ca ngợi vô hạn"), không lấy "lời ca ngợi" làm chủ thể. |

## Điệp khúc

Câu cố định của mục 2:

> Chỉ vì lẽ ấy, ngài Soṇadaṇḍa cũng không thích hợp để đến thăm sa-môn Gotama; mà chính sa-môn Gotama mới thích hợp để đến thăm ngài Soṇadaṇḍa.

Câu cố định của mục 3:

> Chỉ vì lẽ ấy, ngài Gotama cũng không thích hợp để đến thăm chúng tôi; mà chính chúng tôi mới thích hợp để đến thăm ngài Gotama.

| Mục | Các đoạn có câu đầy đủ | Số câu đầy đủ | Số lần "Chỉ vì lẽ ấy..." | Ghi chú |
|---|---|---:|---:|---|
| 2 | 5.5, 5.8, 5.9, 5.10, 5.11, 5.12, 5.13, 5.14, 5.16, 5.17, 5.18, 5.22 | **12** | **12** | 5.4/5.5, 5.7/5.8, 5.21/5.22 là các cặp Pali tách vế. Bản dịch dồn câu đầy đủ vào vế sau, nên vẫn đủ 12 đơn vị. 5.21 diễn ý nửa đầu (xem bảo lưu). |
| 3 | 6.7–6.20, 6.22–6.27, 6.29–6.35 | **27** | **29** | 6.5/6.6 và 6.41/6.42 tách đôi đúng Pali; 27 + 2 = 29 vế. |

Đã đếm lại bằng lệnh tìm chuỗi nguyên văn, không đếm bằng mắt:

- `02-sonadanda.md`: 12 câu đầy đủ, 12 dòng bắt đầu "Chỉ vì lẽ ấy, ngài Soṇadaṇḍa".
- `03-buddha.md`: 27 câu đầy đủ, 29 dòng bắt đầu "Chỉ vì lẽ ấy, ngài Gotama"
  (27 câu đầy đủ + 6.5 + 6.41).

Không có câu nào sai một chữ trong 12 và 27 câu đầy đủ.

## Các điểm trọng tâm

### 5.10 và 13.6 — chương trình học bà-la-môn

Pali: `sanighaṇḍukeṭubhānaṁ sākkharappabhedānaṁ itihāsapañcamānaṁ padako
veyyākaraṇo`. Bản dịch hiện tại: "cùng với từ vựng và nghi lễ tế tự, với ngữ âm
và cách phân loại từ, với bộ sử thi là thứ năm; ngài thuộc từng chữ và thông
thạo ngữ pháp". Đúng các thành phần: `nighaṇḍu` (từ vựng), `keṭubha` (nghi lễ tế
tự), `sākkhara` (ngữ âm), `ppabheda` (phân loại từ), `itihāsa` là thứ năm,
`padako` (thuộc từng chữ), `veyyākaraṇa` (ngữ pháp). Đã đồng bộ "nghi lễ tế tự"
và "khoa luận thuyết về thế giới" với 13.6/14.7.

### 5.14 — Soṇadaṇḍa dạy 300 thanh niên

Pali: `bahūnaṁ ācariyapācariyo tīṇi māṇavakasatāni mante vāceti`. Bản dịch:
"thầy của nhiều bậc thầy, dạy ba trăm thanh niên tụng đọc thần chú". Đúng:
`ācariyapācariyo` là "thầy của các thầy", `tīṇi māṇavakasatāni` là ba trăm thanh
niên, `mante vāceti` là dạy tụng thần chú. Không có lỗi.

### 5.15–5.16 — hai vế đối lập

Pali 5.15: `jiṇṇo vuddho mahallako addhagato vayoanuppatto` (già, lớn tuổi, cao
niên, đã đi hết chặng đường, đã đến tuổi cuối đời). Pali 5.16: `taruṇo ceva
taruṇapabbajito ca` (trẻ, mới xuất gia). Bản dịch giữ đúng hai vế và đặt dấu
chấm phẩy cuối 5.15 để nối sang 5.16. `taruṇapabbajito` dịch "mới xuất gia" là
đúng (Sujato: "newly gone forth"), không phải "xuất gia khi còn trẻ" theo nghĩa
đã lâu.

### 6.15 — `khīṇakāmarāgo vigatacāpallo`

Bản dịch: "đã đoạn tận lòng tham dục, không còn nhẹ dạ phù phiếm". `khīṇakāmarāga`
= tham dục đã cạn; `vigatacāpalla` = không còn sự nhẹ dạ, phù phiếm, thiếu
nghiêm túc. Đúng nghĩa, không cần sửa.

### 6.24 — `ehisvāgatavādī ... pubbabhāsī`

Bản dịch: "nói lời chào đón khách, thân thiện, vui vẻ, không cau có, nét mặt cởi
mở, và là người mở lời trước". Đủ sáu thành phần: `ehi-svāgata-vādī`, `sakhila`,
`sammodaka`, `abbhākuṭika`, `uttānamukha`, `pubbabhāsī`. Đúng.

### 6.28 — `titthakara`

Bản dịch: "bậc đứng đầu trong số những người sáng lập các giáo phái khác nhau",
chú thích giải `titthakara` là "người tạo chỗ lội qua sông", tức người sáng lập
tôn giáo. Đúng. Chỗ "các sa-môn và bà-la-môn khác" thêm chữ "khác" so với
`etesaṁ`, nhưng trong ngữ cảnh là các vị sáng lập vừa nói tới, nên chấp nhận.

### 6.43–6.44 — `ettakavaṇṇo` / `aparimāṇavaṇṇo`

`ettakavaṇṇo` = "bậc chỉ đáng ca ngợi chừng ấy"; `aparimāṇavaṇṇo` = "bậc có lời
ca ngợi vô hạn". Bản dịch hiện tại: "ngài Gotama không chỉ đáng ca ngợi bấy
nhiêu" và "ngài Gotama có lời ca ngợi vô hạn". Đúng hướng, không dịch `vaṇṇa`
thành "sắc vóc" ở đây.

### Thuật ngữ

- `vaṇṇa` = **sắc vóc** ở 5.11, 6.11; = **lời ca ngợi** ở 6.43–6.44 (đúng ngữ cảnh).
- `manta` = **thần chú** (5.10, 5.14).
- `jāti` = **dòng dõi** (5.6, 5.7, 6.4–6.6, 6.17).
- `sīla` = **giới** (5.12, 6.12); không còn "giới hạnh" trong hai tệp.
- `vijjācaraṇa` = **trí tuệ và hạnh tu** (6.22, 6.29).
- `aṅga` không xuất hiện trong hai tệp này (chỉ có ở mục 5), nên không có gì để đối chiếu.

### Xưng hô

- 500 bà-la-môn gọi Soṇadaṇḍa: "thưa ngài Soṇadaṇḍa" (4.5, 5.1).
- Soṇadaṇḍa gọi 500 vị: "thưa quý vị" (4.6, 6.2, 6.43, 6.47).
- Soṇadaṇḍa nói về Đức Thế Tôn: "ngài Gotama" (không dùng "ông ta", "hắn").
- Người kể chuyện: "Đức Thế Tôn" ở tiêu đề 3.0; không có "Đức Phật".
- Không có "ngươi", "mày", "thằng".

### Hình thức

- Không có ngoặc kép cong.
- Không có `...` hay `…` ngoài chú thích (thực tế cả hai tệp đều không có).
- Ngoặc kép cân bằng: 02 có 8 dấu, 03 có 14 dấu; các cặp mở/đóng đúng đoạn.
- Không có HTML.
- Chú thích dài nhất 3 câu (5.11); các chú thích khác 1–2 câu.

## Chỗ chưa chắc / không sửa

1. **5.21** — Pali là nửa đầu của điệp khúc: `Imināpaṅgena na arahati ...`.
   Bản dịch hiện tại diễn ý: "Vì lẽ ấy, việc ngài Soṇadaṇḍa đến thăm sa-môn
   Gotama là không thích hợp." Nghĩa không sai, nhưng không phải nguyên văn nửa
   đầu. Nếu tách đúng Pali thành 5.21 (nửa đầu) và 5.22 (nửa sau) thì số câu đầy
   đủ của mục 2 sẽ còn 11, trái với yêu cầu 12 câu đầy đủ. Tôi giữ 5.21 làm câu
   dẫn diễn ý và 5.22 làm câu đầy đủ, để bảo toàn đúng 12 lần. Đây là chỗ đánh
   đổi có chủ ý, không phải lỗi dịch nghĩa.
2. **5.7 và 5.20** — `Yampi` có sắc thái "và vì", bản dịch dùng "Và" rồi xuống
   câu điệp khúc. Không sai nghĩa, nhưng mất một chút liên kết nguyên nhân. Nếu
   thêm "vì" thì phải thêm dấu phẩy cuối đoạn, làm tăng số đoạn kết bằng dấu
   phẩy; tôi để nguyên.
3. **5.19** — `rājabhogga` (lãnh địa/đất vua hưởng dụng), `rājadāya` (vua ban),
   `brahmadeyya` (ân tứ cho bà-la-môn) bị gộp thành ba lần "vua ban". Trong ngữ
   cảnh vẫn đúng (đất do vua ban), nhưng mất sự phân biệt ba hợp từ. Không sửa
   vì không phải lỗi nghĩa và bản EN của Sujato cũng gộp tương tự.
4. **5.19 "cỏ khô"** — Pali `tiṇa` là "cỏ"; EN của Sujato dùng "hay". "Cỏ khô"
   theo EN, chấp nhận được.
5. **6.9** — `bhadrena yobbanena` có "tuổi thanh xuân tốt đẹp"; bản dịch "đang
   độ thanh xuân" không dịch riêng `bhadra`. Sắc thái tích cực đã nằm trong
   "thanh xuân", không đáng sửa.
6. **6.16** — "khi đối xử với cộng đồng bà-la-môn" là cách diễn giải dative
   `brahmaññāya pajāya`; sát nghĩa hơn là "đối với cộng đồng bà-la-môn". Không
   sai, nhưng có thêm động từ "đối xử".
7. **6.25 chú thích** — "giới Sát-đế-lỵ" dùng "giới" theo nghĩa giai cấp, không
   phải `sīla`. Đây là cách nói quen thuộc, nhưng trong dự án đang dùng "giới"
   cho giới luật, nên có thể đổi thành "hạng Sát-đế-lỵ" nếu muốn tránh nhập
   nhằng. Tôi không sửa vì đây là chú thích và "giới Sát-đế-lỵ" là thuật ngữ
   chuẩn.
8. **13.7 (ngoài phạm vi)** — cùng công thức `akhuddāvakāso dassanāya` nhưng
   đang dịch "nhìn vào không thấy chỗ nào khiếm khuyết", khác 5.11/6.11. Tôi đã
   đồng bộ 5.11 với 6.11, nhưng không sửa 13.7 vì ngoài hai tệp được giao.
9. **6.30–6.32** — `saputto sabhariyo` là "cùng các con trai và vợ"; bản dịch
   "cùng vợ con" là cách nói tự nhiên, có đảo thứ tự và gộp "con trai" thành
   "con". Không sai nghĩa.
10. **6.20, 6.30–6.32** — "đã đến quy y ... xin nương tựa trọn đời" hơi trùng
    (`saraṇaṁ gata` chỉ là "đã quy y, nương tựa"), nhưng là công thức lặp và
    giữ được nhịp. Không sửa.

## Kết luận

**ĐẠT.** Hai tệp bám sát Pali, không còn lỗi nặng về nghĩa; 13 chỗ đã sửa trực
tiếp, trong đó 5.4, 6.8 và 6.29 là đáng kể nhất. Điệp khúc đúng 12 câu đầy đủ ở
mục 2 và 27 câu đầy đủ + 2 cặp tách đôi ở mục 3; câu chữ của các câu đầy đủ
giống hệt nhau. Marker và các kiểm tra hình thức đều đạt.

Bảo lưu duy nhất: 5.21 là câu diễn ý nửa đầu điệp khúc, không phải nguyên văn;
nếu yêu cầu "từng đoạn khớp từng chữ" được đặt lên trên yêu cầu "đúng 12 câu
đầy đủ", thì phải tách 5.21/5.22 và chấp nhận 11 câu đầy đủ. Tôi giữ phương án
12 câu đầy đủ theo đúng đề bài.

## Kiểm tra marker

```
python3 kiem-tra-marker.py ban-dich/02-sonadanda.md
   marker trong bài dịch : 30
   segment trong nguồn   : 30
   số từ nội dung        : 1126
   ==> ĐẠT

python3 kiem-tra-marker.py ban-dich/03-buddha.md
   marker trong bài dịch : 48
   segment trong nguồn   : 48
   số từ nội dung        : 2198
   ==> ĐẠT
```
