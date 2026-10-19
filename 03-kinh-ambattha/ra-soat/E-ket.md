# Rà soát E — mục 6–9

## Tóm tắt

Đã rà toàn bộ 4 tệp thuộc mục 6–9 (124 segment): `ban-dich/10-seers.md` (2.6.0–2.10.14), `ban-dich/11-two-marks.md` (2.11.0–2.15.5), `ban-dich/12-pokkarasati-visits.md` (2.16.0–2.21.7), `ban-dich/13-conclusion.md` (2.22.0–2.22.9). Đối chiếu từng đoạn với `nguon/api_dn3.json` (`root_text`), tham khảo bản EN của Sujato khi cần; kiểm tra riêng danh sách ẩn sĩ (2.8.1, 2.9.3, 2.10.1/4/7/10), hai tướng (2.11.4–2.12.6), cảnh Pokkharasāti nổi giận (2.15.2–2.15.5), công thức quy y (2.22.2–2.22.6) và dòng ghi cuối kinh (2.22.9).

- Marker: `10-seers` 35/35, `11-two-marks` 37/37, `12-pokkarasati-visits` 42/42, `13-conclusion` 10/10. Cả bốn tệp đều cho `==> ĐẠT`.
- Đã sửa trực tiếp 23 lỗi (bảng dưới).
- Không còn lỗi nặng về nghĩa sau khi đối chiếu Pali. Các điểm còn lại là văn phong và chú thích, ghi ở mục "Chất văn".
- Lưu ý: trong lúc tôi rà, `10-seers.md` và `11-two-marks.md` đã bị một tiến trình khác sửa (mtime 08:41–08:44). Báo cáo này dựa trên bản cuối cùng; nếu có ai sửa tiếp, cần chạy lại `kiem-tra-marker.py`.

## Lỗi nặng (phải sửa)

Không còn lỗi nặng về nghĩa. Hai lỗi nghĩa rõ ràng nhất đã được sửa trực tiếp và ghi ở bảng dưới: 2.10.8 ("đánh xe qua lại trên những cỗ xe" là vô lý) và 2.10.11 ("rào chắn đã dựng" sai nghĩa *okkhittapaligha*). Các điểm còn lại (câu dài 2.8.1, chú thích 2.8.1, sắc thái 2.15.2) là văn phong, không phải lỗi nghĩa.

| # | Tệp | Đoạn | Hiện tại | Vấn đề | Đề xuất |
|---|---|---|---|---|---|
| — | — | — | — | Không còn lỗi nặng về nghĩa | — |

## Lỗi nhẹ (đã sửa trực tiếp)

