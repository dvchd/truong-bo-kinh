# Rà soát B — mục 2.1–2.4 (cuộc tra hỏi)

## Tóm tắt

Phạm vi: `ban-dich/03-primitives-1.md` (dn3:1.10.0–1.12.9, 15 đoạn),
`ban-dich/04-primitives-2-3.md` (dn3:1.13.0–1.14.9, 17 đoạn) và
`ban-dich/05-slavegirl.md` (dn3:1.15.0–1.21.11, 62 đoạn). Tổng cộng 94 đoạn.
Đối chiếu `root_text` (PLI), `translation_text` (EN của Bhikkhu Sujato) và `comment_text`
(NOTE) trong `nguon/api_dn3.json`; đọc thêm các tệp nguồn tương ứng trong `nguon/sections/`.
Kiểm tra theo thứ tự: nghĩa so với Pali, nhịp điệp khúc, xưng hô, câu công thức §5, chất văn,
chú thích.

Kết quả chính:

- **Ba lỗi nặng còn tồn đọng.** (1) Nhịp lặp sáu lần `ambaṭṭho māṇavo` ở 1.17.3, 1.18.3,
  1.18.5, 1.19.1 bị nén còn hai lần — đây là chỗ mất nhịp lớn nhất của cả mục. (2) “Chung
  sống” ở 1.15.11 và 1.15.15 làm nhẹ chuyện loạn luân, trong khi đó chính là điểm Đức Thế
  Tôn dùng để bẻ Ambaṭṭha. (3) `bandhupādāpacca` ở 1.10.3 được dịch đúng nghĩa đen nhưng
  không có chú thích, nên lời miệt thị thứ tư trong danh sách thành vô nghĩa với người đọc
  phổ thông.
- **Hai mươi nhóm lỗi nhẹ đã sửa trực tiếp** trong ba tệp: chủ yếu là xưng hô, câu công
  thức, từ Hán-Việt tối nghĩa, đại từ mơ hồ và vài chỗ thêm/bớt một chữ. Danh sách ở dưới.
- **Khung nhịp 2.1–2.3 đã đúng.** Ba câu kết 1.12.9, 1.13.6, 1.14.9 giờ giống nhau từng
  chữ, chỉ khác số thứ tự; công thức năm động từ ở 1.12.8, 1.13.5, 1.14.8 giống hệt. Chỗ
  còn lệch không nằm ở khung mà nằm trong các danh sách 1.17.3–1.19.1 và ở 1.10.2.
- **2.4 có ba lần hỏi nhưng chỉ hai lần im lặng**, không phải ba lần im lặng. Ba lần hỏi là
  1.20.4–5, 1.20.7–8 và 1.21.7–8; hai lần im lặng là 1.20.6 và 1.20.9; lần thứ ba bị
  Vajirapāṇī chặn trước khi Ambaṭṭha kịp im lặng (1.20.10–1.21.3). Bản dịch giữ đúng thứ
  tự và đúng người nói. Cách đếm “ba lần im lặng” trong `00-gioi-thieu.md` là sai; báo cáo
  A đã bắt lỗi này (mục 6 của A), tôi chỉ nhắc lại vì nó ảnh hưởng đến cách đọc nhịp 2.4.
- **Chú thích nhìn chung chính xác nhưng quá hàn lâm.** Các chú thích dài về Mahābhārata,
  Arrian, Manusmṛti, Rig Veda đều có thể rút còn một đôi câu mà không mất thông tin cần
  cho việc hiểu chính văn. Ba chỗ cần chỉnh trong chú thích đã được sửa (Manusmṛti 10.8,
  Arrian quyển VI chương 15, “quân của Alexandros”).
- **Kiểm tra marker:** cả ba tệp đều `==> ĐẠT` (15/15, 17/17, 62/62). Không có “Đức Phật”,
  “ngươi”, “mày”, “thằng”, ngoặc kép cong, `...` hay `…` trong ba tệp.

Kết luận tạm: **CẦN SỬA** — không phải vì sai giáo lý hay sai nghĩa nặng, mà vì mất nhịp
lặp ở bốn đoạn trọng tâm, làm nhẹ một chi tiết tố cáo, và thiếu một chú thích khiến lời
miệt thị không đọc được. Sửa xong ba chỗ ấy thì phần này đạt.

## Lỗi nặng (phải sửa)

