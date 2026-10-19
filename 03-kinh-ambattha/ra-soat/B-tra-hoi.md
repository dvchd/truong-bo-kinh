# Rà soát B — mục 2.1–2.4 (cuộc tra hỏi)

## Tóm tắt

Phạm vi: `ban-dich/03-primitives-1.md` (dn3:1.10.0–1.12.9, 15 đoạn),
`ban-dich/04-primitives-2-3.md` (dn3:1.13.0–1.14.9, 17 đoạn) và
`ban-dich/05-slavegirl.md` (dn3:1.15.0–1.21.11, 62 đoạn). Tổng cộng 94 đoạn.
Đối chiếu `root_text` (PLI), `translation_text` (EN của Bhikkhu Sujato) và
`comment_text` (NOTE) trong `nguon/api_dn3.json`; đọc thêm các tệp nguồn trong
`nguon/sections/`. Kiểm tra theo thứ tự: nghĩa so với Pali, nhịp điệp khúc, xưng hô,
câu công thức §5, chất văn, chú thích.

Kết quả chính:

- **Không có lỗi nặng còn tồn đọng.** Ba nghi vấn lớn đã kiểm tra và đều đạt:
  (1) nhịp lặp `ambaṭṭho māṇavo` ở 1.17.3, 1.18.3, 1.18.5–6 và 1.19.1 được giữ đúng
  6/7/7/7 lần, khớp Pali; (2) `saṁvāsaṁ kappesuṁ` ở 1.15.11 và 1.15.15 được dịch là
  “ăn nằm”, không làm nhẹ chuyện loạn luân; (3) `bandhupādāpacca` ở 1.10.3 có chú thích
  giải thích Phạm Thiên và bốn giai cấp, nên lời miệt thị thứ tư không còn vô nghĩa.
- **Các lỗi nhẹ đã sửa trực tiếp** trong ba tệp: bỏ “mới” ở 1.10.2; đổi “chẳng thích
  đáng” thành “chẳng vừa lòng” ở 1.12.8, 1.13.5, 1.14.8; sửa chú thích 1.10.3 (“di cư”
  thay vì “tràn vào”), 1.17.2 (“học vấn” thay vì “hạnh kiểm”), 1.21.1 (“bảo vệ Chánh
  pháp” thay vì “hộ pháp của Pháp”); cùng các chỗ đã sửa trước đó (danh sách dưới).
- **Bốn chú thích còn quá dài** so với người đọc phổ thông: 1.12.7, 1.16.1, 1.20.3,
  1.21.1. Đây là gợi ý biên tập, không phải lỗi nghĩa. Chú thích 1.15.4 đã được rút ngắn, nên không còn các dẫn chứng
  Mahābhārata/Arrian/Manusmṛti dài trong bản dịch; nếu khôi phục, phải dùng đúng
  Manusmṛti 10.8 và Arrian quyển VI chương 15.
- **2.4 có ba lần hỏi nhưng chỉ hai lần im lặng**, không phải ba lần im lặng. Hai lần
  hỏi đầu đầy đủ (1.20.4–5, 1.20.7–8), mỗi lần tiếp theo là một lần im lặng (1.20.6,
  1.20.9). Đến lần thứ ba, Đức Thế Tôn ra tối hậu thư trước (1.20.10–12), Vajirapāṇī
  hiện (1.21.1–3), Ambaṭṭha xin nhắc lại (1.21.4–6), rồi Đức Thế Tôn mới lặp lại đầy
  đủ (1.21.7–8) và Ambaṭṭha đáp (1.21.9–11). Vì thế không có lần im lặng thứ ba. Bản
  dịch giữ đúng thứ tự và đúng người nói. Cách đếm “ba lần im lặng” trong
  `00-gioi-thieu.md` là sai; báo cáo A đã bắt lỗi này, tôi chỉ nhắc lại vì nó ảnh
  hưởng đến cách đọc nhịp 2.4.
- **Kiểm tra marker:** cả ba tệp đều `==> ĐẠT` (15/15, 17/17, 62/62). Không có “Đức
  Phật”, “ngươi”, “mày”, “thằng”, ngoặc kép cong, `...` hay `…` trong ba tệp.

Kết luận tạm: **ĐẠT**. Bản dịch bám Pali, giữ đúng nhịp điệp khúc, đúng ngôi xưng hô
và đúng các câu công thức; các đề xuất còn lại chỉ là biên tập chú thích và vài chỗ
dùng từ.

## Lỗi nặng (phải sửa)

Không có lỗi nặng còn tồn đọng. Ba nghi vấn được kiểm tra kỹ:

1. **Nhịp lặp `ambaṭṭho māṇavo`** (1.17.3, 1.18.3, 1.18.5–6, 1.19.1). Bản dịch lặp
   “Ambaṭṭha” đúng số lần của Pali: 6/7/7/7. Đây là chỗ dễ mất nhịp nhất của cả mục,
   vì mỗi vị ngữ trong danh sách bị đập xuống bằng một lần gọi tên; bản dịch đã giữ
   được nhịp búa gõ ấy. Bảng đối chiếu ở mục Nhịp điệu.