| # | Tệp | Đoạn | Đã sửa thành | Lý do |
|---|---|---|---|---|
| 1 | 10-seers.md | 2.6.1 | "bà-la-môn Pokkharasāti hưởng phần lộc do vua Pasenadi nước Kosala ban cho" | *dattika* là phần lộc/ân ban, không phải "đồ ăn"; *bhuñjati* là hưởng dụng |
| 2 | 10-seers.md | 2.8.1 | "những vị đã sáng tác thần chú và truyền bá thần chú" | Đồng nhất với 2.9.3 và 2.10.1/4/7/10; Pali có hai danh từ cùng bổ nghĩa |
| 3 | 10-seers.md | 2.8.1 | "Kassapa và Bhagu." (thay vì dấu hai chấm) | Câu đã trọn; dấu hai chấm treo lơ lửng trước 2.8.2 |
| 4 | 10-seers.md | 2.9.4 | "năm thứ dục lạc" | Chuẩn thuật ngữ của dự án (DN 1 và DN 2 đều dùng "năm thứ dục lạc"); "món" chỉ đồ ăn |
| 5 | 10-seers.md | 2.10.2 | "nhiều món ăn kèm" | *byañjana* là món ăn kèm/curry; "món ăn phụ" dễ hiểu là bữa phụ |
| 6 | 10-seers.md | 2.10.8 | "rong ruổi trên những cỗ xe do ngựa cái có đuôi tết lại kéo, dùng những cây gậy nhọn dài thúc vào những con vật kéo xe" | Sửa "đánh xe trên những cỗ xe" (vô lý), "bờm" thành "đuôi" (*kuttavāla*), "roi" thành "gậy thúc" (*patodalaṭṭhi*) |
| 7 | 10-seers.md | 2.10.11 | "then cửa đã cài" | *okkhittapaligha* là then/cửa đã hạ; "rào chắn đã dựng" đảo nghĩa |
| 8 | 11-two-marks.md | 2.11.6; 2.12.4 | "về tướng sinh thực khí ẩn kín trong bao và về tướng lưỡi rộng lớn" | Thống nhất với 12:66/78; bỏ "chiếc" (loại từ không hợp với lưỡi) |
| 9 | 11-two-marks.md | 2.12.5 | "thấy được tướng sinh thực khí ẩn kín trong bao của Ngài" | Thống nhất với 12:81 |
| 10 | 11-two-marks.md | 2.12.6 | "vuốt qua vuốt lại ... vuốt qua vuốt lại" | *anumasi paṭimasi* là vuốt/chạm qua lại; "liếm" sai nghĩa |
| 11 | 11-two-marks.md | 2.12.10 | "chúng con phải đi; chúng con còn nhiều việc" | Ambaṭṭha tự xưng "con" với Phật (2.14.3); thống nhất |
| 12 | 11-two-marks.md; 12-pokkarasati-visits.md | 11:2.14.11; 12:2.17.4/5/6/7 | "cuộc trò chuyện" | Thống nhất; "nói chuyện" thiếu trang trọng |
| 13 | 11-two-marks.md | 2.15.2; 2.15.4 | "Ôi chao, cái thứ học giả nhà ta! ..." | *aho vata* là thán từ; "Hay nhỉ/Hay chưa" mang nghĩa khen, sai sắc thái |
| 14 | 11-two-marks.md | 2.15.2; 2.15.4 | "một kẻ chỉ lo cái lợi của mình như thế" | *atthacara* là kẻ cầu lợi cho mình; bản cũ "lo điều ích lợi" mơ hồ, mất ý mỉa mai |
| 15 | 12-pokkarasati-visits.md | 2.18.2; 2.18.6 | "hầu hết ba mươi hai tướng ... chỉ trừ hai tướng" | Thống nhất với 11:18/30 (*yebhuyyena*) |
| 16 | 12-pokkarasati-visits.md | 2.18.9 | "thực hiện một phép thần thông như vậy" | Thống nhất với 11:39 (*iddhābhisaṅkhāra*) |
| 17 | 12-pokkarasati-visits.md | 2.18.10 | "vuốt qua vuốt lại ... vuốt qua vuốt lại" | Thống nhất với 2.12.6 |
| 18 | 12-pokkarasati-visits.md | 2.19.2 | "trọn vẹn" | Thống nhất với 11:50/89 (*paripuṇṇa*) |
| 19 | 12-pokkarasati-visits.md | 2.20.3 | "Rồi vào buổi sáng, Đức Thế Tôn đắp y ..." | Trật tự tự nhiên; không đổi nghĩa |
| 20 | 13-conclusion.md | 2.22.3 | "Thưa ngài Gotama, như người ta dựng lại cái đã bị lật úp ... Cũng vậy, thưa ngài Gotama, ngài Gotama đã làm sáng tỏ giáo pháp bằng nhiều cách." | Khớp công thức DN 2:99.3 (chỉ đổi đại từ theo §3); bản cũ lệch mẫu |
| 21 | 13-conclusion.md | 2.22.4 | Thêm "Thưa ngài Gotama," ở đầu câu | Pali có *bho gotama*; §3 yêu cầu "thưa ngài Gotama" |
| 22 | 13-conclusion.md | 2.22.5 | "ghi nhận" | Công thức DN 2 (*dhāretu*); "nhận biết" là nhận thức, không phải chấp nhận |
| 23 | 13-conclusion.md | 2.22.6 | Bỏ "thường" ("Như ngài Gotama đến thăm ...") | Pali không có; "thường đến thăm" thêm ý không có trong nguồn |

## Danh sách ẩn sĩ và thần chú (mục 6)