| # | Tệp | Đoạn | Hiện tại | Vấn đề | Đề xuất |
|---|---|---|---|---|---|
| 1 | 05-slavegirl.md | dn3:1.17.3; 1.18.3; 1.18.5; 1.19.1 | 1.17.3: “Thưa ngài Gotama, thanh niên Ambaṭṭha sinh ra trong dòng dõi tốt, là con nhà gia thế, học rộng, ăn nói khéo, thông minh, và thanh niên Ambaṭṭha có thể đối đáp với ngài Gotama về vấn đề này.” | Pali lặp `ambaṭṭho māṇavo` 6 lần ở 1.17.3, 7 lần ở 1.18.3, 6 lần ở 1.18.5, 7 lần ở 1.19.1. Bản dịch chỉ còn 2 lần trong danh sách vị ngữ ở 1.17.3, 2 lần ở 1.18.3, 2 lần ở 1.18.5 và 2 lần ở 1.19.1 (thêm 1 lần ở câu kết). Đây không phải danh sách bình thường: mỗi vị ngữ bị đập xuống bằng một lần gọi tên, tạo nhịp búa gõ. Nén lại thì câu trôi và mất sắc thái dồn ép; bốn đoạn cũng không còn vang nhau. §1.4 của hướng dẫn nói rõ: PLI lặp thì bản dịch phải lặp. | Lặp tên trước mỗi vị ngữ. 1.17.3: “Thưa ngài Gotama, thanh niên Ambaṭṭha sinh ra trong dòng dõi tốt, thanh niên Ambaṭṭha là con nhà gia thế, thanh niên Ambaṭṭha học rộng, thanh niên Ambaṭṭha ăn nói khéo, thanh niên Ambaṭṭha thông minh, và thanh niên Ambaṭṭha có thể đối đáp với ngài Gotama về vấn đề này.” Áp dụng cùng khuôn cho 1.18.3 (danh sách phủ định), 1.18.5 (danh sách khẳng định) và 1.19.1 (các thanh niên lặp lại danh sách khẳng định). Nếu thấy “thanh niên Ambaṭṭha” sáu lần quá nặng, có thể dùng “Ambaṭṭha” ở các lần sau; nhưng phải lặp tên, không được nuốt vào đại từ. |
| 2 | 05-slavegirl.md | dn3:1.15.11; 1.15.15 | 1.15.11: “Vì sợ dòng dõi bị pha lẫn, họ đã chung sống với chính các chị em gái của mình.” 1.15.15: “…họ đang chung sống với chính các chị em gái của mình.” | `saṁvāsaṁ kappesuṁ` trong ngữ cảnh này là quan hệ tính dục, không chỉ ở chung. “Chung sống” tiếng Việt có thể chỉ là sống cùng nhà, nên làm nhẹ chuyện loạn luân — đúng cái scandal mà Đức Thế Tôn đang dùng để cho thấy gốc gác Sakya không trong sạch như Ambaṭṭha tưởng. EN của Sujato dịch “slept with”; chú thích 1.15.11 đã nói thẳng “loạn luân”, nhưng chính văn lại rụt rè hơn chú thích. | 1.15.11: “…họ đã ăn nằm với chính các chị em gái của mình.” 1.15.15: “…họ đang ăn nằm với chính các chị em gái của mình.” Nếu muốn bớt thô, “lấy nhau” cũng rõ hơn “chung sống”, nhưng “ăn nằm” sát nghĩa và sát giọng Pali hơn. |
| 3 | 03-primitives-1.md | dn3:1.10.3 | “Còn bọn sa-môn trọc đầu, bọn sa-môn rởm, bọn tiện dân, bọn đen, bọn sinh ra từ gót chân của người bà con dòng họ chúng ta, thì ta nói chuyện với chúng cũng đúng như ta đang nói với ngài Gotama vậy.” | `bandhupādāpacca` được dịch đúng nghĩa đen nhưng người đọc không có cách nào biết “người bà con” là Brahmā và “gót chân” là huyền thoại bốn giai cấp sinh ra từ bốn phần thân của Ngài. Trong cùng một câu, “tiện dân” và “bọn đen” đã có chú thích, còn lời miệt thị thứ tư thì bỏ trống. Với người đọc phổ thông, “bọn sinh ra từ gót chân của người bà con dòng họ chúng ta” là một cụm vô nghĩa, làm mất lực của cả danh sách. | Thêm chú thích ngay sau 1.10.3: “Bandhupādāpacca nghĩa đen là ‘sinh ra từ gót chân của người bà con’. Theo huyền thoại Bà-la-môn, bà-la-môn sinh ra từ miệng Brahmā, sát-đế-lợi từ cánh tay, phệ-xá từ đùi, thủ-đà-la từ gót chân; ‘người bà con’ ở đây là Brahmā, tổ chung. Vì thế đây là lời miệt thị hạng người thấp kém.” Có thể thay chính văn bằng “bọn sinh ra từ gót chân của vị tổ chung (Brahmā)”, nhưng chú thích an toàn hơn vì không thêm tên riêng vào lời Ambaṭṭha. |

## Lỗi nhẹ (đã sửa trực tiếp)

