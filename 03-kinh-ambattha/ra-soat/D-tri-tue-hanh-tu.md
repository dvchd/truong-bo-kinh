# Rà soát D — mục 4 và 5

## Tóm tắt

Đã đối chiếu từng đoạn của `ban-dich/08-knowledge-conduct.md` (31 đoạn, dn3:2.1.0–2.2.23) và `ban-dich/09-four-causes.md` (44 đoạn, dn3:2.3.0–2.5.5) với `root_text` Pali trong `nguon/api_dn3.json`, đối chiếu chú thích với NOTE của Sujato trong `nguon/sections/`, và kiểm tra lại bằng `kiem-tra-marker.py`.

Kết quả hình thức: cả hai tệp đều `==> ĐẠT` (31/31 và 44/44 marker); không có ngoặc cong, không có dấu ba chấm, không dùng "Đức Phật", "ngươi", "mày". Các câu công thức bắt buộc của §5 có đủ số lần và đúng nguyên văn. Cách dùng cặp `vijjācaraṇa` cũng đạt: không có chỗ nào lẫn `vijjā`/`caraṇa` với hợp chất; 2.2.22 và 2.2.23 tách đúng hai thành phần.

Đã sửa trực tiếp 17 mục lỗi nhẹ (bảng dưới). Còn 5 lỗi nặng chưa thể tự sửa vì hoặc đụng đến thuật ngữ đã được `HUONG-DAN-DICH.md` quy định, hoặc đụng đến quyết định biên tập về cách khai triển peyyāla. Kết luận: **CẦN SỬA**.

## Lỗi nặng (phải sửa)