2. **`saṁvāsaṁ kappesuṁ`** (1.15.11, 1.15.15). Bản dịch dùng “ăn nằm”, không dùng
   “chung sống”; đủ mạnh để người đọc thấy chuyện loạn luân, đúng như EN “slept with”
   và chú thích “loạn luân”. Không cần sửa.
3. **`bandhupādāpacca`** (1.10.3). Có chú thích ngay sau đoạn: “Sinh ra từ gót chân
   của bà con chúng ta” là nghĩa đen; bốn giai cấp sinh ra từ bốn phần thân của Phạm
   Thiên; “bà con” là Phạm Thiên, vị tổ chung. Lời miệt thị thứ tư không còn là cụm
   vô nghĩa. Không cần thêm chú thích mới.

Vì ba chỗ trên đều đạt, không có hàng nào trong bảng “phải sửa”. Các vấn đề còn lại
đều là nhẹ hoặc tùy chọn biên tập.

## Lỗi nhẹ (đã sửa trực tiếp)

| # | Tệp | Đoạn | Đã sửa thành | Lý do |
|---|---|---|---|---|
| 1 | 03-primitives-1.md | dn3:1.10.2 | “Thưa ngài Gotama, khi đang đi thì bà-la-môn xứng đáng nói chuyện với bà-la-môn đang đi…” (bỏ “mới” ở cả bốn vế) | `arahati` là “xứng đáng, phải lẽ”, không phải “chỉ khi… mới”. “Mới” biến quy tắc lễ nghi thành điều kiện. |
| 2 | 03-primitives-1.md | dn3:1.10.3 (chú thích) | “…dòng người Ấn-Âu da sáng di cư vào Ấn Độ từ phương bắc.” | “Tràn vào” mang nghĩa xâm lược, không trung tính; “di cư” sát nghĩa hơn. |
| 3 | 03-primitives-1.md | dn3:1.11.1 | “Ông hãy chú tâm cho kỹ vào chính mục đích ấy.” | “Khéo chú tâm vào chính mục đích mà mình đã đến đây” là calque của `yadattāya upasaṅkamitvā`; vừa lặp vừa tối. |
| 4 | 03-primitives-1.md | dn3:1.11.2; 1.12.1 | “chưa tu tập xong” (thay cho “chưa tu tập”) | `vusita` là đã hoàn tất; thiếu “xong” thì cách chơi chữ `vusitamānī` (“tưởng mình đã tu tập xong”) không còn. |
| 5 | 03-primitives-1.md | dn3:1.12.1 | “…bèn chửi rủa chính Đức Thế Tôn, khinh bỉ chính Đức Thế Tôn và mắng nhiếc chính Đức Thế Tôn:” | Pali lặp `bhagavantaṁyeva` ba lần; bản cũ nén còn một, làm mất nhịp ba bước. |
| 6 | 03-primitives-1.md | dn3:1.12.2 | “…thanh niên Ambaṭṭha nói với Đức Thế Tôn như vậy, rồi nói tiếp:” | Pali dùng `…ti bhagavantaṁ etadavoca:` để dẫn lời nói kéo dài đến 1.12.8; thẻ “như vậy” đóng lời sớm, người đọc tưởng 1.12.3 là lời mới. |
| 7 | 03-primitives-1.md | dn3:1.12.7; 1.12.9 | “lại không kính trọng bà-la-môn…”; “lần thứ nhất” | 1.12.8, 1.13.5, 1.14.8 đều có “lại”; “lần thứ nhất” song song với “lần thứ hai/ba” ở hai câu kết sau. |
| 8 | 03-primitives-1.md; 04-primitives-2-3.md | dn3:1.12.8; 1.13.5; 1.14.8 | “điều ấy thật chẳng vừa lòng, thật chẳng phải lẽ” | `nacchannaṁ` là “không vừa lòng”, `nappatirūpaṁ` là “không phải lẽ”; bản cũ dùng “chẳng thích đáng” cho cả hai, làm mất vế đầu. |
| 9 | 04-primitives-2-3.md | dn3:1.13.0; 1.14.0 | “### 2.2. Lần thứ hai dùng chữ "tiện dân"”; “### 2.3. Lần thứ ba dùng chữ "tiện dân"” | Hai tiêu đề cũ chỉ là “Lần thứ hai/ba”, không nói rõ làm gì; tiêu đề 2.1 đã có “dùng chữ "tiện dân"”. |
| 10 | 04-primitives-2-3.md | dn3:1.13.3; 1.13.4 | “nhà họp chung”; “…cũng chẳng ai mời tôi ngồi vào một chỗ nào.” | “Nhà hội” là Hán-Việt cổ; `santhāgāra` là nhà họp chung. Bản cũ “không ai mời tôi một chỗ ngồi nào” vừa lúng túng vừa mất `api` (“even”). |
| 11 | 04-primitives-2-3.md | dn3:1.14.1; 1.14.2 | “…trong chính tổ của mình.”; “Ông là bậc đáng kính, không nên nổi nóng vì một chuyện nhỏ nhặt như vậy.” | `sake` là “của chính mình”; “chính… của mình” giữ tiếng vang `saka`/Sakya. §3 quy định Đức Thế Tôn gọi Ambaṭṭha là “ông”; bản cũ “Bậc đáng kính như Ambaṭṭha” vừa ngôi thứ ba vừa nghe mỉa. |
| 12 | 05-slavegirl.md | dn3:1.15.5 | “Thưa ngài Gotama, tôi thuộc dòng Kaṇhāyana.” | `kaṇhāyano` là tên dòng, không phải tên người; “tôi là người Kaṇhāyana” dễ bị hiểu là “người tên Kaṇhāyana”. |
| 13 | 05-slavegirl.md | dn3:1.15.6; 1.16.10 | “…khi nhớ lại tên họ và dòng dõi bên cha mẹ ông từ thuở xưa…” | `anussarato` là tuyệt đối phân từ (“khi nhớ lại”), không phải mệnh lệnh; “bên cha mẹ” làm rõ `mātāpettikaṁ`. |
| 14 | 05-slavegirl.md | dn3:1.15.6 (chú thích) | “…nghĩa là dòng Sakya sinh ra từ các bậc chủ nhân ấy, chứ không phải chính họ là chủ.” | Câu cũ “nghĩa không phải là dòng Sakya làm chủ, mà là họ sinh ra từ các bậc chủ nhân ấy” tối nghĩa. |
| 15 | 05-slavegirl.md | dn3:1.15.8 | “…con trai của bà chánh hậu mà mình yêu quý…” (bỏ “nhất”) | `piyā manāpā` là “yêu quý, dễ mến”, không có so sánh nhất; “nhất” là thêm, dù EN của Sujato cũng dịch “most beloved”. |
| 16 | 05-slavegirl.md | dn3:1.15.16 | “Rồi vua Okkāka, này Ambaṭṭha, thốt lên lời cảm thán:” | “Buột miệng thốt lên lời cảm khái” pha hai giọng; `udāna` là lời cảm thán/thốt lên. |
| 17 | 05-slavegirl.md | dn3:1.15.18; 1.16.9 | “vua Okkāka” (thay cho “vị ấy”); “Kaṇha” (thay cho “vị ấy”) | Hai chỗ “vị ấy” mơ hồ: ở 1.15.18 là Okkāka, ở 1.16.9 là Kaṇha. |
| 18 | 05-slavegirl.md | dn3:1.16.4 | “…hãy cứu con khỏi thứ ô uế này…” | `parimocetha` là “giải thoát/cứu khỏi”, không phải “rửa sạch”; giữ ba động từ rửa/tắm/cứu. |
| 19 | 05-slavegirl.md | dn3:1.16.6 | “…nhận ra đó là 'kẻ đen'.” | Pali có `‘kaṇhā’ti`; dấu ngoặc cho thấy “kẻ đen” là nhãn được gán, không phải lời miêu tả trung tính. |
| 20 | 05-slavegirl.md | dn3:1.17.2 (chú thích) | “…quan tâm đến học vấn và trí tuệ hơn là xuất thân.” | Chính văn 1.17.2–1.17.3 ca ngợi dòng dõi, học vấn, ăn nói, thông minh — không phải hạnh kiểm. |
| 21 | 05-slavegirl.md | dn3:1.20.2; 1.20.7; 1.20.12; 1.21.2 | “đang đặt ra cho ông”; “Lần thứ hai, Đức Thế Tôn nói với thanh niên Ambaṭṭha:”; “đến ba lần” | `āgacchati` là “nảy ra/đặt ra”, không phải “đến với ông”; `etadavoca` là “nói”, không phải “hỏi”; `yāvatatiyakaṁ` là “đến ba lần”. |
| 22 | 05-slavegirl.md | dn3:1.20.5; 1.20.8; 1.21.8 | “Ông đã nghe các bà-la-môn tuổi cao, lão thành, những bậc thầy của các bậc thầy nói lại thế nào: dòng Kaṇhāyana bắt nguồn từ đâu…” | Câu cũ dồn phần dẫn lên đầu (“Theo những gì ông đã nghe…”) rồi mới hỏi; dấu hai chấm tách phần dẫn khỏi nội dung hỏi, dễ đọc hơn mà không đổi nghĩa. |
| 23 | 05-slavegirl.md | dn3:1.21.1 (chú thích) | “…một vị Bồ-tát dữ dằn, bảo vệ Chánh pháp.” | “Hộ pháp của Pháp” lặp nghĩa; “bảo vệ Chánh pháp” gọn hơn. |
| 24 | 05-slavegirl.md | dn3:1.21.5 | “Thưa ngài Gotama — ngài vừa nói gì vậy?” | Người kể vừa nói Ambaṭṭha “hoảng sợ, kinh hãi, lông tóc dựng ngược”; lời thoại cũ “Ngài Gotama vừa nói gì vậy?” đều đều. Thêm “thưa” và chỗ ngắt để giọng khúm núm hơn, không thêm nội dung. |