| # | Tệp | Đoạn | Đã sửa thành | Lý do |
|---|---|---|---|---|
| 1 | 03-primitives-1.md | dn3:1.11.1 | “…Ông hãy chú tâm cho kỹ vào chính mục đích ấy.” | “Khéo chú tâm vào chính mục đích mà mình đã đến đây” là calque của `yadattāya upasaṅkamitvā`; “mục đích mà mình đã đến đây” vừa lặp vừa tối. |
| 2 | 03-primitives-1.md | dn3:1.11.2; 1.12.1 | “chưa tu tập xong” (thay cho “chưa tu tập”) | `vusita` là đã hoàn tất; chú thích 1.11.2 nói rõ chữ này thường chỉ quả vị A-la-hán. Thiếu “xong” thì cách chơi chữ `vusitamānī` (“tưởng mình đã tu tập xong”) không còn. |
| 3 | 03-primitives-1.md | dn3:1.12.1 | “…bèn chửi rủa chính Đức Thế Tôn, khinh bỉ chính Đức Thế Tôn và mắng nhiếc chính Đức Thế Tôn:” | Pali lặp `bhagavantaṁyeva` ba lần; bản cũ nén còn một, làm mất nhịp ba bước của câu. |
| 4 | 03-primitives-1.md | dn3:1.12.7; 1.12.9 | 1.12.7 thêm “lại” trước “không kính trọng”; 1.12.9 “lần thứ nhất” (thay cho “lần đầu tiên”) | 1.12.8, 1.13.5, 1.14.8 đều có “lại”; thêm vào 1.12.7 cho bốn lần khớp nhau. “Lần thứ nhất” song song với “lần thứ hai/ba” ở hai câu kết sau. |
| 5 | 04-primitives-2-3.md | dn3:1.13.0; 1.14.0 | “### 2.2. Lần thứ hai dùng chữ "tiện dân"”; “### 2.3. Lần thứ ba dùng chữ "tiện dân"” | Hai tiêu đề cũ chỉ là “Lần thứ hai/ba”, không nói rõ làm gì; tiêu đề 2.1 đã có “dùng chữ "tiện dân"”. Sửa cho khớp mẫu và khớp Pali `dutiya/tatiya ibbhavāda`. |
| 6 | 04-primitives-2-3.md | dn3:1.13.3; 1.13.4 | “nhà họp chung” (thay cho “nhà hội”) | “Nhà hội” là từ Hán-Việt cổ, ít người đọc phổ thông hiểu; `santhāgāra` là nhà họp chung của dòng họ. |
| 7 | 04-primitives-2-3.md | dn3:1.13.4 | “…và cũng chẳng ai mời tôi ngồi vào một chỗ nào.” | Bản cũ “không ai mời tôi một chỗ ngồi nào” vừa lúng túng vừa mất `api` (“even”): ngay cả một chỗ ngồi cũng không ai mời. |
| 8 | 04-primitives-2-3.md | dn3:1.14.1 | “…cũng được tự do hót trong chính tổ của mình.” | `sake kulāvake` = “trong tổ của chính nó”; “chính… của mình” giữ được tiếng vang `saka`/Sakya mà câu sau sẽ khai thác. Bản cũ “trong tổ của nó” trôi và mất chữ “chính”. |
| 9 | 04-primitives-2-3.md | dn3:1.14.2 | “Ông là bậc đáng kính, không nên nổi nóng vì một chuyện nhỏ nhặt như vậy.” | §3 quy định Đức Thế Tôn gọi Ambaṭṭha là “ông”; bản cũ “Bậc đáng kính như Ambaṭṭha không nên…” vừa dùng ngôi thứ ba vừa nghe như mỉa mai, trái với giọng hòa giải của đoạn. |
| 10 | 05-slavegirl.md | dn3:1.15.2 | “Thanh niên Ambaṭṭha này lấy chữ ‘tiện dân’ mà mạt sát dòng Sakya quá mức.” | Bản cũ “cứ lấy… quá đáng lắm rồi” nghe bực bội; Đức Thế Tôn trong đoạn này điềm tĩnh, chỉ nhận xét rồi quyết định hỏi dòng dõi. Bỏ “cứ” và “quá đáng lắm rồi” để giọng lạnh lại. |
| 11 | 05-slavegirl.md | dn3:1.15.4 (chú thích) | “Manusmṛti 10.8”; “quyển VI, chương 15”; “bị quân của Alexandros đánh tan” | Ba chỗ sai/thiếu: chú thích gốc của Sujato ghi Manusmṛti 1.8, nhưng điều nói về con lai giữa bà-la-môn và phệ-xá là 10.8; Arrian chỉ ghi “chapter 15” mà không nói quyển, đúng là quyển VI chương 15; Arrian kể Perdiccas đánh tan người Abastania, nên “quân của Alexandros” chính xác hơn “Alexandros” một mình. |
| 12 | 05-slavegirl.md | dn3:1.15.5 | “Thưa ngài Gotama, tôi thuộc dòng Kaṇhāyana.” | `kaṇhāyano` là tên dòng, không phải tên người; “tôi là người Kaṇhāyana” dễ bị hiểu là “người tên Kaṇhāyana”. |
| 13 | 05-slavegirl.md | dn3:1.15.6; 1.16.10 | “…khi nhớ lại tên họ và dòng dõi bên cha mẹ ông từ thuở xưa…” | `anussarato` là tuyệt đối phân từ (“khi nhớ lại”), không phải mệnh lệnh; bản cũ “nhớ lại…” đọc như lời khuyên. “Bên cha mẹ” làm rõ `mātāpettikaṁ` (cả dòng cha lẫn dòng mẹ). |
| 14 | 05-slavegirl.md | dn3:1.15.6 (chú thích) | “…nghĩa là dòng Sakya sinh ra từ các bậc chủ nhân ấy, chứ không phải chính họ là chủ.” | Câu cũ “nghĩa không phải là dòng Sakya làm chủ, mà là họ sinh ra từ các bậc chủ nhân ấy” tối nghĩa, người đọc không biết “không phải… mà là” phủ định cái gì. |
| 15 | 05-slavegirl.md | dn3:1.15.8 | “…con trai của bà chánh hậu mà mình yêu quý…” (bỏ “nhất”) | Pali `piyā manāpā` là “yêu quý, dễ mến”, không có so sánh nhất; “nhất” là thêm, dù EN của Sujato cũng dịch “most beloved”. Giữ “nhất” là thêm chi tiết không có trong PLI. |
| 16 | 05-slavegirl.md | dn3:1.15.16 | “Rồi vua Okkāka, này Ambaṭṭha, thốt lên lời cảm thán:” | “Buột miệng thốt lên lời cảm khái” pha hai giọng: “buột miệng” thân mật, “cảm khái” Hán-Việt trừu tượng. `udāna` là lời cảm thán/thốt lên; “thốt lên lời cảm thán” gọn và đúng. |
| 17 | 05-slavegirl.md | dn3:1.15.18; 1.16.9 | “vua Okkāka” (thay cho “vị ấy”); “Kaṇha” (thay cho “vị ấy”) | Hai chỗ “vị ấy” mơ hồ: ở 1.15.18 là Okkāka, ở 1.16.9 là Kaṇha. Làm rõ không thêm nghĩa, chỉ giải quyết đại từ treo. |
| 18 | 05-slavegirl.md | dn3:1.16.2 (chú thích); 1.16.6 | “…quanh chữ ‘đen’”; “…nhận ra đó là ‘kẻ đen’.” | Pali có `‘kaṇhā’ti` — dấu ngoặc cho thấy “đen/kẻ đen” là nhãn được gán, không phải lời miêu tả trung tính. Bản cũ không có ngoặc ở 1.16.6, đọc như tác giả khẳng định. |
| 19 | 05-slavegirl.md | dn3:1.20.2; 1.20.7; 1.20.12; 1.21.2 | “đang đặt ra cho ông”; “Lần thứ hai, Đức Thế Tôn nói với thanh niên Ambaṭṭha:”; “đến ba lần” | `āgacchati` là “nảy ra/đặt ra”, không phải “đến với ông”; `etadavoca` là “nói”, không phải “hỏi”; `yāvatatiyakaṁ` là “đến ba lần”, không phải “đến lần thứ ba”. |
| 20 | 05-slavegirl.md | dn3:1.20.3 (chú thích) | “Lời đe dọa làm đầu vỡ tung…” | Chính văn nói “vỡ thành bảy mảnh”; “nổ tung” là hình ảnh khác (nổ vì lực từ trong ra), không khớp với `muddhaṁ phālessāmi` (chẻ/vỡ). |

## Nhịp điệu ba lần

Mục 2.1–2.4 không được xây bằng bốn câu mở giống nhau. Nó được xây bằng một **khung**:

1. Đức Thế Tôn ra đòn (nhận xét, câu hỏi, hoặc ví dụ).
2. Ambaṭṭha đáp lại bằng một lần miệt thị “tiện dân”.
3. Một công thức năm động từ giống hệt nhau.
4. Một câu kết giống hệt nhau, chỉ khác số thứ tự.

Sang 2.4, khung đổi hẳn: Đức Thế Tôn không nói về “tiện dân” nữa mà hỏi dòng dõi; Ambaṭṭha
không miệt thị nữa mà im lặng; và cái kết không phải lời kết tội dòng Sakya mà là lời thú
nhận nguồn gốc của chính Ambaṭṭha. Vì thế “ba lần” ở đây là ba lần **lảng tránh bằng miệt
thị**, không phải ba lần im lặng. Cái được gọi là “ba lần im lặng” chỉ nằm trong 2.4, và thực
ra chỉ có hai lần.