| # | Tệp | Đoạn | Hiện tại | Vấn đề | Đề xuất |
|---|---|---|---|---|---|
| 1 | `09-four-causes.md` | 2.3.0, 2.3.1, 2.3.6, 2.3.10, 2.3.13, 2.3.17, 2.3.18, 2.5.2, 2.5.4 | "Bốn căn nguyên đọa lạc"; "sự thành tựu ... này có bốn căn nguyên đọa lạc"; "căn nguyên đọa lạc thứ nhất của sự thành tựu..." | `apāyamukha` ở đây là lối mở để **rời bỏ** sự thành tựu khi không đạt được, tức bốn lối tu khổ hạnh thấp hơn. "Đọa lạc" trong tiếng Việt là rơi vào cảnh khổ, sa đọa; "căn nguyên đọa lạc" thành ra "nguyên nhân gây đọa lạc", ngược với nghĩa "rời bỏ". Câu "sự thành tựu ấy có bốn căn nguyên đọa lạc" còn đọc thành "sự thành tựu ấy gây ra bốn cái đọa lạc". Chính chú thích 2.3.1 nói "lối mở để rời bỏ", mâu thuẫn với thuật ngữ; `HUONG-DAN-DICH.md` §4.3 cũng ghi "bốn lý do khiến phải từ bỏ". | Đổi thuật ngữ thành **"bốn lối rời bỏ"** (tiêu đề `## 5. Bốn lối rời bỏ`). Nếu vẫn giữ "căn nguyên đọa lạc" theo hướng dẫn thì phải chú thích ngay lần đầu: "bốn căn nguyên đọa lạc — bốn lối rời bỏ sự thành tựu này", và sửa các câu kết thành "lối rời bỏ thứ nhất..." để không đọc thành "nguyên nhân gây đọa lạc". Cần sửa cả §4.3 và §6.2 của hướng dẫn; không tự đổi tiêu đề trong bản dịch. |
| 2 | `08-knowledge-conduct.md` | 2.2.7; 2.2.8, 2.2.10, 2.2.12, 2.2.14; 2.2.17; 2.2.18 | 2.2.7 tóm con đường tu tập trong 3 câu; bốn đoạn thiền chỉ có công thức thiền và câu "tỏa khắp"; 2.2.17 rút gọn ví dụ ngọc; 2.2.18 mỗi thắng trí chỉ một mệnh đề | Pali dùng `…pe…`; theo §1.5 phải khai triển đầy đủ. Bản dịch đang **tóm tắt**, không khai triển: thiếu bốn ví dụ thiền (bột tắm, hồ nước, hoa sen, vải trắng), thiếu mười loại thần thông, thiếu chi tiết thiên nhĩ, tha tâm, túc mạng, thiên nhãn; ví dụ ngọc thiếu "tám mặt" và các màu chỉ. Chú thích 2.2.7 chỉ nói về con đường tu tập, không nói gì về các ví dụ thiền và sáu thắng trí. Đây là thiếu nội dung so với Pali, không chỉ là văn phong. | (a) Khai triển đầy đủ từ DN 2, đúng §1.5: bốn ví dụ thiền, mười thần thông, chi tiết bốn thắng trí sau, ví dụ ngọc tám mặt. Hoặc (b) nếu chủ trương tóm tắt, ghi rõ ngay tại 2.2.8, 2.2.17, 2.2.18 "phần này được tóm lược; xem Kinh Sa-môn quả", và sửa §1.5 của hướng dẫn cho phép tóm tắt có kiểm chứng. Không nên để nửa vời như hiện tại. |
| 3 | `08` và `09` | 2.2.7, 2.2.8, 2.2.12, 2.2.17, 2.2.18; 2.5.4 | "năm triền cái", "thiền-na", "tầm", "tứ", "tâm xả", "có sắc", "bốn đại", "thắng trí", "lậu hoặc", "ba minh", "bà con chúng ta" — đều dùng lần đầu mà không giải thích | §1.3 yêu cầu thuật ngữ Phật học phải có gloss ngay lần đầu. Người đọc hiện đại không quen Phật học sẽ không theo được các đoạn cốt lõi 2.2.7–2.2.18; 2.5.4 gần như không hiểu nếu không biết Vệ-đà và thần thoại Phạm Thiên. Bảng thuật ngữ là tệp riêng, không được dẫn trong bài đọc. | Thêm gloss ngắn hoặc chú thích, không cần chen vào lời Phật. Gợi ý: "năm triền cái (tham dục, sân hận, hôn trầm–thụy miên, trạo cử–hối quá, nghi ngờ)"; "tầm (hướng tâm đến đối tượng), tứ (giữ tâm nơi đối tượng)"; "tâm xả (không thiên vị, không bám)"; "có sắc, do bốn đại (đất, nước, lửa, gió) hợp thành"; "lậu hoặc (những ô nhiễm sâu kín của tâm)"; "ba minh (ba bộ Vệ-đà)"; "bà con chúng ta (chỉ Phạm Thiên; bốn giai cấp sinh từ các phần thân của Ngài, giai cấp thấp nhất từ bàn chân)". |
| 4 | `09-four-causes.md` | 2.4.2, 2.4.4, 2.4.5, 2.4.7, 2.4.11, 2.4.15, 2.4.18, 2.5.1, 2.5.2 | "cùng với thầy của mình"; "nơi mình và nơi thầy của mình" | `sācariyaka` là "thuộc về truyền thống/tông phái của mình", không phải "ông cộng với thầy" như hai cá nhân. Chú thích 2.4.2 nói rõ nghĩa "denomination", nhưng bản chính vẫn dịch literal; 9 lần lặp làm lập luận 2.5.1–2.5.2 khó hiểu: đó là sự thiếu hụt của cả **truyền thống**, không phải chuyện riêng của Ambaṭṭha và Pokkharasāti. | Lần đầu dịch "cùng với truyền thống của mình" (chú thích: nghĩa đen "bắt nguồn từ thầy"); sau đó dùng "ông và truyền thống của ông". Nếu muốn giữ "thầy", phải thêm chú thích tại 2.4.2 và 2.5.2 rằng "thầy" đại diện cho cả truyền thống, không chỉ cá nhân. |
| 5 | `09-four-causes.md` | 2.5.1–2.5.2 | "đã thiếu hẳn sự thành tựu..."; "còn thiếu cả bốn căn nguyên đọa lạc của sự thành tựu... nữa" | `ceva ... ca` là "chẳng những ... mà còn". Ý của Pali: Ambaṭṭha **tệ hơn** bốn người thất bại — không có sự thành tựu, mà còn chưa làm nổi cả bốn lối tu dự phòng. Câu hiện tại đọc thành "thiếu cả bốn căn nguyên đọa lạc", nghe như thiếu cái xấu, nên mất hẳn sự mỉa mai. Đây là hệ quả của thuật ngữ ở mục 1, nhưng câu chữ cũng cần sửa. | "Này Ambaṭṭha, như vậy là ông cùng với truyền thống của mình chẳng những không có sự thành tựu trí tuệ và hạnh tu tối thượng này, mà còn chưa đạt tới cả bốn lối rời bỏ ấy nữa." Nếu giữ thuật ngữ cũ, ít nhất đổi "thiếu" thành "chưa đạt tới" và thêm "ấy" để câu bớt ngược nghĩa. |

### Chi tiết lỗi nặng

#### 1. `apāyamukha` — thuật ngữ và chú thích đang đánh nhau

Pali 2.3.1: `Imāya ... anuttarāya vijjācaraṇasampadāya cattāri apāyamukhāni bhavanti.` Nghĩa: "Đối với sự thành tựu trí tuệ và hạnh tu tối thượng này, có bốn lối mở để rời bỏ." Bốn lối ấy là bốn cách tu khổ hạnh thấp hơn mà một người chọn khi không đạt được sự thành tựu: sống bằng quả rụng, đào củ rễ, hầu lửa, dựng nhà bốn cửa ở ngã tư. Không phải bốn việc ác, cũng không phải bốn nguyên nhân khiến người ta bị đọa.

Chú thích 2.3.1 đã nói đúng: "lối mở để rời bỏ sự thành tựu ấy". Nhưng câu chính lại là "có bốn căn nguyên đọa lạc". "Căn nguyên đọa lạc" là "nguyên nhân của sự sa đọa"; đặt sau "sự thành tựu... có" thì thành ra sự thành tựu ấy sinh ra bốn cái đọa lạc. Các câu kết "căn nguyên đọa lạc thứ nhất **của** sự thành tựu" càng làm người đọc hiểu sai quan hệ sở hữu. Đây là lỗi nghĩa, không phải lỗi chữ.