## Nhịp điệu ba lần

Mục 2.1–2.4 không được xây bằng bốn câu mở giống nhau. Nó được xây bằng một **khung**:

1. Đức Thế Tôn ra đòn (nhận xét, câu hỏi, hoặc ví dụ).
2. Ambaṭṭha đáp lại bằng một lần miệt thị “tiện dân” (riêng 2.4 thì im lặng).
3. Một công thức năm động từ giống hệt nhau (2.1–2.3).
4. Một câu kết giống hệt nhau, chỉ khác số thứ tự (2.1–2.3).

Sang 2.4, khung đổi hẳn: Đức Thế Tôn không nói về “tiện dân” nữa mà hỏi dòng dõi;
Ambaṭṭha không miệt thị nữa mà im lặng; và cái kết không phải lời kết tội dòng Sakya
mà là lời thú nhận nguồn gốc của chính Ambaṭṭha. Vì thế “ba lần” ở đây là ba lần
**lảng tránh bằng miệt thị**, không phải ba lần im lặng. Cái được gọi là “ba lần im
lặng” chỉ nằm trong 2.4, và thực ra chỉ có hai lần.

| Lần | Câu mở | Câu kết | Câu lặp giữa | Nhịp có trùng không? |
|---|---|---|---|---|
| 2.1 (1.10–1.12) | Ambaṭṭha: “Không phải vậy, thưa ngài Gotama.” (1.10.1) | “Thế là thanh niên Ambaṭṭha lần thứ nhất ném chữ "tiện dân" vào dòng Sakya.” (1.12.9) | Năm động từ ở 1.12.7 và 1.12.8 | Kết đúng; giữa đúng. Mở khác 2.2/2.3 là có chủ ý: đây là lời Ambaṭṭha cắt ngang, không phải lời Phật. |
| 2.2 (1.13) | Đức Thế Tôn: “Này Ambaṭṭha, dòng Sakya đã làm gì mất lòng ông?” (1.13.1) | “…lần thứ hai ném chữ "tiện dân" vào dòng Sakya.” (1.13.6) | Năm động từ ở 1.13.5 | Kết đúng, song song với 2.1. Mở khác 2.1 là có chủ ý: đây là câu hỏi của Phật. |
| 2.3 (1.14) | Đức Thế Tôn: “Này Ambaṭṭha, đến con chim cút nhỏ cũng được tự do hót trong chính tổ của mình.” (1.14.1) | “…lần thứ ba ném chữ "tiện dân" vào dòng Sakya.” (1.14.9) | Năm động từ ở 1.14.8 | Kết đúng, song song với 2.1/2.2. Mở khác là có chủ ý: đây là ví dụ của Phật, và là đòn nặng nhất trong ba lần. |
| 2.4 (1.15–1.21) | “Rồi Đức Thế Tôn nghĩ như thế này: ‘Thanh niên Ambaṭṭha này lấy chữ "tiện dân" mà mạt sát dòng Sakya quá mức. Chi bằng ta hỏi xem ông ta thuộc dòng dõi nào.’” (1.15.1–2) | “và vị ấy là vị tổ đầu tiên của dòng Kaṇhāyana.” (1.21.11) | Câu hỏi dòng dõi lặp ba lần: 1.20.4–5, 1.20.7–8, 1.21.7–8 | Kết khác hẳn 2.1–2.3 là có chủ ý: cái bẫy đã đóng. Nhịp trong 2.4 là nhịp hỏi–im–hỏi–im–đe–hỏi lại–đáp, không phải nhịp miệt thị. |