| Lần | Câu mở | Câu kết | Câu lặp giữa | Nhịp có trùng không? |
|---|---|---|---|---|
| 2.1 (1.10–1.12) | Ambaṭṭha: “Không phải vậy, thưa ngài Gotama.” (1.10.1) | “Thế là thanh niên Ambaṭṭha lần thứ nhất ném chữ ‘tiện dân’ vào dòng Sakya.” (1.12.9) | Năm động từ ở 1.12.7 và 1.12.8 | Kết đúng; giữa đúng. Mở khác 2.2/2.3 là có chủ ý: đây là lời Ambaṭṭha cắt ngang, không phải lời Phật. |
| 2.2 (1.13) | Đức Thế Tôn: “Này Ambaṭṭha, dòng Sakya đã làm gì mất lòng ông?” (1.13.1) | “…lần thứ hai ném chữ ‘tiện dân’ vào dòng Sakya.” (1.13.6) | Năm động từ ở 1.13.5 | Kết đúng, song song với 2.1 sau khi sửa “lần thứ nhất”. Mở khác 2.1 là có chủ ý: đây là câu hỏi của Phật. |
| 2.3 (1.14) | Đức Thế Tôn: “Này Ambaṭṭha, đến con chim cút nhỏ cũng được tự do hót trong chính tổ của mình.” (1.14.1) | “…lần thứ ba ném chữ ‘tiện dân’ vào dòng Sakya.” (1.14.9) | Năm động từ ở 1.14.8 | Kết đúng, song song với 2.1/2.2. Mở khác là có chủ ý: đây là ví dụ của Phật, và là đòn nặng nhất trong ba lần. |
| 2.4 (1.15–1.21) | Rồi Đức Thế Tôn nghĩ như thế này: Ngài thấy Ambaṭṭha lấy chữ “tiện dân” mà mạt sát dòng Sakya quá mức, nên quyết định hỏi dòng dõi ông ta. (1.15.1–2) | “và vị ấy là vị tổ đầu tiên của dòng Kaṇhāyana.” (1.21.11) | Câu hỏi dòng dõi lặp ba lần: 1.20.4–5, 1.20.7–8, 1.21.7–8 | Kết khác hẳn 2.1–2.3 là có chủ ý: cái bẫy đã đóng. Nhịp trong 2.4 là nhịp hỏi–im–hỏi–im–đe–hỏi lại–đáp, không phải nhịp miệt thị. |

Phân tích:

- **Ba câu kết đã song song.** 1.12.9, 1.13.6, 1.14.9 giống nhau từng chữ, chỉ khác “thứ
  nhất / thứ hai / thứ ba”. Trước khi sửa, 1.12.9 dùng “lần đầu tiên”, phá nhịp. Đã sửa.
- **Công thức năm động từ đã song song.** 1.12.8, 1.13.5, 1.14.8 giống hệt: “dòng Sakya là
  tiện dân, và vẫn cứ là tiện dân, lại không kính trọng bà-la-môn, không tôn trọng bà-la-môn,
  không nể vì bà-la-môn, không cung kính bà-la-môn, không thờ phụng bà-la-môn.” 1.12.7 là
  câu gốc, đứng sau lời dẫn trực tiếp, nên bắt đầu bằng “Họ” thay vì “dòng Sakya” — khác
  biệt này là tất yếu, không phải lỗi. Trước khi sửa, 1.12.7 thiếu “lại”; đã thêm.
- **Câu mở khác nhau là đúng.** 2.1 mở bằng lời cắt ngang của Ambaṭṭha, 2.2 mở bằng câu hỏi
  của Phật, 2.3 mở bằng ví dụ của Phật. Nếu ép ba câu mở giống nhau mới là sai. Cái cần
  trùng là câu kết và công thức giữa, và chúng đã trùng.
- **Chỗ mất nhịp lớn nhất không nằm ở khung mà ở trong danh sách 1.17.3–1.19.1.** Pali lặp
  `ambaṭṭho māṇavo` trước từng vị ngữ; bản dịch chỉ gọi tên ở đầu và cuối, còn ở giữa dùng
  ngôi không. Đây là chỗ “một lần rút gọn” mà yêu cầu rà soát đã cảnh báo. Đã xếp vào lỗi
  nặng số 1.
- **Chỗ mất nhịp thứ hai ở 1.10.2.** Bốn vế đi/đứng/ngồi/nằm và bốn lần `bho gotama` bị nén
  thành một câu dài với một lời gọi. Bốn vế vẫn đủ, nhưng tiếng gọi lặp — cái làm nên nhịp
  lễ nghi — biến mất. Xem mục Chất văn.
- **Chỗ mất nhịp thứ ba ở 1.12.1.** Ba lần `bhagavantaṁyeva` bị nén còn một; đã sửa.
- **2.4 có đủ ba lần hỏi, nhưng không phải ba lần im lặng.** Lần một: hỏi đầy đủ (1.20.4–5),
  im lặng (1.20.6). Lần hai: hỏi đầy đủ (1.20.7–8), im lặng (1.20.9). Lần ba: không hỏi lại
  đầy đủ ngay, mà ra tối hậu thư “ai được hỏi đến ba lần mà không trả lời thì đầu sẽ vỡ”
  (1.20.10–12); Vajirapāṇī hiện (1.21.1–3); Ambaṭṭha xin nhắc lại (1.21.4–6); Phật nhắc lại
  đầy đủ (1.21.7–8); Ambaṭṭha đáp (1.21.9–11). Bản dịch giữ đúng thứ tự này. Nếu người đọc
  đếm thành “ba lần im lặng” thì là do lời giới thiệu, không phải do bản dịch; báo cáo A đã
  chỉ ra lỗi ấy.
- **Câu hỏi dòng dõi lặp gần như từng chữ** ở 1.20.4–5, 1.20.7–8 và 1.21.7–8. Đây là nhịp
  điệp khúc của 2.4, và nó đã đúng. Chỗ cần trau là cú pháp câu hỏi quá dài, không phải số
  lần lặp; xem mục Chất văn.

## Câu công thức và xưng hô

### Câu công thức