`HUONG-DAN-DICH.md` §4.3 ghi: `cattāro apāyamukhāni` → "bốn lý do khiến phải từ bỏ" → "bốn căn nguyên đọa lạc". Chính dòng đầu của hướng dẫn đã đúng hơn dòng sau. Đề nghị cấp trên sửa §4.3 và §6.2 thành "bốn lối rời bỏ" (hoặc "bốn lối từ bỏ"), rồi thống nhất toàn bộ 9 chỗ trong tệp 09. Nếu chưa muốn đổi thuật ngữ, bắt buộc phải chua ngay tại 2.3.1 và sửa lại các câu kết để "đọa lạc" không còn đứng ở vị trí "của sự thành tựu".

#### 2. Peyyāla đang được tóm tắt, không được khai triển

Đây là lỗi nặng nhất về nội dung. Bốn vị trí:

| Đoạn | Pali | Bản dịch hiện có | Thiếu |
|---|---|---|---|
| 2.2.7 | `…pe…` sau `paṭisañcikkhati` | 3 câu tóm tắt: xuất gia, tu giới–căn–niệm–biết đủ, tìm chỗ vắng, bỏ năm triền cái | Toàn bộ chi tiết của con đường tu tập tuần tự trong DN 2, kể cả các ví dụ và năm triền cái từng cái |
| 2.2.8, 2.2.10, 2.2.12, 2.2.14 | `…pe…` sau mỗi công thức thiền | Công thức thiền + câu "thấm đẫm, tỏa khắp" | Bốn ví dụ: bột tắm thơm, hồ nước mát, hoa sen trong bùn, tấm vải trắng |
| 2.2.17 | `…pe…` sau "hướng tâm đến tri kiến" | Thân do bốn đại + ví dụ ngọc lưu ly rút gọn | "Tám mặt", "khéo mài", "không tì vết", "đủ mọi phẩm chất", các màu chỉ (xanh, vàng, đỏ, trắng, nâu) |
| 2.2.18 | `…pe…` sau `idampissa hoti vijjāya` | Mỗi thắng trí một mệnh đề | Mười loại thần thông; chi tiết thiên nhĩ (xa gần), tha tâm (có tham/không tham...), túc mạng (một đời, hai đời... nhiều kiếp), thiên nhãn (chúng sinh theo nghiệp, các cõi) |

Chú thích 2.2.7 có nói "bản Pali lược bỏ phần trình bày tuần tự... người đọc được giả định đã biết đoạn ấy như trong Kinh Sa-môn quả". Nhưng chú thích ấy chỉ đặt ở 2.2.7, không đặt ở 2.2.8, 2.2.17, 2.2.18; người đọc không biết rằng các ví dụ thiền và sáu thắng trí cũng đang bị tóm. Hơn nữa, §1.5 của hướng dẫn nói peyyāla **phải khai triển đầy đủ**, không nói "được phép tóm tắt".

Đề xuất: hoặc khai triển đầy đủ (tốt nhất, đúng hướng dẫn), hoặc nếu giữ tóm tắt thì phải (a) thêm chú thích tại từng chỗ, (b) ghi rõ trong báo cáo chung rằng DN 3 được dịch theo lối tóm lược có chủ ý, và (c) sửa §1.5 của hướng dẫn. Hiện tại đang là giải pháp nửa vời: tóm tắt nhưng không nói đủ là đã tóm tắt.

#### 3. Thuật ngữ chưa được giải thích ở lần đầu

Các chỗ nặng nhất:

- 2.2.7: "năm triền cái" — không nói năm cái là gì. Đây là đoạn chuyển từ giới hạnh sang thiền; không hiểu triền cái thì không hiểu vì sao tâm được "làm cho trong sạch".
- 2.2.8: "thiền-na", "tầm", "tứ" — ba thuật ngữ chống đỡ toàn bộ bốn đoạn thiền. "Thiền-na" có thể quen với người Phật tử, nhưng "tầm", "tứ" thì gần như không.
- 2.2.12: "tâm xả" — không giải thích; người đọc dễ hiểu "xả" là buông bỏ, trong khi ở đây là tâm bình đẳng, không thiên vị.
- 2.2.17: "có sắc", "bốn đại" — "có sắc" là cách nói của người biết giáo lý; người thường sẽ hiểu "sắc" là màu.
- 2.2.18: "thắng trí", "lậu hoặc" — "thắng trí" xuất hiện từ 2.2.3 nhưng không bao giờ được giải thích; "lậu hoặc" là trung tâm của đoạn giác ngộ.
- 2.5.4: "thông ba minh", "bà con chúng ta" — hai chỗ này gần như không thể hiểu nếu không có chú thích. "Ba minh" ở đây là ba bộ Vệ-đà của người bà-la-môn, không phải ba minh của Phật. "Bà con chúng ta" là Phạm Thiên, vị tổ trong thần thoại bà-la-môn.