Phân tích:

- **Ba câu kết song song.** 1.12.9, 1.13.6, 1.14.9 giống nhau từng chữ, chỉ khác
  “thứ nhất / thứ hai / thứ ba”. Đây là điệp khúc rõ nhất của mục 2.1–2.3.
- **Công thức năm động từ song song.** 1.12.8, 1.13.5, 1.14.8 giống hệt: “dòng Sakya
  là tiện dân, và vẫn cứ là tiện dân, lại không kính trọng bà-la-môn, không tôn trọng
  bà-la-môn, không nể vì bà-la-môn, không cung kính bà-la-môn, không thờ phụng
  bà-la-môn.” 1.12.7 là câu gốc, đứng sau lời dẫn trực tiếp, nên bắt đầu bằng “Họ”
  thay vì “dòng Sakya” — khác biệt này là tất yếu, không phải lỗi.
- **Câu mở khác nhau là đúng.** 2.1 mở bằng lời cắt ngang của Ambaṭṭha, 2.2 mở bằng
  câu hỏi của Phật, 2.3 mở bằng ví dụ của Phật. Nếu ép ba câu mở giống nhau mới là
  sai. Cái cần trùng là câu kết và công thức giữa, và chúng đã trùng.
- **Nhịp lặp sáu lần trong danh sách đã đạt.** Đây là chỗ dễ hỏng nhất, nên đối chiếu
  riêng:

| Đoạn | Pali `ambaṭṭho māṇavo` | Việt “Ambaṭṭha” | Ghi chú |
|---|---|---|---|
| 1.17.3 | 6 | 6 | Sáu vị ngữ, sáu lần gọi tên. |
| 1.18.3 | 7 | 7 | Sáu lần trong danh sách + “gác Ambaṭṭha” ở cuối. |
| 1.18.5–6 | 7 | 7 | Sáu lần trong danh sách + “thanh niên Ambaṭṭha” ở 1.18.6. |
| 1.19.1 | 7 | 7 | Sáu lần trong danh sách + “để Ambaṭṭha” ở câu kết. |

- **Các chỗ lặp khác cũng đạt.** 1.10.2 giữ đủ bốn lời gọi “thưa ngài Gotama” cho bốn
  vế đi/đứng/ngồi/nằm; 1.12.1 giữ đủ ba lần “chính Đức Thế Tôn”; 1.12.3–1.12.6 giữ
  đủ bốn lần “dòng dõi Sakya”; 1.21.4 giữ đủ ba lần “tìm chỗ che chở / ẩn náu / nương
  tựa nơi Đức Thế Tôn”. Đây là những chỗ dễ bị nén, và bản dịch không nén.
- **2.4 có đủ ba lần hỏi, nhưng không phải ba lần im lặng.** Lần một: hỏi đầy đủ
  (1.20.4–5), im lặng (1.20.6). Lần hai: hỏi đầy đủ (1.20.7–8), im lặng (1.20.9).
  Lần ba: không hỏi lại đầy đủ ngay, mà ra tối hậu thư “ai được hỏi đến ba lần mà
  không trả lời thì đầu sẽ vỡ” (1.20.10–12); Vajirapāṇī hiện (1.21.1–3); Ambaṭṭha
  xin nhắc lại (1.21.4–6); Phật nhắc lại đầy đủ (1.21.7–8); Ambaṭṭha đáp
  (1.21.9–11). Bản dịch giữ đúng thứ tự này. Nếu người đọc đếm thành “ba lần im
  lặng” thì là do lời giới thiệu, không phải do bản dịch; báo cáo A đã chỉ ra lỗi ấy.
- **Câu hỏi dòng dõi lặp gần như từng chữ** ở 1.20.4–5, 1.20.7–8 và 1.21.7–8. Đây là
  nhịp điệp khúc của 2.4, và nó đã đúng. Cú pháp câu hỏi đã được rút gọn bằng dấu
  hai chấm, nên không còn câu dài dồn phần dẫn lên đầu.

## Câu công thức và xưng hô

### Câu công thức

| Câu (Pali → Việt) | Số lần trong phạm vi | Đúng | Ghi chú |
|---|---|---|---|
| `Atha kho bhagavā ambaṭṭhaṁ māṇavaṁ etadavoca:` → “Rồi Đức Thế Tôn nói với thanh niên Ambaṭṭha:” | 3 (1.15.3, 1.20.1, 1.20.10) | 3/3 | Đúng từng chữ. Ngoài phạm vi còn 1 lần ở 02. |
| `Dutiyampi kho bhagavā ambaṭṭhaṁ māṇavaṁ etadavoca:` → “Lần thứ hai, Đức Thế Tôn nói với thanh niên Ambaṭṭha:” | 1 (1.20.7) | 1/1 | Biến thể có `Dutiyampi`; `etadavoca` là “nói”, không phải “hỏi”. |
| `Taṁ kiṁ maññasi, ambaṭṭha,` → “Ambaṭṭha, ông nghĩ thế nào?” | 3 (1.20.4, 1.20.8, 1.21.7) | 3/3 | Đúng từng chữ; cả ba lần đều mở đầu câu hỏi dòng dõi. |
| `Evaṁ vutte, ambaṭṭho māṇavo tuṇhī ahosi.` → “Khi nghe vậy, thanh niên Ambaṭṭha im lặng.” | 1 (1.20.6) | 1/1 | Đúng từng chữ. |
| `Dutiyampi kho ambaṭṭho māṇavo tuṇhī ahosi.` → “Lần thứ hai, thanh niên Ambaṭṭha vẫn im lặng.” | 1 (1.20.9) | 1/1 | “Vẫn” là thêm nhỏ để nối, không đổi nghĩa; có thể bỏ nếu muốn sát chữ tuyệt đối. |
| `Itiha … idaṁ paṭhamaṁ … ibbhavādaṁ nipātesi.` → “Thế là … lần thứ nhất ném chữ "tiện dân" vào dòng Sakya.” | 3 (1.12.9, 1.13.6, 1.14.9) | 3/3 | Ba câu song song, chỉ khác số thứ tự. |
| `Atha kho bhagavato etadahosi:` → “Rồi Đức Thế Tôn nghĩ như thế này:” | 1 (1.15.1) | 1/1 | Đúng từng chữ. |
| `Atha kho … rājā okkāko … āmantesi:` → “Rồi vua Okkāka … gọi … lại bảo:” | 1 (1.15.12) | 1/1 | Đúng; “lại bảo” tự nhiên hơn “gọi… mà bảo”. |
| `… udānaṁ udānesi:` → “…thốt lên lời cảm thán:” | 1 (1.15.16) | 1/1 | Đã sửa từ “buột miệng thốt lên lời cảm khái”. |
| `Te evamāhaṁsu:` → “Họ nói như thế này:” | 1 (1.16.7) | 1/1 | Đúng. |
| `Evaṁ vutte, te māṇavakā bhagavantaṁ etadavocuṁ:` → “Khi nghe vậy, các thanh niên ấy nói với Đức Thế Tôn:” | 1 (1.17.1) | 1/1 | Đúng khuôn `Evaṁ vutte`; không nằm trong bảng §5 nhưng dùng nhất quán. |
| `Atha kho bhagavā te māṇavake etadavoca:` → “Rồi Đức Thế Tôn nói với các thanh niên ấy:” | 1 (1.18.1) | 1/1 | Đúng. |