| Câu (Pali → Việt) | Số lần trong phạm vi | Đúng | Ghi chú |
|---|---|---|---|
| `Atha kho bhagavā ambaṭṭhaṁ māṇavaṁ etadavoca:` → “Rồi Đức Thế Tôn nói với thanh niên Ambaṭṭha:” | 3 (1.15.3, 1.20.1, 1.20.10) | 3/3 | Đúng từng chữ. Ngoài phạm vi còn 1 lần ở 02. |
| `Dutiyampi kho bhagavā ambaṭṭhaṁ māṇavaṁ etadavoca:` → “Lần thứ hai, Đức Thế Tôn nói với thanh niên Ambaṭṭha:” | 1 (1.20.7) | 1/1 | Biến thể có `Dutiyampi`; trước khi sửa là “hỏi… lần thứ hai”, sai vì `etadavoca` là “nói”. Đã sửa. |
| `Taṁ kiṁ maññasi, ambaṭṭha,` → “Ambaṭṭha, ông nghĩ thế nào?” | 3 (1.20.4, 1.20.8, 1.21.7) | 3/3 | Đúng từng chữ; cả ba lần đều mở đầu câu hỏi dòng dõi. |
| `Evaṁ vutte, ambaṭṭho māṇavo tuṇhī ahosi.` → “Khi nghe vậy, thanh niên Ambaṭṭha im lặng.” | 1 (1.20.6) | 1/1 | Đúng từng chữ. |
| `Dutiyampi kho ambaṭṭho māṇavo tuṇhī ahosi.` → “Lần thứ hai, thanh niên Ambaṭṭha vẫn im lặng.” | 1 (1.20.9) | 1/1 | “Vẫn” là thêm nhỏ để nối, không đổi nghĩa; có thể bỏ nếu muốn sát chữ tuyệt đối. |
| `Itiha … idaṁ paṭhamaṁ … ibbhavādaṁ nipātesi.` → “Thế là … lần thứ nhất ném chữ ‘tiện dân’ vào dòng Sakya.” | 3 (1.12.9, 1.13.6, 1.14.9) | 3/3 | Đã sửa “lần đầu tiên” thành “lần thứ nhất”; ba câu còn lại song song. |
| `Atha kho bhagavato etadahosi:` → “Rồi Đức Thế Tôn nghĩ như thế này:” | 1 (1.15.1) | 1/1 | Đúng từng chữ. |
| `Atha kho … rājā okkāko … āmantesi:` → “Rồi vua Okkāka … gọi … lại bảo:” | 1 (1.15.12) | 1/1 | Đúng; “lại bảo” tự nhiên hơn “gọi… mà bảo”. |
| `Atha kho … rājā okkāko udānaṁ udānesi:` → “Rồi vua Okkāka … thốt lên lời cảm thán:” | 1 (1.15.16) | 1/1 | Đã sửa từ “buột miệng thốt lên lời cảm khái”. |
| `Te evamāhaṁsu:` → “Họ nói như thế này:” | 1 (1.16.7) | 1/1 | Đúng. |
| `Evaṁ vutte, te māṇavakā bhagavantaṁ etadavocuṁ:` → “Khi nghe vậy, các thanh niên ấy nói với Đức Thế Tôn:” | 1 (1.17.1) | 1/1 | Đúng khuôn `Evaṁ vutte`; không nằm trong bảng §5 nhưng dùng nhất quán. |
| `Atha kho bhagavā te māṇavake etadavoca:` → “Rồi Đức Thế Tôn nói với các thanh niên ấy:” | 1 (1.18.1) | 1/1 | Đúng. |

Không có câu công thức nào bị đổi đại từ hay đổi ngôi. Hai chỗ cần lưu ý:

- **1.20.10** dùng “Rồi Đức Thế Tôn nói với thanh niên Ambaṭṭha:” đúng công thức, nhưng
  nội dung sau đó là tối hậu thư chứ không phải câu hỏi đầy đủ. Đây là Pali, không phải lỗi
  dịch. Nếu người đọc thấy “lần thứ ba” bị hẫng, có thể thêm một chú thích ngắn ở 1.20.10:
  “Đây là lần thứ ba Đức Thế Tôn hỏi, nhưng Ngài không lặp lại câu hỏi đầy đủ; Ngài ra tối
  hậu thư trước.”
- **1.21.4** là `Atha kho ambaṭṭho māṇavo … upanisīditvā bhagavantaṁ etadavoca:` — bản dịch
  “bèn ngồi xuống sát bên và nói với Đức Thế Tôn:” giữ đúng động tác `upanisīditvā`, không
  cần dùng đúng khuôn “Rồi … nói với …” vì có thêm cử chỉ.

### Xưng hô

- **Đức Thế Tôn → Ambaṭṭha:** “ông” trong mọi lời trực tiếp. Trước khi sửa, 1.14.2 là
  “Bậc đáng kính như Ambaṭṭha không nên…”, vừa ngôi thứ ba vừa nghe mỉa; đã đổi thành “Ông
  là bậc đáng kính, không nên…”. Không có “ngươi”, “mày”, “thằng” trong cả ba tệp.
- **Người kể → Đức Thế Tôn:** “Đức Thế Tôn” 6 lần ở 03, 1 lần ở 04, 14 lần ở 05; “Đức Phật”
  0 lần. Đúng §3.
- **Ambaṭṭha → Đức Thế Tôn:** “thưa ngài Gotama” trong mọi lời gọi trực tiếp. Hai chỗ
  1.21.5–6 dùng “Ngài Gotama” vì Pali chuyển sang `bhavaṁ gotamo` (kính ngữ ngôi thứ ba),
  không phải `bho gotama`; đây là chuyển đúng, không phải lỗi. Nếu muốn thống nhất tuyệt
  đối thì có thể đổi thành “thưa ngài Gotama”, nhưng sẽ làm mất sắc thái khiếp sợ của
  `bhavaṁ`.
- **Các thanh niên → Đức Thế Tôn:** “thưa ngài Gotama” ở 1.17.2, 1.17.3, 1.19.1. Họ nói về
  Ambaṭṭha ở ngôi thứ ba, không gọi anh ta trực tiếp; không có chỗ nào dùng “ngươi/mày”.
- **Yakkha → Ambaṭṭha:** “hắn” ở 1.21.2 (“ta sẽ làm đầu hắn vỡ thành bảy mảnh”). Đây là
  trường hợp duy nhất dùng “hắn” trong ba tệp. Yakkha đang đe dọa, nên “hắn” có lý; nhưng
  nếu dự án muốn tránh đại từ miệt thị hoàn toàn, đổi thành “ông ta” hoặc “người ấy”. Đừng
  để “hắn” lọt vào lời Đức Thế Tôn — hiện không có.
- **1.11.2 — Phật nói với Ambaṭṭha nhưng nói về anh ta ở ngôi thứ ba:** bản dịch giữ đúng:
  “Thanh niên Ambaṭṭha này chưa tu tập xong mà lại tưởng mình đã tu tập xong…”. Lời này nằm
  trong cùng dấu ngoặc bắt đầu từ 1.11.1 (“Này Ambaṭṭha…”), nên người đọc biết Ngài đang
  nói với ông ta. Tiếng gọi `bho` trong 1.11.2 không được dịch, nhưng thêm “Này Ambaṭṭha”
  lần nữa sẽ lặp tên ngay sau 1.11.1; giữ như hiện tại là chấp nhận được.
- **“Ta” của Đức Thế Tôn:** xuất hiện ở 1.15.2 (“ta hỏi”), 1.18.3 (“các vị cứ tranh luận
  với ta”), 1.18.6 (“đối đáp với ta”). §3 không cấm, nhưng báo cáo A đã nêu cùng vấn đề ở
  1.9.5: “ta” đi với “ông” tạo giọng bề trên, hơi lệch mục tiêu “lịch sự đến mức lạnh lùng”.
  Đây là quyết định ở cấp hướng dẫn, không phải lỗi cục bộ; nếu sửa thì phải sửa đồng loạt
  (1.9.5, 1.15.2, 1.18.3, 1.18.6), không nên sửa lẻ ở đây.