| Tên Pali | Bản dịch | Đúng/Sai | Ghi chú |
|---|---|---|---|
| 1. Aṭṭhaka | Aṭṭhaka | Đúng | Giữ nguyên dạng Pali; dấu ṭ đúng |
| 2. Vāmaka | Vāmaka | Đúng | ā dài đúng |
| 3. Vāmadeva | Vāmadeva | Đúng | |
| 4. Vessāmitta | Vessāmitta | Đúng | ā và tt đúng |
| 5. Yamataggi | Yamataggi | Đúng | Pali *yamataggi* (Phạn *Jamadagni*); bản EN của Sujato ghi "Yamadaggi" là lỗi chính tả của bản EN, không theo |
| 6. Aṅgīrasa | Aṅgīrasa | Đúng | ṅ và ī đúng |
| 7. Bhāradvāja | Bhāradvāja | Đúng | ā ở cả hai vị trí |
| 8. Vāseṭṭha | Vāseṭṭha | Đúng | ā và ṭṭ đúng |
| 9. Kassapa | Kassapa | Đúng | |
| 10. Bhagu | Bhagu | Đúng | |

- Thứ tự khớp đúng Pali 2.8.1, 2.9.3 và 2.10.1/4/7/10; không thiếu, không trùng, không đảo.
- Cả 10 tên đều giữ dạng Pali, không chuyển sang Hán-Việt, không dịch nghĩa.
- Thuật ngữ đi kèm đúng: *isayo* = "ẩn sĩ"; *mantā* = "thần chú"; *kattāro* = "sáng tác"; *pavattāro* = "truyền bá".
- Chú thích 2.8.1 giải thích đúng về *mantradraṣṭa* và việc Đức Thế Tôn dùng *kattāro*, nhưng quá dài và nặng (xem "Chất văn").

## Cảnh Pokkharasāti nổi giận (2.15.x)

Pali 2.15.2 và 2.15.4 lặp cùng một tràng: "aho vata re amhākaṁ, paṇḍitaka, ... bahussutaka, ... tevijjaka, evarūpena kira, bho, puriso atthacarakena kāyassa bhedā paraṁ maraṇā apāyaṁ duggatiṁ vinipātaṁ nirayaṁ upapajjeyya." Đây là ba tiếng thán từ mỉa mai, có hậu tố giảm nhẹ *-ka*, rồi lời nguyền tái sinh vào cõi dữ.

Bản hiện tại:

> "Ôi chao, cái thứ học giả nhà ta! Ôi chao, cái thứ uyên bác nhà ta! Ôi chao, cái thứ thông ba Vệ-đà nhà ta! Nghe đâu, một kẻ ăn ở như thế, một kẻ chỉ lo cái lợi của mình như thế, thì sau khi thân hoại mạng chung, sẽ sinh vào cõi dữ, đường ác, nơi đọa lạc, địa ngục!"

và 2.15.4:

> "... địa ngục!" — nói dứt lời, ông nổi giận, bực bội, giơ chân đá thanh niên Ambaṭṭha một cái.

Đánh giá:

- Cơn giận không bị mất: "cái thứ" là từ miệt thị, "chỉ lo cái lợi của mình" là lời kết tội, lời nguyền địa ngục giữ đủ bốn tầng *apāya, duggati, vinipāta, niraya*, và hành vi đá được dịch.
- *padasāyeva pavattesi*: "giơ chân đá ... một cái" dịch được ý "dùng chân"; "giơ chân" và "một cái" là thêm cho tự nhiên, không sai nghĩa.
- Hai chỗ còn nhẹ: "Ôi chao" (thán từ trung tính, có thể đọc như thương hại) và "bực bội" (so với *kupito anattamano* là "nổi giận, bất mãn"). Nếu muốn sắc hơn, có thể dùng "Ôi dào" cho tiếng thán từ và "phẫn nộ" cho *kupito*; nhưng "phẫn nộ" hơi quá so với *anattamano*. Bản hiện tại chấp nhận được.
- Lỗi cũ "Hay nhỉ" (bản 08:42) đọc như khen hoặc ngạc nhiên nhẹ, làm mất hẳn giọng mỉa mai; đã sửa thành "Ôi chao".
- Lỗi cũ "một kẻ lo điều ích lợi như thế" mơ hồ, có thể hiểu là kẻ theo đuổi điều tốt; đã sửa thành "một kẻ chỉ lo cái lợi của mình như thế".

Kết luận riêng: cảnh này đã đạt; không còn chỗ nào làm mất cơn giận.

## Công thức quy y so với DN 1 và DN 2