Đề xuất gloss cụ thể đã ghi ở bảng. Nên đặt thành chú thích `[Chú thích: ...]` sau đoạn, không chen vào lời Phật, để giữ giọng văn.

#### 4. `sācariyaka` — "thầy" hay "truyền thống"?

Chú thích 2.4.2 viết: `sācariyaka` nghĩa đen là "cái bắt nguồn từ vị thầy của mình", là cách nói chỉ phe phái, truyền thống tôn giáo hay triết học riêng. Nhưng bản chính lại dịch "cùng với thầy của mình" ở 9 chỗ. Hệ quả:

- 2.4.2: "Ông có thấy sự thành tựu... nơi mình và nơi thầy của mình không?" — nghe như hỏi hai cá nhân.
- 2.5.1–2.5.2: "ông cùng với thầy của mình đã thiếu hẳn... còn thiếu cả..." — nghe như lỗi riêng của Ambaṭṭha và Pokkharasāti, trong khi Pali nói cả truyền thống của họ không có sự thành tựu và cũng không làm nổi bốn lối tu dự phòng.
- 2.5.3–2.5.4: lời của Pokkharasāti được đặt trong mối quan hệ thầy–trò, nhưng lập luận của Phật là về **phe phái** của ông ta.

Đề xuất: lần đầu dùng "cùng với truyền thống của mình" (hoặc "cả phe phái của mình"), chú thích nghĩa đen; các lần sau dùng "ông và truyền thống của ông". Nếu giữ "thầy" cho sát chữ, phải nói rõ trong chú thích rằng "thầy" ở đây đại diện cho truyền thống, không chỉ cá nhân.

#### 5. 2.5.1–2.5.2 — mất sự leo thang

Pali: `imāya ceva ... parihīno sācariyako. Ye cime ... cattāri apāyamukhāni bhavanti, tato ca tvaṁ parihīno sācariyako.` Chữ `ceva ... ca` là "chẳng những ... mà còn". Ý: ông không có sự thành tựu, mà còn kém cả bốn người đã thất bại và phải rời bỏ. Bản dịch hiện tại dùng "đã thiếu hẳn" và "còn thiếu cả ... nữa", đúng hướng, nhưng vì "căn nguyên đọa lạc" nghe như "nguyên nhân gây đọa lạc" nên câu "thiếu cả bốn căn nguyên đọa lạc" thành ra vô lý. Khi sửa thuật ngữ thành "lối rời bỏ", câu sẽ rõ; nên sửa thêm "thiếu" → "chưa đạt tới" cho khỏi hiểu là "thiếu cái xấu".

## Lỗi nhẹ (đã sửa trực tiếp)