## Chất văn — chỗ cần viết lại

1. **1.10.2 — bốn vế, một lời gọi.** Hiện tại là một câu dài, chỉ có một “thưa ngài Gotama”
   ở đầu, trong khi Pali lặp `bho gotama` bốn lần. Bốn vế đi/đứng/ngồi/nằm vẫn đủ, nhưng
   nhịp lễ nghi bị phẳng. Đề xuất tách thành bốn câu, dùng “còn” để nối:
   “Thưa ngài Gotama, bà-la-môn đang đi thì mới xứng đáng nói chuyện với bà-la-môn đang đi.
   Còn khi đang đứng, bà-la-môn mới xứng đáng nói chuyện với bà-la-môn đang đứng. Khi đang
   ngồi… Khi đang nằm…”
   Nếu muốn sát Pali hơn, lặp “thưa ngài Gotama” trước cả bốn vế; nhưng tiếng Việt sẽ nặng,
   nên tôi nghiêng về bốn câu với một lời gọi + “còn”. Cũng nên xem lại “mới xứng đáng”:
   `arahati` là “phải lẽ/xứng đáng”, không có nghĩa “chỉ khi… mới”; “thì mới xứng đáng” nghe
   như điều kiện. Có thể đổi thành “thì mới phải lẽ” hoặc “thì mới đúng lễ”.
2. **1.12.2 — thẻ người kể cắt đôi lời nói.** Hiện tại: “…Sa-môn Gotama rồi sẽ bị ta làm
   cho bẽ mặt, thưa ngài Gotama!” — thanh niên Ambaṭṭha nói với Đức Thế Tôn như vậy. Rồi
   1.12.3 mở ngoặc mới. Pali dùng `…ti bhagavantaṁ etadavoca:` để dẫn một lời nói kéo dài
   đến 1.12.8; thẻ “như vậy” đóng lời sớm, người đọc tưởng 1.12.3 là lời mới. Đề xuất:
   “…như vậy, rồi nói tiếp:” hoặc “…nói với Đức Thế Tôn như vậy, rồi tiếp:”. Không thêm
   nghĩa, chỉ nối lại mạch.
3. **1.16.4 — động từ thứ ba `parimocetha` bị gộp vào “rửa sạch”.** Hiện tại: “‘Mẹ ơi,
   hãy rửa cho con, mẹ ơi, hãy tắm cho con, hãy rửa sạch cho con khỏi thứ ô uế này; con sẽ
   có ích cho mẹ.’” Pali có ba động từ: `dhovatha` (rửa), `nahāpetha` (tắm), `parimocetha`
   (giải thoát/cứu khỏi), rồi mới đến `imasmā asucismā` (khỏi thứ ô uế này). Bản dịch đổi
   động từ thứ ba thành “rửa sạch… khỏi”, nên ba động từ rửa/tắm/cứu thành hai động từ
   rửa/tắm; mất sắc thái “cứu/thả khỏi” của `parimocetha`. Đề xuất: “‘Mẹ ơi, hãy rửa cho con; mẹ ơi,
   hãy tắm cho con; hãy cứu con khỏi thứ ô uế này; con sẽ có ích cho mẹ.’” Hoặc giữ “gột
   rửa” nếu muốn liền mạch với hình ảnh tắm rửa, nhưng “cứu” sát `parimocetha` hơn.
4. **1.17.3 — “ăn nói khéo”.** `kalyāṇavākkaraṇa` là “nói năng khéo léo, lưu loát”, nhưng
   “ăn nói khéo” trong tiếng Việt hiện đại thường hàm ý “khéo mồm, khéo miệng”, không hẳn
   là lời khen. Trong danh sách ba lần (1.17.3, 1.18.5, 1.19.1), nên đổi thành “ăn nói lưu
   loát” hoặc “lời lẽ khéo léo”. Đây là lựa chọn từ vựng, không phải lỗi nghĩa; nếu đổi thì
   đổi cả ba lần cho khớp, và đổi “ăn nói vụng về” ở 1.18.3 thành “ăn nói lúng túng” nếu
   muốn đối xứng.
5. **1.20.4–5 — câu hỏi dòng dõi quá dài, phần đầu nặng.** Hiện tại: “Theo những gì ông đã
   nghe các bà-la-môn tuổi cao, lão thành, những bậc thầy của các bậc thầy nói lại, dòng
   Kaṇhāyana bắt nguồn từ đâu, và ai là vị tổ đầu tiên của dòng Kaṇhāyana?” Câu này lặp ba
   lần, nên cú pháp càng cần gọn. Đề xuất: “Ông đã nghe các bà-la-môn tuổi cao, lão thành,
   những bậc thầy của các bậc thầy nói lại thế nào: dòng Kaṇhāyana bắt nguồn từ đâu, và ai
   là vị tổ đầu tiên của dòng Kaṇhāyana?” Dấu hai chấm tách phần dẫn khỏi nội dung hỏi, dễ
   đọc hơn mà không đổi nghĩa.
6. **1.21.5–6 — Ambaṭṭha quá bình tĩnh.** Người kể vừa nói anh ta “khiếp sợ, lông tóc dựng
   ngược, tìm chỗ che chở”, nhưng lời thoại “Ngài Gotama vừa nói gì vậy? Xin ngài Gotama nói
   lại lần nữa” vẫn đều đều. Đề xuất: “Thưa ngài Gotama — ngài vừa nói gì vậy? Xin ngài nói
   lại lần nữa.” Dấu gạch ngang tạo chỗ ngắt, “thưa” thêm vẻ khúm núm; vẫn giữ nguyên nội
   dung. Không nên thêm “con sợ quá” hay “con chưa nghe rõ” vì Pali không có.
7. **1.15.6 và 1.16.10 — câu dòng dõi dài, nhiều tầng.** 1.16.10 là câu chốt của cả đoạn:
   “Như vậy đó, này Ambaṭṭha, khi nhớ lại tên họ và dòng dõi bên cha mẹ ông từ thuở xưa,
   thì dòng Sakya là con của các bậc chủ nhân, còn ông là con của một người nữ tỳ của dòng
   Sakya.” Câu đúng nhưng nặng vì “khi… thì…” chen giữa. Có thể thêm dấu hai chấm sau
   “Ambaṭṭha”: “Như vậy đó, này Ambaṭṭha: khi nhớ lại…, thì…”. Không nên tách thành hai câu
   vì đây là câu kết đòn, tách sẽ mất lực.