Không có câu công thức nào bị đổi đại từ hay đổi ngôi. Hai chỗ cần lưu ý:

- **1.20.10** dùng “Rồi Đức Thế Tôn nói với thanh niên Ambaṭṭha:” đúng công thức,
  nhưng nội dung sau đó là tối hậu thư chứ không phải câu hỏi đầy đủ. Đây là Pali,
  không phải lỗi dịch. Nếu người đọc thấy “lần thứ ba” bị hẫng, có thể thêm một chú
  thích ngắn ở 1.20.10: “Đây là lần thứ ba Đức Thế Tôn hỏi, nhưng Ngài không lặp lại
  câu hỏi đầy đủ; Ngài ra tối hậu thư trước.”
- **1.21.4** là `Atha kho ambaṭṭho māṇavo … upanisīditvā bhagavantaṁ etadavoca:` — bản
  dịch “bèn ngồi xuống sát bên và nói với Đức Thế Tôn:” giữ đúng động tác
  `upanisīditvā`, không cần dùng đúng khuôn “Rồi … nói với …” vì có thêm cử chỉ.

### Xưng hô

- **Đức Thế Tôn → Ambaṭṭha:** “ông” trong mọi lời trực tiếp. 1.14.2 đã đổi từ “Bậc
  đáng kính như Ambaṭṭha không nên…” thành “Ông là bậc đáng kính, không nên…”. Không
  có “ngươi”, “mày”, “thằng” trong cả ba tệp.
- **Người kể → Đức Thế Tôn:** “Đức Thế Tôn” 6 lần ở 03, 1 lần ở 04, 15 lần ở 05;
  “Đức Phật” 0 lần. Đúng §3.
- **Ambaṭṭha → Đức Thế Tôn:** “thưa ngài Gotama” trong mọi lời gọi trực tiếp. Hai chỗ
  1.21.5–6 dùng “thưa ngài Gotama” / “Xin ngài Gotama” để render `bhavaṁ gotamo` (kính
  ngữ), không phải `bho gotama`; đây là chuyển đúng, không phải lỗi.
- **Các thanh niên → Đức Thế Tôn:** “thưa ngài Gotama” ở 1.17.2, 1.17.3, 1.19.1. Họ
  nói về Ambaṭṭha ở ngôi thứ ba, không gọi anh ta trực tiếp; không có chỗ nào dùng
  “ngươi/mày”.
- **Yakkha → Ambaṭṭha:** “hắn” ở 1.21.2 (“ta sẽ làm đầu hắn vỡ thành bảy mảnh”). Đây
  là trường hợp duy nhất dùng “hắn” trong ba tệp. Yakkha đang đe dọa, nên “hắn” có
  lý; nhưng nếu dự án muốn tránh đại từ miệt thị hoàn toàn, đổi thành “ông ta” hoặc
  “người ấy”. Đừng để “hắn” lọt vào lời Đức Thế Tôn — hiện không có.
- **1.11.2 — Phật nói với Ambaṭṭha nhưng nói về anh ta ở ngôi thứ ba:** bản dịch giữ
  đúng: “Thanh niên Ambaṭṭha này chưa tu tập xong mà lại tưởng mình đã tu tập xong…”.
  Lời này nằm trong cùng dấu ngoặc bắt đầu từ 1.11.1 (“Này Ambaṭṭha…”), nên người
  đọc biết Ngài đang nói với ông ta. Tiếng gọi `bho` trong 1.11.2 không được dịch,
  nhưng thêm “Này Ambaṭṭha” lần nữa sẽ lặp tên ngay sau 1.11.1; giữ như hiện tại là
  chấp nhận được.
- **“Ta” của Đức Thế Tôn:** xuất hiện ở 1.15.2 (“ta hỏi”), 1.18.3 (“các vị cứ tranh
  luận với ta”), 1.18.6 (“đối đáp với ta”). §3 không cấm, nhưng báo cáo A đã nêu cùng
  vấn đề ở 1.9.5: “ta” đi với “ông” tạo giọng bề trên, hơi lệch mục tiêu “lịch sự
  đến mức lạnh lùng”. Đây là quyết định ở cấp hướng dẫn, không phải lỗi cục bộ; nếu
  sửa thì phải sửa đồng loạt (1.9.5, 1.15.2, 1.18.3, 1.18.6), không nên sửa lẻ.