| # | Tệp | Đoạn | Đã sửa thành | Lý do |
|---|---|---|---|---|
| 1 | `08-knowledge-conduct.md` | 2.1.1 (chú thích) | "Ambaṭṭha thật đáng khen: sau phen bị bẽ mặt hoàn toàn ấy..." | "Đáng khen cho Ambaṭṭha" không phải cách nói tiếng Việt tự nhiên. |
| 2 | `08-knowledge-conduct.md` | 2.1.2 (chú thích) | "...khớp với chữ "ở đâu" (yattha) ở đoạn 2.1.4." | `yattha` nằm ở 2.1.4, không phải "đoạn kế tiếp"; câu chú thích cũng được viết lại cho dễ hiểu. |
| 3 | `08-knowledge-conduct.md` | 2.2.2 | "bậc Ứng Cúng, Chánh Đẳng Giác... bậc vô thượng... điều phục... chư thiên và loài người" | Cùng một công thức mười danh hiệu như 1.2.5 và 1.4.4; bản cũ dùng "A-la-hán / Chánh đẳng giác / tối thượng / giáo hóa / trời và người", không đồng bộ với 01 và 02. |
| 4 | `08-knowledge-conduct.md` | 2.2.3 | "thế giới này — có chư thiên, Ma vương, Phạm Thiên, có dân chúng cùng hàng sa-môn và bà-la-môn..." | Câu cũ đặt "thế gian ấy có..." sau "loan báo cho... biết", làm thế gian thành khán giả thay vì đối tượng được chứng ngộ; đồng thời thiếu `pajaṁ` ("dân chúng"). Nay khớp với 01/02. |
| 5 | `08-knowledge-conduct.md` | 2.2.7 | Tách thành 3 câu: "...không nhà. Người ấy tu tập... biết đủ. Sau đó, người ấy tìm đến..." | Câu cũ dài 7 mệnh đề nối bằng dấu phẩy và chấm phẩy, phải đọc lại. |
| 6 | `08-knowledge-conduct.md` | 2.2.7 (chú thích) | "...trong kinh này cũng như các kinh tiếp theo..." | Sujato viết "in this sutta and those that follow"; bản cũ bỏ mất "this sutta". |
| 7 | `08-knowledge-conduct.md` | 2.2.12 | "mà các bậc thánh nói đến" | Bỏ "vẫn": Pali `ācikkhanti` không có nghĩa "vẫn còn nói". |
| 8 | `08-knowledge-conduct.md` | 2.2.14 | "Vị ấy ngồi tỏa khắp thân này..." | Bỏ dấu phẩy sau "ngồi"; `pharitvā nisinno hoti` là một hành động "ngồi tỏa khắp", không phải hai hành động liên tiếp. |
| 9 | `08-knowledge-conduct.md` | 2.2.18 | "thi triển các loại thần thông" | `paccanubhoti` là "thi triển, thể nghiệm", không phải "thực hành" như một bài tập. |
| 10 | `09-four-causes.md` | 2.3.1 (chú thích) | "...là lối mở để rời bỏ sự thành tựu ấy." | Bản cũ "rời bỏ" không có tân ngữ, tối nghĩa; thêm "sự thành tựu ấy" để nối với câu chính. |
| 11 | `09-four-causes.md` | 2.3.11 (chú thích) | Chỉ còn: "Nhà lửa... Đức Thế Tôn có lúc cũng trú trong những nhà ấy (Trung Bộ 75; Luật tạng, Đại phẩm 1:15.2.2)." | Bỏ hai câu về Satapatha Brāhmaṇa và Arthaśāstra: quá hàn lâm, không giúp người đọc hiểu đoạn kinh. |
| 12 | `09-four-causes.md` | 2.4.2 | "Ông có thấy sự thành tựu trí tuệ và hạnh tu tối thượng này nơi mình và nơi thầy của mình không?" | Câu cũ "Ông có thấy nơi mình, cùng với thầy của mình, sự thành tựu..." là calque, đọc gãy. Chú thích 2.4.2 được cập nhật theo câu mới. |
| 13 | `09-four-causes.md` | 2.4.4 | "Thưa ngài Gotama, so với sự thành tựu..., tôi cùng với thầy của tôi đáng kể gì?" | Đưa "so với" lên trước, bỏ lối nói treo "đáng kể gì, so với..." ở cuối câu. |
| 14 | `09-four-causes.md` | 2.4.7, 2.4.11, 2.4.15, 2.4.18 | "Phải chăng vì không đạt được..., ông cùng với thầy của mình đã...?" | Pali `api nu` là câu hỏi tu từ ("phải chăng"), không phải câu điều kiện "Vì... ông có...?". Bản cũ đọc thành câu khẳng định có đuôi hỏi. |
| 15 | `09-four-causes.md` | 2.5.3 | "Này Ambaṭṭha, nhưng lời này do thầy của ông, bà-la-môn Pokkharasāti, nói ra:" | Bỏ "là ... đã" thừa trong "lời này là do... đã nói ra". |
| 16 | `09-four-causes.md` | 2.5.4 | "những sa-môn hèn mọn" | `samaṇakā` là dạng giảm nhẹ mang tính khinh miệt ("mấy ông sa-môn con con"), không phải "giả hiệu" (hàng giả). "Giả hiệu" thêm nghĩa không có trong Pali. |
| 17 | `09-four-causes.md` | 2.5.4 | "chúng là gì, mà bàn chuyện với các bà-la-môn thông ba minh?" | Bỏ lối "chuyện đàm đạo với... là gì?" vừa trùng "là gì" vừa quá trang trọng; câu mới sắc hơn và vẫn giữ ý khinh miệt. |

## Bảng câu công thức

| Câu | Số lần phải có | Số lần đúng | Chỗ lệch |
|---|---|---|---|
| "Và điều này cũng thuộc về hạnh tu của vị ấy." | 4 | 4 | Không. Có đủ ở 2.2.9, 2.2.11, 2.2.13, 2.2.15. |
| "Và điều này cũng thuộc về trí tuệ của vị ấy." | 2 | 2 | Không. Có đủ ở 2.2.18, 2.2.20. |
| "Nhưng người ấy rốt cuộc chỉ trở thành kẻ hầu hạ cho người có đủ trí tuệ và hạnh tu." | 4 | 4 | Không. Có đủ ở 2.3.5, 2.3.9, 2.3.12, 2.3.16. |
| "Ambaṭṭha, ông nghĩ thế nào" | 14 (toàn kinh) | 5 trong `09`; 0 trong `08` | Trong `09`: 5/5 đúng nguyên văn (2.4.1, 2.4.6, 2.4.10, 2.4.14, 2.4.17). Toàn kinh: 14/14 về chữ. `05` và `07` thêm dấu "?" (ngoài phạm vi); `10` không có dấu như `09`. Câu bị ngắt theo marker nên không có dấu cuối — đúng §5 nhưng dễ bị đọc thành lỗi. |
| "Rồi Đức Thế Tôn nghĩ như thế này:" | 4 (toàn kinh) | 0 trong 2 tệp | Không có trong mục 4–5; 4 lần nằm ở các tệp khác (`05`, `06`, `11`, `12`). |
| "Rồi thanh niên Ambaṭṭha nghĩ như thế này:" / "Rồi bà-la-môn Pokkharasāti nghĩ như thế này:" | 1 + 1 | 0 | Không có trong 2 tệp. |
| "Rồi Đức Thế Tôn nói với thanh niên Ambaṭṭha:" | 4 | 0 | Không có trong 2 tệp. |
| Các câu còn lại của §5 ("Nghe nói...", "Thưa ngài Gotama, đúng vậy", "Khi nghe vậy... im lặng", "Lành thay, lành thay") | 4, 4, nhiều, 2 | 0 | Không có trong 2 tệp; không có gì để đối chiếu. |