8. **1.15.10 — “khu rừng sāka” không được gloss trong chính văn.** Chú thích 1.15.10 giải
   thích sāka/sāla, nhưng người đọc phổ thông gặp “khu rừng sāka” lần đầu mà không có gì
   níu. Có thể viết “khu rừng sāka (sa-la)” ngay lần đầu, hoặc để nguyên và tin vào chú
   thích. Đây là lựa chọn biên tập, không phải lỗi.

### Hai lối chơi chữ saka / sāka

- `saka` (“của mình, của chính mình”) xuất hiện ở 1.14.1 (`sake kulāvake`), 1.14.2 (`sakaṁ
  Kapilavatthuṁ`), 1.15.11/15 (`sakāhi bhaginīhi`) và 1.15.17 (`sakyā ... paramasakyā`).
  Bản dịch giữ tiếng vang bằng “chính… của mình” ở 1.14.1 (đã sửa từ “của nó”), “nơi của
  chính dòng Sakya” ở 1.14.2, “chính các chị em gái của mình” ở 1.15.11/15. Chú thích
  1.15.11 và 1.15.17 giải thích pun. Đây là cách xử lý tốt: không cần Việt hóa tên, chỉ cần
  giữ chữ “của mình” và để chú thích nối vào tên Sakya.
- `sāka` (tên một loại cây, trong `mahāsākasaṇḍo`) ở 1.15.10 và 1.15.14 là lối chơi chữ trên
  tên Sakya. Bản dịch giữ nguyên “sāka”, không Việt hóa thành “sa-la” hay “sakhua”; chú
  thích 1.15.10 giải thích sāka/sāla và cây thực tế. Cách này trung thành với Pali, nhưng
  người đọc phổ thông không thấy được pun nếu không đọc chú thích. Có thể thêm gloss “(một
  loại cây, có lẽ là sa-la)” ngay lần đầu ở 1.15.10; đây là lựa chọn biên tập.
- `kaṇha` (“đen”) là tên của Kaṇha và cũng là nhãn miệt thị; bản dịch giữ tên “Kaṇha”,
  gloss “nghĩa là đen” ở 1.16.2, rồi dùng “kẻ đen” trong ngoặc ở 1.16.6. Đây là cách tốt
  nhất có thể trong tiếng Việt.
- `ayyaputta` (“con của các bậc chủ nhân”) và `ibbha` (“tiện dân”) đã có chú thích; xem
  bảng chú thích ở trên.

## Chú thích

Các chú thích trong ba tệp nhìn chung chính xác và có ích: chúng giải thích `ibbha`, `kaṇha`,
`ayyaputta`, `sāka`, `saka`, `Kaṇhāyana`, Vajirapāṇī. Nhưng nhiều chú thích quá dài so với
người đọc phổ thông, nhất là các chỗ dẫn kinh điển Sanskrit, sử thi và học giả mà không
ảnh hưởng đến việc hiểu chính văn. Dưới đây là các chỗ nên cắt; ba chỗ cần chỉnh trong chú
thích đã sửa trực tiếp (xem bảng lỗi nhẹ, mục 11).