## Chất văn — chỗ cần viết lại

Các chỗ dưới đây không phải lỗi nghĩa; chỉ là lựa chọn từ ngữ có thể làm câu rõ hoặc
sát Pali hơn. Không bắt buộc sửa.

1. **1.13.1 — “mất lòng ông”.** Pali `aparaddhun` là “làm gì sai/quấy rầy”. Đề xuất:
   “Này Ambaṭṭha, dòng Sakya đã làm gì sai với ông?” “Mất lòng” nhẹ hơn và nghiêng
   về cảm giác bị xúc phạm, trong khi câu hỏi của Phật là hỏi nguyên do.
2. **1.15.13 — “đang ở đâu”.** Pali `sammanti` là “định cư, ngụ lại”. Đề xuất:
   “Này các vị, hiện giờ các vương tử đang định cư ở đâu?” Câu hiện tại không sai,
   nhưng “đang ở đâu” có thể chỉ là đang đứng/đang ngồi.
3. **1.20.9 — “vẫn im lặng”.** Pali `Dutiyampi … tuṇhī ahosi` chỉ nói “lần thứ hai
   im lặng”, không có “vẫn”. “Vẫn” là thêm nhỏ để nối; nếu muốn sát chữ, bỏ “vẫn”.
4. **1.15.10 — “khu rừng sāka”.** Chú thích 1.15.10 giải thích sāka/sāla, nhưng người
   đọc phổ thông gặp “khu rừng sāka” lần đầu mà không có gì níu. Có thể viết “khu
   rừng sāka (sa-la)” ngay lần đầu, hoặc để nguyên và tin vào chú thích.
5. **1.16.10 — câu chốt dài.** “Như vậy đó, này Ambaṭṭha, khi nhớ lại tên họ và dòng
   dõi bên cha mẹ ông từ thuở xưa, thì dòng Sakya là con của các bậc chủ nhân, còn
   ông là con của một người nữ tỳ của dòng Sakya.” Câu đúng nhưng nặng vì “khi… thì…”
   chen giữa. Có thể thêm dấu hai chấm sau “Ambaṭṭha”: “Như vậy đó, này Ambaṭṭha:
   khi nhớ lại…, thì…”. Không nên tách thành hai câu vì đây là câu kết đòn.
6. **1.21.2 — “hắn”.** Đây là lời đe dọa của dạ-xoa, nên “hắn” có lý; giữ nguyên.
   Chỉ cần bảo đảm “hắn” không lọt vào lời Đức Thế Tôn.

### Chú thích

Bản dịch đã rút gọn nhiều chú thích nguồn. Đáng chú ý nhất là 1.15.4: chú thích nguồn
dài về Mahābhārata, Arrian và Manusmṛti đã được rút còn hai câu (“Ambaṭṭha cũng
là tên một dân tộc ở miền tây bắc… người Abastania mà sử gia Arrianô nhắc đến…”). Đây
là cách xử lý đúng cho người đọc phổ thông. Nếu sau này khôi phục chi tiết, phải dùng
đúng Manusmṛti 10.8 (không phải 1.8), Arrian quyển VI chương 15 (không chỉ “chapter
15”), và nói “quân của Alexandros” vì Arrian kể Perdiccas đánh tan người Abastania.

Các chú thích còn lại nhìn chung chính xác. Bốn chú thích còn quá dài so với người
đọc phổ thông:

| # | Đoạn | Chú thích hiện tại | Vấn đề | Đề xuất |
|---|---|---|---|---|
| 1 | 03:1.12.7 | `ibbha` = “tiện dân”, gốc “con voi”, `hatthigopakā`; thêm Chāndogya Upaniṣad 1.10 và Snp 3.1:18.4. | Phần từ nguyên rất hay và cần; hai dẫn chứng Sanskrit/Pali không cần cho người đọc phổ thông. | Giữ câu đầu (ibbha = tiện dân, gốc “voi”, người giữ voi); cắt Chāndogya và Snp, hoặc chỉ giữ một câu “Pali cũng có chỗ gọi dân bản địa là niketino”. |
| 2 | 05:1.16.1 | `dāsa` trong Vệ-đà = “nô lệ, người hầu”, cũng chỉ kẻ thù; kṛṣṇayoni, Rig Veda 2.20.7, 10.22.8, 10.62.10; Disā có lẽ từ dviṣa. | Ba dẫn chứng cho một giả thuyết từ nguyên; với người đọc phổ thông, chúng chỉ làm nặng thêm. | Rút còn một câu: “Trong tiếng Vệ-đà, dāsa vừa có nghĩa ‘nô lệ, người hầu’, vừa dùng để chỉ kẻ thù; tên Disā có lẽ liên quan đến dviṣa (‘kẻ thù’).” Cắt ba số câu Rig Veda và chi tiết “bào thai đen tối”. |
| 3 | 05:1.20.3 | Lời đe dọa làm đầu vỡ tung; Bṛhadāraṇyaka 1.3.24, 3.9.26; Rāmāyaṇa 7.26.44c; Mahābhārata 14.7.2c. | Ba dẫn chứng cho một motif; chỉ cần một tương đương là đủ. | Giữ một câu: “Lời đe dọa làm đầu vỡ tung cũng xuất hiện trong Bṛhadāraṇyaka Upaniṣad và một số sử thi về sau.” Cắt các số câu cụ thể. |
| 4 | 05:1.21.1 | Vajirapāṇī = Indra/Sakka; MN 35:14.1; Vajrahasta/DN 20:12.1; Rig Veda 1.173.10a; Đại thừa gọi một vị Bồ-tát dữ dằn, bảo vệ Chánh pháp. | Phần xác định Vajirapāṇī = Indra/Sakka rất cần; Rig Veda và Đại thừa là mở rộng, không cần cho đoạn này. | Giữ: “Vajirapāṇī (‘tay cầm tia chớp’) là một dạng của Indra/Sakka; hình ảnh này cũng có ở MN 35.” Cắt Rig Veda và câu Đại thừa. |