Ghi chú:

- `vijjācaraṇa` nhất quán: 08 dùng "trí tuệ và hạnh tu" cho hợp chất, "trí tuệ" cho `vijjā`, "hạnh tu" cho `caraṇa`; 2.2.22 tách đúng ba danh hiệu; 2.2.23 dùng "sự thành tựu trí tuệ và thành tựu hạnh tu" đúng vì Pali có hai chữ `sampadā`.
- Mười danh hiệu ở 2.2.2 đã được đồng bộ với 1.2.5 và 1.4.4 trong lần sửa này. Riêng 2.2.4 vẫn còn khác 01/02: "có ý nghĩa và lời lẽ khéo léo" so với "có ý nghĩa và văn cú". Đây là lựa chọn văn phong, không phải lỗi nghĩa, nhưng nên thống nhất một cách dịch cho `sātthaṁ sabyañjanaṁ`.
- Các câu công thức của §5 không xuất hiện trong hai tệp này không phải là thiếu sót của hai tệp; chúng thuộc các mục khác của kinh. Bảng ghi "0" để tránh hiểu nhầm là đã đối chiếu.

## Bốn căn nguyên đọa lạc — kiểm tra cấu trúc

### 1. Từng căn nguyên

| # | Câu mở | Nội dung | Câu kết | Đánh giá |
|---|---|---|---|---|
| 1 | 2.3.3: "Này Ambaṭṭha, ở đây có một sa-môn hay bà-la-môn nào đó, không đạt được sự thành tựu... bèn mang theo đòn gánh và giỏ, đi sâu vào một vùng rừng vắng:" | 2.3.4: "Ta sẽ sống bằng quả rụng." | 2.3.5 (câu `paricāraka`) + 2.3.6 ("căn nguyên... thứ nhất") | Đủ. |
| 2 | 2.3.7: "Lại nữa... không đạt được..., cũng không đạt được cách sống bằng quả rụng, bèn mang theo cuốc và giỏ..." | 2.3.8: "Ta sẽ sống bằng củ, rễ và quả." | 2.3.9 + 2.3.10 ("thứ hai") | Đủ. |
| 3 | 2.3.11: "Lại nữa... không đạt được..., bèn dựng một nhà lửa ở ven làng hay ven thị trấn, rồi sống ở đó hầu hạ ngọn lửa." | Nội dung nằm ngay trong câu mở; Pali không có lời nguyện riêng | 2.3.12 + 2.3.13 ("thứ ba") | Đủ và đúng Pali. Đừng thêm lời nguyện cho đủ bộ; Pali không có. |
| 4 | 2.3.14: "Lại nữa... không đạt được..., cũng không đạt được việc hầu hạ ngọn lửa, bèn dựng một ngôi nhà có bốn cửa ở ngã tư đường, rồi sống ở đó:" | 2.3.15: "Vị sa-môn hay bà-la-môn nào từ bốn phương này đi đến, ta sẽ cúng dường..." | 2.3.16 + 2.3.17 ("thứ tư") | Đủ. |
| Tổng | 2.3.18: "Này Ambaṭṭha, đó là bốn căn nguyên đọa lạc của sự thành tựu..." | — | — | Đủ về cấu trúc; còn lỗi thuật ngữ ở mục 1. |

### 2. Chuỗi tích lũy — bốn lần có phân biệt được không?

Có. Bản dịch giữ đúng chuỗi "không đạt được" cộng dồn:

| Lần | Đoạn | "Không đạt được" | Bổ sung so với lần trước |
|---|---|---|---|
| 1 | 2.3.3 | sự thành tựu trí tuệ và hạnh tu | — |
| 2 | 2.3.7 | sự thành tựu + cách sống bằng quả rụng | + quả rụng |
| 3 | 2.3.11 | sự thành tựu + quả rụng + củ, rễ, quả | + củ, rễ, quả |
| 4 | 2.3.14 | sự thành tựu + quả rụng + củ, rễ, quả + hầu hạ lửa | + hầu hạ lửa |

Mỗi lần còn có câu kết riêng ("thứ nhất", "thứ hai", "thứ ba", "thứ tư") và cùng câu `paricāraka`. Như vậy bốn căn nguyên không bị lẫn vào nhau. Đây là điểm đạt.

### 3. Về "chuỗi bốn lần khoe có trí tuệ và hạnh tu"

Tôi đã dò toàn bộ 437 đoạn của `nguon/api_dn3.json`: **không có** cụm `catūhi ṭhānehi ... vijjācaraṇaṁ ... anussāveyya` ("xưng bừa về trí tuệ và hạnh tu") trong DN 3. Vì vậy, nếu hướng dẫn hoặc yêu cầu rà soát chờ đợi một chuỗi bốn lần "khoe có trí tuệ và hạnh tu", chuỗi ấy không nằm trong kinh này. Trong mục 5 chỉ có:

- chuỗi bốn lần "không đạt được" (bảng trên), và
- chuỗi bốn câu hỏi ở 2.4.7, 2.4.11, 2.4.15, 2.4.18 (đã sửa cấu trúc "Phải chăng...").

Cả hai chuỗi đều đã được phân biệt. Không nên tạo thêm một chuỗi "khoe" không có trong Pali.

### 4. Nhận xét về câu mở và câu kết

- Bốn câu mở đều bắt đầu bằng "Này Ambaṭṭha" hoặc "Lại nữa, này Ambaṭṭha", đủ để người đọc nhận ra từng căn nguyên.
- Câu kết nào cũng có công thức `paricāraka` + câu đánh số. Đúng.
- Điểm yếu duy nhất là thuật ngữ "đọa lạc" ở câu mở và câu kết, đã nêu ở mục 1. Nó làm người đọc tưởng bốn căn nguyên là bốn việc ác, trong khi chúng là bốn lối tu khổ hạnh thấp hơn. Chú thích 2.3.1 sửa được phần nào, nhưng không sửa được ấn tượng ban đầu.

## Chất văn — chỗ cần viết lại

1. **2.1.2 — câu mở trừu tượng.** "Trong sự thành tựu trí tuệ và hạnh tu tối thượng, người ta không nói đến chuyện giai cấp..." Người đọc phải hiểu ngầm "khi nói đến". Đề xuất: "Khi nói đến sự thành tựu trí tuệ và hạnh tu tối thượng, người ta không nói đến chuyện giai cấp, không nói đến chuyện dòng dõi, không nói đến chuyện kiêu căng:" — rõ hơn mà vẫn đúng locative.

2. **2.1.3 và 2.1.5 — "Người này" thay cho `tvaṁ`.** Pali là lời nói trực tiếp "you are worthy / not worthy of me"; bản dịch chuyển thành ngôi thứ ba "Người này xứng với tôi". Trong ngữ cảnh dạm hỏi, cách nói ấy không sai, nhưng nó làm mất tính trực tiếp và có thể gây hiểu là người thứ ba. Nếu muốn giữ trung tính, có thể dùng "Bạn xứng với tôi" hoặc thêm chú thích "lời người ta nói khi dạm hỏi". Đây là lựa chọn có chủ ý, tôi không tự sửa.

3. **2.2.4 — `sātthaṁ sabyañjanaṁ`.** "Có ý nghĩa và lời lẽ khéo léo" dễ hiểu nhưng là diễn giải; 01/02 dùng "có ý nghĩa và văn cú". Nên chọn một cách dịch thống nhất cho công thức này. "Văn cú" chính xác hơn với `sabyañjana`; "lời lẽ khéo léo" thân thiện hơn với người đọc mới. Nếu giữ "lời lẽ khéo léo", nên ghi rõ đây là cách diễn đạt, không phải nghĩa đen.

4. **2.2.7 — "từ bỏ gia đình".** Chính xác với `agārasmā anagāriyaṁ pabbajati`, nhưng người đọc hiện đại có thể hiểu là bỏ mặc gia đình. Có thể dùng "rời bỏ nhà cửa, sống đời không nhà" để giữ nghĩa xuất gia mà bớt cảm giác ruồng bỏ. Không bắt buộc.

5. **2.2.17 — "có sắc", "bốn đại".** Đây là chỗ khó nhất cho người không quen giáo lý. Nên thêm gloss: "Thân này của ta là vật chất (có sắc), do bốn đại — đất, nước, lửa, gió — hợp thành..." Hoặc chú thích ngắn. Câu "do cha mẹ sinh ra, được nuôi dưỡng bằng cơm cháo" đã rất rõ, chỉ cần mở hai thuật ngữ đầu.

6. **2.2.18 — đoạn quá dày.** Một đoạn 969 ký tự nhồi sáu thắng trí, bốn chân lý về khổ, bốn chân lý về lậu hoặc và sự giải thoát. Nên tách thành các câu ngắn hơn, mỗi thắng trí một câu, và thêm gloss "thắng trí", "lậu hoặc". Việc tách câu không làm mất nội dung; ngược lại giúp người đọc theo được tiến trình.

7. **2.4.1, 2.4.6, 2.4.10, 2.4.14, 2.4.17 — không có dấu cuối.** "Ambaṭṭha, ông nghĩ thế nào" đứng cuối đoạn mà không có dấu hỏi, vì câu tiếp tục ở đoạn sau. Đây là hệ quả của cách chia marker, và §5 quy định đúng nguyên văn không có "?". Nhưng người đọc dễ tưởng lỗi đánh máy. Đề xuất sửa hướng dẫn: cho phép thêm "?" hoặc dấu hai chấm ở cuối đoạn, hoặc ghi chú rằng câu tiếp tục. Không nên tự thêm "?" vào bản dịch khi §5 đang quy định khác.