| # | Tệp: đoạn | Hiện tại | Vấn đề | Đề xuất |
|---|---|---|---|---|
| 1 | 03:1.10.3 | Chú thích chỉ giải thích `kaṇha`, không giải thích `bandhupādāpacca`. | Thiếu chú thích cho lời miệt thị thứ tư; xem lỗi nặng số 3. | Thêm chú thích `bandhupādāpacca`; giữ chú thích `kaṇha` nhưng đổi “tràn vào” thành “di cư vào” cho bớt hình ảnh xâm lược. |
| 2 | 03:1.12.7 | Chú thích `ibbha` dài, có Chāndogya Upaniṣad 1.10 và Snp 3.1:18.4. | Phần từ nguyên “voi” và `hatthigopakā` rất hay, nhưng hai dẫn chứng Sanskrit/Pali không cần cho người đọc phổ thông. | Giữ câu đầu (ibbha = tiện dân, gốc “voi”, người giữ voi); cắt Chāndogya và Snp, hoặc chỉ giữ một câu “Pali cũng có chỗ gọi dân bản địa là niketino”. |
| 3 | 05:1.15.4 | Chú thích dài: Mahābhārata 7.4.5c, 7.132.23a; Arrian, Anabasis quyển VI chương 15; Manusmṛti 10.8; vị trí Sindh. | Đây là chú thích nặng nhất trong ba tệp: 5 dòng cho một dân tộc chỉ được nhắc một lần. Các dẫn chứng đã được sửa đúng, nhưng với người đọc phổ thông, chi tiết Manusmṛti về con lai bà-la-môn/phệ-xá không giúp hiểu vì sao Ambaṭṭha tự hào về dòng dõi. | Giữ 2 câu: “Người Ambaṭṭha là một dân tộc ở miền tây bắc Ấn Độ thời cổ, có lẽ là người Abastania mà Arrian ghi lại, sống ở vùng Sindh phía bắc Pakistan.” Cắt các số câu Mahābhārata và đoạn Manusmṛti; nếu giữ Manusmṛti thì chỉ một mệnh đề: “Văn bản sau này coi ambaṣṭha là con lai giữa bà-la-môn và phệ-xá.” |
| 4 | 05:1.15.5 | Chú thích Kaṇhāyana/Kāṇvāyana: Rig Veda 8.55.4, 1.117.8, “Kaṇva Đen”. | Giả thuyết học thuật, có thể đúng, nhưng không cần cho mạch truyện; người đọc chỉ cần biết Kaṇhāyana là dòng của Ambaṭṭha và nghĩa “hậu duệ của người đen”. | Rút còn: “Kaṇhāyana nghĩa là ‘hậu duệ của Kaṇha/người đen’; có lẽ đây là cách chơi chữ trên tên dòng Kāṇvāyana trong Rig Veda, nhưng truyền thống Phật giáo gắn nó với kaṇha.” Cắt các số câu. |
| 5 | 05:1.15.7 | Chú thích Okkāka = Ikṣvāku, con Manu, vương triều Mặt Trời; thuyết gốc Munda, mía `ikṣuḥ`, Jinasena thế kỷ 9, Natubhai Shah. | Phần xác định Okkāka = Ikṣvāku rất cần; phần từ nguyên Munda/mía và dẫn Jinasena/Shah là học thuật, không ảnh hưởng nghĩa. | Giữ: “Okkāka là Ikṣvāku trong truyền thống Bà-la-môn, con của Manu, người sáng lập vương triều Mặt Trời.” Cắt thuyết Munda, mía và dẫn Jinasena/Shah. |
| 6 | 05:1.15.10 | Chú thích sāka/sāla, so sánh Gilgamesh, MN 93, gợi ý dùng “sakhua”. | So sánh Gilgamesh và MN 93 lạc đề; chú thích gợi ý dùng “sakhua” nhưng chính văn giữ `sāka`, nên gợi ý ấy treo lơ lửng. | Giữ: “sāka và sāla dễ lẫn; cây thực tế có lẽ là sa-la (sāla), nhưng bản dịch giữ sāka để bảo toàn cách chơi chữ với tên Sakya.” Cắt Gilgamesh, MN 93; bỏ câu “có thể dùng sakhua” hoặc nói rõ “nếu muốn Việt hóa thì có thể dùng sa-la”. |
| 7 | 05:1.15.11 | Chú thích `saka` và bốn dẫn chứng `sambheda`: AN 2.9:1.5, DN 26:20.2, AN 5.103:6.4, AN 10.45:4.1. | Bốn dẫn chứng cho một từ không cần thiết; người đọc không tra được, và chúng không làm rõ thêm chuyện loạn luân. | Giữ câu đầu (saka = “của mình”, chơi chữ trên Sakya) và câu về loạn luân trong gia đình vương tộc; cắt bốn dẫn chứng `sambheda`. |
| 8 | 05:1.16.1 | Chú thích `dāsa`/`dviṣa`: Rig Veda 2.20.7, 10.22.8, 10.62.10; “sinh ra từ bào thai đen tối”. | Ba dẫn chứng cho một giả thuyết từ nguyên; với người đọc phổ thông, chúng chỉ làm nặng thêm. | Rút còn một câu: “Trong tiếng Vệ-đà, dāsa vừa có nghĩa ‘nô lệ, người hầu’, vừa dùng để chỉ kẻ thù; tên Disā có lẽ liên quan đến dviṣa (‘kẻ thù’).” Cắt ba số câu Rig Veda và chi tiết “bào thai đen tối”. |
| 9 | 05:1.16.2 | Chú thích Arthaśāstra 3.13: nữ nô tỳ được bảo vệ khỏi quấy rối, có con với chủ thì mẹ con được tự do, nếu không tự nguyện thì chủ nộp phạt. | Quá chi tiết pháp lý cho một đoạn kể chuyện; người đọc không cần biết chế tài. | Rút còn: “Theo Arthaśāstra, nữ nô tỳ có một số quyền bảo vệ; nếu sinh con với chủ thì mẹ con được tự do.” Cắt các mức phạt. |
| 10 | 05:1.17.2 | Chú thích: “Dòng dõi quan trọng… nhưng văn học Bà-la-môn và Upaniṣad cho thấy nhiều người, như ở đây, quan tâm đến hạnh kiểm và trí tuệ hơn là xuất thân.” | Chính văn 1.17.2–1.17.3 cho thấy các thanh niên ca ngợi dòng dõi, học vấn, ăn nói, thông minh — không phải hạnh kiểm. Chú thích nói “hạnh kiểm” là suy diễn quá xa. | Đổi “hạnh kiểm và trí tuệ” thành “học vấn và trí tuệ”, hoặc cắt chú thích vì không cần cho mạch truyện. |
| 11 | 05:1.20.3 | Chú thích Bṛhadāraṇyaka 1.3.24, 3.9.26; Rāmāyaṇa 7.26.44c; Mahābhārata 14.7.2c. | Ba dẫn chứng cho một lời đe dọa; chỉ cần một tương đương là đủ. “Nổ tung” đã sửa thành “vỡ tung”. | Giữ một câu: “Lời đe dọa làm đầu vỡ tung cũng xuất hiện trong Bṛhadāraṇyaka Upaniṣad và một số sử thi về sau.” Cắt các số câu cụ thể. |
| 12 | 05:1.21.1 | Chú thích Vajirapāṇī/Indra/Sakka, Rig Veda, “Đại thừa mượn tên này để gọi một vị Bồ-tát dữ dằn, là hộ pháp của Pháp.” | Phần xác định Vajirapāṇī = Indra/Sakka rất cần; phần Rig Veda và Đại thừa là mở rộng, không cần cho đoạn này. “Hộ pháp của Pháp” lặp nghĩa. | Giữ: “Vajirapāṇī (‘tay cầm tia chớp’) là một dạng của Indra/Sakka; hình ảnh này cũng có ở MN 35.” Cắt Rig Veda và câu Đại thừa; nếu giữ thì viết “một vị Bồ-tát dữ dằn, bảo vệ Chánh pháp.” |

Tóm lại về chú thích: **không có chú thích nào sai nghĩa nghiêm trọng** sau khi sửa ba chỗ
trong chú thích. Vấn đề là tỉ lệ: các chú thích 1.15.4, 1.15.7, 1.16.1, 1.20.3 và 1.21.1
dài gấp ba bốn lần thông tin cần thiết. Với người đọc phổ thông, một câu xác định + một
câu vì sao nó đáng chú ý là đủ; các số câu Sanskrit, tên học giả và niên đại nên để cho
người làm nghiên cứu.

## Kết luận

**CẦN SỬA.** Bản dịch bám Pali, giữ đúng thứ tự và đúng người nói; các câu công thức §5
đúng khuôn, chỉ có biến thể cần thiết ở 1.20.7 và 1.20.9; xưng hô đúng bảng §3; không có
từ cấm, không có ngoặc kép cong, không có dấu lược. Nhưng ba chỗ còn lại phải sửa trước khi
coi là ĐẠT:

1. **1.17.3, 1.18.3, 1.18.5, 1.19.1** — lặp lại `ambaṭṭho māṇavo` trước từng vị ngữ. Đây là
   lỗi nhịp lớn nhất của mục 2; không sửa thì bốn đoạn trọng tâm mất sức dồn.
2. **1.15.11, 1.15.15** — thay “chung sống” bằng “ăn nằm” (hoặc “lấy nhau”) để không làm nhẹ
   chuyện loạn luân.
3. **1.10.3** — thêm chú thích `bandhupādāpacca`; nếu không, lời miệt thị thứ tư trong danh
   sách vẫn là một cụm vô nghĩa.

Hai mươi nhóm lỗi nhẹ đã sửa trực tiếp; các đề xuất còn lại ở mục Chất văn và Chú thích là
tùy chọn biên tập, không bắt buộc. Sau khi sửa ba chỗ trên, phần 2.1–2.4 có thể đạt.

Kiểm tra marker sau khi sửa:

- `03-primitives-1.md`: 15/15 đoạn — `==> ĐẠT` (635 từ nội dung).
- `04-primitives-2-3.md`: 17/17 đoạn — `==> ĐẠT` (358 từ nội dung).
- `05-slavegirl.md`: 62/62 đoạn — `==> ĐẠT` (2209 từ nội dung).