Các chú thích sau đã đủ gọn, không nên cắt thêm:

- **1.10.3** `bandhupādāpacca`: giải thích đúng Phạm Thiên và bốn giai cấp; đây là chú
  thích bắt buộc để hiểu lời miệt thị thứ tư.
- **1.10.3** `kaṇha`: giải thích “đen” là miệt thị chủng tộc; đã đổi “tràn vào” thành
  “di cư vào”.
- **1.11.2** `vusita`: giải thích “tu tập xong” theo nghĩa A-la-hán; cần cho cách chơi
  chữ.
- **1.12.2** `rabhasa/bhassa`: giải thích lựa chọn bản PTS và bản chú giải; gọn.
- **1.14.2** `āyasmā`: giải thích vì sao Đức Thế Tôn gọi Ambaṭṭha là “bậc đáng kính”;
  cần cho sắc thái xoa dịu.
- **1.15.5** Kaṇhāyana: một câu, có thể cắt mệnh đề Kāṇvāyana nếu muốn gọn hơn, nhưng
  không cần.
- **1.15.7** Okkāka = Ikṣvāku, con Manu, vương triều Mặt Trời; gọn và đủ.
- **1.15.10** sāka/sāla: giải thích đúng; chỉ nên thống nhất cách gọi “sa-la” trong
  chính văn nếu muốn gloss.
- **1.15.11** saka/sambheda: giải thích cách chơi chữ và loạn luân; gọn.
- **1.16.2** kaṇha/Arthaśāstra: gọn; “quanh chữ ‘đen’” đã sửa.
- **1.17.2** dòng dõi/học vấn: đã sửa “hạnh kiểm” thành “học vấn”; giữ.

Tóm lại về chú thích: **không có chú thích nào sai nghĩa nghiêm trọng**. Vấn đề là tỉ
lệ: bốn chú thích 1.12.7, 1.16.1, 1.20.3, 1.21.1 dài hơn mức cần thiết cho người đọc
phổ thông. Một câu xác định + một câu vì sao nó đáng chú ý là đủ; các số câu Sanskrit,
tên học giả và niên đại nên để cho người làm nghiên cứu.

## Kết luận

**ĐẠT.** Bản dịch bám Pali, giữ đúng thứ tự và đúng người nói; nhịp lặp sáu lần
`ambaṭṭho māṇavo` được giữ đủ 6/7/7/7; công thức năm động từ ở 1.12.8, 1.13.5, 1.14.8
giống hệt; ba câu kết 1.12.9, 1.13.6, 1.14.9 song song; xưng hô đúng bảng §3; không
có từ cấm, ngoặc kép cong hay dấu lược. Ba nghi vấn lớn — nhịp lặp sáu lần, “chung
sống”, và chú thích `bandhupādāpacca` — đều đã ổn trong bản hiện tại (lặp đủ 6/7/7/7,
“ăn nằm”, và chú thích đầy đủ).

Các đề xuất còn lại chỉ là biên tập:

1. Rút bốn chú thích dài 1.12.7, 1.16.1, 1.20.3, 1.21.1 (xem bảng ở mục Chú thích).
2. Tùy chọn: “làm gì sai với ông” ở 1.13.1; “định cư ở đâu” ở 1.15.13; bỏ “vẫn” ở
   1.20.9; gloss “sāka (sa-la)” ở 1.15.10; dấu hai chấm sau “Ambaṭṭha” ở 1.16.10.
3. Giữ “hắn” ở 1.21.2 như một ngoại lệ có chủ ý của lời đe dọa.

Kiểm tra marker:

- `03-primitives-1.md`: 15/15 đoạn — `==> ĐẠT` (728 từ nội dung, kể cả chú thích).
- `04-primitives-2-3.md`: 17/17 đoạn — `==> ĐẠT` (358 từ nội dung).
- `05-slavegirl.md`: 62/62 đoạn — `==> ĐẠT` (2001 từ nội dung, kể cả chú thích).