8. **2.4.7, 2.4.11, 2.4.15, 2.4.18 — câu hỏi dài.** Sau khi sửa thành "Phải chăng vì...", câu vẫn dài 50–60 chữ vì phải kể hết các lần thất bại trước đó. Có thể tách thành hai câu: "Ông không đạt được sự thành tựu... này. Vậy có phải ông cùng với thầy của mình đã...?" Nhưng Pali là một câu; tách sẽ làm mất nhịp điệu truy vấn. Hiện tại đọc được; chỉ nên tách nếu ưu tiên tốc độ đọc hơn nhịp văn.

9. **2.5.4 — "thông ba minh", "bà con chúng ta".** Đây là hai chỗ tối nghĩa nhất trong toàn bộ hai tệp. Cần chú thích, không chỉ gloss một chữ. Gợi ý: "Ba minh (tevijjā) ở đây là ba bộ Vệ-đà mà người bà-la-môn phải thuộc. 'Bà con chúng ta' là Phạm Thiên; theo thần thoại bà-la-môn, bốn giai cấp sinh ra từ các phần thân của Ngài, giai cấp thấp nhất từ bàn chân." Câu "chúng là gì, mà bàn chuyện với..." sau khi sửa đã tự nhiên hơn, nhưng vẫn cần hai gloss này mới hiểu được.

10. **2.3.1 và 2.5.1–2.5.2 — thuật ngữ "đọa lạc".** Đã nêu ở lỗi nặng 1 và 5. Đây là chỗ cần quyết định ở cấp hướng dẫn, không phải sửa lẻ trong tệp.

11. **Lặp "sự thành tựu trí tuệ và hạnh tu tối thượng" 23 lần** (4 lần trong 08, 19 lần trong 09). Sự lặp là có chủ ý trong Pali, tạo nhịp và nhấn mạnh; không nên xóa hết. Nhưng ở các câu không phải công thức, có thể dùng "sự thành tựu ấy" sau lần đầu để bớt nặng. Ví dụ 2.3.7: "...không đạt được sự thành tựu ấy, cũng không đạt được cách sống bằng quả rụng..." — vẫn rõ vì tiền ngữ đã có.

12. **Chú thích.** Các chú thích hiện có đều đúng nghĩa so với NOTE của Sujato; không có chú thích sai. Nhưng:
    - 2.1.2 vẫn còn hơi kỹ thuật ("locative", "yattha"); đã sửa một phần, có thể nói đơn giản hơn nữa.
    - 2.3.5 dùng "chỉ giỏi phục dịch" — hơi khẩu ngữ so với phần còn lại; có thể đổi "rốt cuộc chỉ làm người phục dịch".
    - 2.3.11 sau khi cắt đã gọn; đây là ví dụ tốt cho các chú thích khác.
    - 2.4.2 đã khớp với câu mới; nhưng nếu đổi `sācariyaka` thành "truyền thống" thì phải viết lại chú thích này.
    - Thiếu chú thích ở 2.5.4 (ba minh, bà con) và ở 2.2.8 (thiền-na, tầm, tứ), 2.2.18 (thắng trí, lậu hoặc).

## Kết luận

**CẦN SỬA.**

Hình thức đã đạt: đủ marker, đúng thứ tự, không lặp, không có ký tự cấm, các câu công thức §5 đủ số lần và đúng chữ. Nhưng ba vấn đề quyết định vẫn còn:

1. **Thuật ngữ `apāyamukha` bị dịch ngược nghĩa** — "căn nguyên đọa lạc" thay vì "lối rời bỏ". Đây là lỗi nghĩa, ảnh hưởng đến cả mục 5 và kết luận của Đức Thế Tôn ở 2.5.1–2.5.2. Cần sửa ở cấp hướng dẫn trước, rồi sửa đồng loạt 9 chỗ trong tệp 09.
2. **Peyyāla bị tóm tắt thay vì khai triển** — thiếu bốn ví dụ thiền, mười thần thông, chi tiết bốn thắng trí, ví dụ ngọc tám mặt. Cần quyết định: khai triển đầy đủ, hoặc chấp nhận tóm tắt và ghi rõ ở từng chỗ + sửa §1.5.
3. **Thuật ngữ cốt lõi không được giải thích** — "triền cái", "tầm", "tứ", "xả", "sắc", "bốn đại", "thắng trí", "lậu hoặc", "ba minh", "bà con". Với người đọc không quen Phật học, các đoạn 2.2.7–2.2.18 và 2.5.4 hiện chưa dùng được.

Ngoài ra, `sācariyaka` cần được dịch theo nghĩa "truyền thống" hoặc phải chú thích rõ ở mọi chỗ; nếu không, lập luận của mục 5 sẽ bị hiểu thành chuyện riêng của hai cá nhân. Hai lỗi còn lại (cách dịch `sācariyaka` và câu 2.5.1–2.5.2) gắn với hai điểm đầu: khi sửa thuật ngữ và cách dịch `sācariyaka`, phải sửa lại hai chỗ ấy cho khớp.

Sau khi sửa ba điểm trên, cần chạy lại `kiem-tra-marker.py` cho cả hai tệp và đọc lại toàn bộ 2.5.1–2.5.4 để kiểm tra mạch lập luận.