- DN 1 (`01-kinh-pham-vong/ban-dich/24-end-of-round.md`) không có công thức quy y ở cuối kinh; kết bằng dòng ghi in nghiêng và ghi chú của người dịch.
- DN 2 (`02-kinh-sa-mon-qua/ban-dich/32-conclusion.md`, 99.2–99.5) có công thức chuẩn.
- DN 3 2.22.2–2.22.5 hiện khớp DN 2 từng câu, chỉ đổi đại từ theo §3:

| DN 2 | DN 3 |
|---|---|
| "Thật vi diệu thay, bạch Đức Thế Tôn! Thật vi diệu thay, bạch Đức Thế Tôn!" | "Thật vi diệu thay, thưa ngài Gotama! Thật vi diệu thay, thưa ngài Gotama!" |
| "Bạch Đức Thế Tôn, như người ta dựng lại cái đã bị lật úp, mở ra cái đã bị che kín, chỉ đường cho người bị lạc, hay cầm ngọn đèn dầu trong bóng tối để những ai có mắt có thể nhìn thấy hình sắc. Cũng vậy, bạch Đức Thế Tôn, Đức Thế Tôn đã làm sáng tỏ giáo pháp bằng nhiều cách." | "Thưa ngài Gotama, như người ta dựng lại cái đã bị lật úp, mở ra cái đã bị che kín, chỉ đường cho người bị lạc, hay cầm ngọn đèn dầu trong bóng tối để những ai có mắt có thể nhìn thấy hình sắc. Cũng vậy, thưa ngài Gotama, ngài Gotama đã làm sáng tỏ giáo pháp bằng nhiều cách." |
| "Bạch Đức Thế Tôn, con xin quy y Đức Thế Tôn, quy y Pháp và quy y Tăng đoàn tỳ-kheo." | "Thưa ngài Gotama, chính con đây, cùng với con cái, vợ, tùy tùng và các quan, xin quy y ngài Gotama, quy y Pháp và quy y Tăng đoàn tỳ-kheo." |
| "Xin Đức Thế Tôn ghi nhận con là người cư sĩ đã quy y, từ hôm nay cho đến trọn đời." | "Xin ngài Gotama ghi nhận con là người cư sĩ đã quy y, từ hôm nay cho đến trọn đời." |

- Khác biệt duy nhất ở 2.22.4 là do Pali DN 3 thêm *saputto sabhariyo sapariso sāmacco* ("cùng với con cái, vợ, tùy tùng và các quan"); không phải lỗi.
- Cách xưng "thưa ngài Gotama" là đúng §3: Pokkharasāti là bà-la-môn, gọi Đức Thế Tôn là *bho gotama*, không dùng "bạch Đức Thế Tôn" như vua Ajātasattu trong DN 2.
- Dòng ghi 2.22.9 "Kinh Ambaṭṭha, bài thứ ba, đã hoàn thành." nằm ngoài ngoặc kép, không gán cho nhân vật nào, đúng vai trò lời ghi của người biên tập. DN 2 dùng "kết thúc tại đây"; nếu muốn đồng nhất, có thể đổi thành "Kinh Ambaṭṭha, bài thứ ba, kết thúc tại đây." — không bắt buộc.

## Chất văn — chỗ cần viết lại

1. **2.8.1 và 2.9.2–2.9.4, 2.10.1/4/7/10: câu quá dài.** Câu hỏi "Ông đã nghe ... nói thế nào — [danh sách ẩn sĩ] — ... phải chăng các vị ấy đã ...?" dài khoảng 100–110 từ và lặp 5 lần. Đây là chỗ khó đọc nhất của cả bốn tệp. Có thể tách bằng cách thêm một mệnh đề dẫn, ví dụ: "Ông đã nghe các bà-la-môn ... nói thế nào? Họ nói rằng những ẩn sĩ thời xưa ... đó là Aṭṭhaka ... Bhagu. Phải chăng các vị ấy đã ...?" Cách này thêm "Họ nói rằng" (không có trong Pali), nên cần tác giả cân nhắc giữa sát chữ và dễ đọc. Nếu ưu tiên sát chữ, giữ nguyên và chấp nhận câu dài.
2. **2.9.2 và 2.10.1/4/7/10: "nói thế nào".** *Kinti te sutaṁ ... bhāsamānānaṁ* là "ông đã nghe ... nói những gì", không phải "nói thế nào" (cách nói). Nên đổi thành "nói những gì" hoặc "theo lời ...". Hiện tại người đọc vẫn hiểu, nhưng sắc nghĩa chưa chuẩn.
3. **2.8.1: chú thích quá nặng.** Chú thích dài khoảng 180 từ trong một đoạn, gồm từ nguyên Dravida, phân biệt tên ẩn sĩ với tên dòng dõi, và cách hiểu *isi*. Nên tách thành 2 đoạn và bỏ bớt phần từ nguyên nếu muốn phổ thông hơn; phần cốt lõi (các vị "thấy" Vệ-đà, Đức Thế Tôn dùng *kattāro*) là đủ.
4. **2.14.1: lặp "Ambaṭṭha" bốn lần** trong một đoạn ("Ambaṭṭha xuống xe ... Ambaṭṭha đảnh lễ ... Khi Ambaṭṭha đã ngồi ... nói với Ambaṭṭha"). Có thể thay lần 2–3 bằng "ông ấy" hoặc "chàng" cho đỡ nặng.
5. **2.21.7: công thức nặng.** "Phàm cái gì có tính chất sinh khởi, tất cả cái ấy đều có tính chất chấm dứt." đúng nghĩa nhưng nặng. Có thể rút thành "Phàm cái gì sinh khởi, cái ấy đều chấm dứt." — vẫn giữ *samudayadhamma* / *nirodhadhamma*.
6. **2.11.6: "sinh thực khí".** Đã thống nhất với 12, nhưng đây là từ kỹ thuật, không phải ai cũng hiểu. Nếu muốn phổ thông, thêm gloss lần đầu: "tướng sinh thực khí (bộ phận sinh dục) ẩn kín trong bao"; hoặc dùng "chỗ kín" thống nhất cả 11 và 12.
7. **2.15.2: "Ôi chao".** Có thể mạnh hơn bằng "Ôi dào" (mỉa mai, khinh bỉ) nếu tác giả muốn sát giọng *aho vata re* hơn. "Bực bội" có thể đổi thành "bất mãn" nhưng không cần.
8. **2.7.6–2.7.7: câu rối.** "Phải chăng kẻ ấy nói lời của vua, bàn việc của vua như vậy, mà chỉ chừng ấy thôi, kẻ ấy có thành vua hay thành đại thần của vua không?" — bỏ "mà" hoặc "Phải chăng" sẽ gọn hơn: "Kẻ ấy nói lời của vua, bàn việc của vua như vậy — chỉ chừng ấy thôi, kẻ ấy có thành vua hay thành đại thần của vua không?"
9. **2.22.7: "hay khởi lòng tin".** *Cittaṁ vā pasādessanti* là "làm cho tâm hoan hỷ", không hẳn "khởi lòng tin". Có thể đổi thành "hay làm cho tâm hoan hỷ".

## Kết luận

**ĐẠT.**

- Cả bốn tệp đều qua kiểm tra marker (35/37/42/10).
- Đã đối chiếu toàn bộ 124 segment với Pali; các lỗi nghĩa rõ ràng đã được sửa (23 mục), trong đó có hai lỗi nặng về nghĩa ở 2.10.8 và 2.10.11.
- Danh sách 10 ẩn sĩ đúng thứ tự, đúng dạng Pali, không thiếu, không trùng; *Yamataggi* đúng (bản EN "Yamadaggi" là lỗi của EN).
- Công thức quy y 2.22.2–2.22.5 khớp DN 2, chỉ đổi đại từ theo §3; dòng ghi 2.22.9 đúng vai trò colophon, không phải lời thoại.
- Còn 9 gợi ý văn phong ở trên, không chặn xuất bản. Nếu có thêm một vòng biên tập, ưu tiên: (1) câu dài 2.8.1/2.10.x, (2) chú thích 2.8.1, (3) "nói thế nào" ở 2.9.2/2.10.x.
- Lưu ý lần cuối: `10-seers.md` và `11-two-marks.md` đã bị sửa đồng thời trong lúc rà; nếu có ai sửa tiếp sau báo cáo này, cần chạy lại marker và đối chiếu lại các mục đã sửa.
