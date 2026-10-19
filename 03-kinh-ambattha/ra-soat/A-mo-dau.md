# Rà soát A — mục 1–2 và lời giới thiệu

> **Ghi chú phiên bản (08:58).** Báo cáo này rà soát bản `00-gioi-thieu.md` **160 dòng** đọc lúc 08:47.
> Trong lúc tôi viết báo cáo, tệp đã được sửa hai lần (181 dòng lúc 08:53:35; 183 dòng lúc 08:54:22);
> bản mới nhất có md5 `a7cc57a19ced2d8867ede05757971212`. **Cả 14 lỗi nặng ở mục dưới đã được khắc phục trong bản
> 183 dòng** — tôi đã kiểm tra lại từng điểm. Các bảng giữ nguyên để làm hồ sơ đối chiếu, không phải
> danh sách việc còn phải làm. Phần dịch 1–2 (`01-opening.md`, `02-ambattha.md`) không bị người khác
> sửa trong lúc rà soát.

## Tóm tắt

Phạm vi: `ban-dich/00-title.md`, `ban-dich/00-gioi-thieu.md`, `ban-dich/01-opening.md`
(dn3:1.1.1–1.2.8, 12 đoạn) và `ban-dich/02-ambattha.md` (dn3:1.3.0–1.9.5, 39 đoạn).
Đối chiếu `root_text` và `translation_text` trong `nguon/api_dn3.json`, các tệp
`nguon/sections/01-opening.md` và `02-ambattha.md`; dùng thêm các mục 2.1–2.9 để kiểm
chứng lời giới thiệu.

Kết quả chính:

- **Bản dịch 1–2: không có lỗi dịch nghĩa nặng.** Bám Pali, giữ đúng giọng, xưng hô đúng
  bảng §3; 12 nhóm lỗi nhẹ đã sửa trực tiếp. `00-title.md`, `01-opening.md` và `02-ambattha.md` đều `==> ĐẠT` sau khi sửa.
- **Lời giới thiệu: bản đầu 160 dòng có 14 lỗi nặng**, trong đó hai lỗi hệ thống: (a) tư thế
  và phản ứng của Ambaṭṭha ở 1.9 bị mô tả ngược; (b) số lần im lặng và vị trí Vajirapāṇī ở 2.4
  bị đếm sai (hai lần im lặng thành ba, câu hỏi thứ ba thành "lần thứ tư"). **Bản hiện tại
  183 dòng đã sửa cả 14**; còn 4 điểm nhỏ về giọng.
- **Kết luận: ĐẠT** (bản hiện tại) — bản đầu cần sửa, bản hiện tại đã đạt; 4 điểm nhỏ không
  chặn phát hành.

Ghi chú về `00-title.md`: 2 marker, 86 từ, `==> ĐẠT`; chỉ có một điểm nhỏ là "nhân vật
chính" (Ambaṭṭha vắng mặt ở mục 8–9), không đáng sửa.

## Lỗi nặng (phải sửa)

Không còn lỗi nặng trong bản hiện tại. Toàn bộ 14 lỗi nặng nằm ở bản đầu (160 dòng);
bảng dưới là hồ sơ đối chiếu, không phải việc còn phải làm. Bản 183 dòng đã sửa đúng cả 14 điểm:
tư thế Ambaṭṭha, phản ứng của tỳ-kheo, câu hỏi 1.9.5, "không tranh cãi", "chỗ sợ", 5 dòng bảng
mục 4, số lần im lặng, mục 6, "quỳ", nhà xuất bản, "chỉ hỏi", "không ai kết tội", giọng
Pokkharasāti, "không thể trả lời". Không có lỗi nặng nào trong phần dịch 1–2.

| # | Tệp | Đoạn | Bản đầu (160 dòng) | Vấn đề | Bản hiện tại / đề xuất |
|---|---|---|---|---|---|
| 1 | 00-gioi-thieu.md | dòng 44 | "Anh ta không đứng dậy chào, **vẫn ngồi**, vẫn nói chuyện theo kiểu ngang hàng." | Sai tư thế. 1.9.2 chỉ nói **các học trò** ngồi xuống một bên (`ekamantaṁ nisīdiṁsu`); 1.9.3 nói Ambaṭṭha **đi đi lại lại và đứng** nói với Đức Thế Tôn đang ngồi. Anh ta chỉ ngồi sau khi bị Vajirapāṇī dọa (1.21.4 `upanisīditvā`). Ảnh "vẫn ngồi" đảo ngược tương quan tư thế của cả cảnh. | "Anh ta không đứng dậy chào. Khi Đức Thế Tôn đang ngồi, anh ta cứ đi đi lại lại, rồi đứng nói chuyện với Ngài theo kiểu ngang hàng." |
| 2 | 00-gioi-thieu.md | dòng 45 | "Các tỳ-kheo thấy vậy thì **bất bình**." | Sai. 1.8.1–1.8.3: các tỳ-kheo ở ngoài, nghĩ rằng Đức Thế Tôn **không thấy nặng nề** khi đàm đạo với người con nhà danh giá; không ai bất bình. Họ còn chỉ đường cho Ambaṭṭha (1.8.4–1.8.5). Họ không chứng kiến cảnh trong chòi. | Xóa câu. Nếu cần giữ nhịp: "Các tỳ-kheo ở ngoài không hay biết chuyện gì xảy ra trong chòi." |
| 3 | 00-gioi-thieu.md | dòng 45–46 | "chỉ hỏi một câu tưởng như vô hại: **anh ta có thật nghĩ rằng một người như vậy là ngang hàng được không**." | Sai nội dung câu hỏi. 1.9.5 hỏi: "có phải ông đàm luận với các bà-la-môn tuổi cao… theo cách này: đi hay đứng trong khi ta đang ngồi, nói với ta vài câu xã giao?" — hỏi về **cách cư xử**, không phải về "ngang hàng". | "chỉ hỏi một câu: có phải ông vẫn đàm luận với các bà-la-môn cao tuổi theo cách ấy — đi hoặc đứng trong khi người đối diện đang ngồi?" |
| 4 | 00-gioi-thieu.md | dòng 48–49 | "**Đức Thế Tôn vẫn không tranh cãi.**" | Sai. 1.11.2 Ngài quở Ambaṭṭha "chưa tu tập mà tưởng mình đã tu tập"; 1.14.1–2 dùng ví dụ chim cút; 1.15.6 nói thẳng "ông là con của một người nữ tỳ của dòng Sakya"; 1.24–1.28 lập luận. Ngài không đôi co, nhưng không im lặng. | "Đức Thế Tôn không đôi co, nhưng Ngài không im lặng: Ngài quở, đặt câu hỏi, và dùng chính lập luận của Ambaṭṭha để bẻ lại." |
| 5 | 00-gioi-thieu.md | dòng 52 | "Ambaṭṭha đáp: dòng Kaṇhāyana. **Và đó chính là chỗ anh ta sợ.**" | Suy diễn tâm lý không có trong kinh. 1.15.4–1.15.5: Ambaṭṭha đáp ngay, không do dự; nỗi sợ chỉ xuất hiện ở 1.21.4, sau khi Vajirapāṇī hiện. | "Ambaṭṭha đáp gọn: dòng Kaṇhāyana. Câu trả lời ấy về sau trở thành chỗ yếu của anh ta." |
| 6 | 00-gioi-thieu.md | dòng 60–63, 69 (bảng mục 4) | 2.1 "Đức Thế Tôn hỏi về dòng dõi"; 2.2 "hỏi lại; Ambaṭṭha nói lảng"; 2.3 "Hỏi lần thứ ba; Ambaṭṭha vẫn lảng"; 2.4 "**Lần thứ tư**"; 7 "**hắn vẫn phân vân**" | Sai hệ thống. 2.1 (1.11–1.12) chỉ có lời miệt thị "tiện dân" lần đầu và lời quở, **không có câu hỏi dòng dõi**. 2.2 (1.13) Đức Thế Tôn hỏi dòng Sakya đã làm gì nên tội; Ambaṭṭha **kể chuyện Kapilavatthu**, không "nói lảng". 2.3 (1.14) không có câu hỏi thứ ba: Ngài đưa ví dụ chim cút và lập luận bốn giai cấp; Ambaṭṭha lặp "tiện dân" lần ba. 2.4 (1.15.4) là **lần đầu** hỏi dòng dõi, không phải "lần thứ tư". 7 (2.12.8): Ambaṭṭha kết luận Ngài **đủ cả 32 tướng, không thiếu**, rồi bỏ đi — không "phân vân". | Sửa 5 dòng: 2.1 "Ambaṭṭha lần đầu gọi sa-môn là tiện dân; Đức Thế Tôn quở anh ta chưa tu tập"; 2.2 "Ambaṭṭha gọi tiện dân lần hai; Ngài hỏi dòng Sakya đã làm gì nên tội; anh ta kể chuyện Kapilavatthu"; 2.3 "Ambaṭṭha gọi tiện dân lần ba; Ngài đưa ví dụ chim cút và lập luận bốn giai cấp"; 2.4 "Ngài hỏi dòng dõi; anh ta đáp Kaṇhāyana; Ngài hỏi nguồn gốc; hai lần im lặng; Vajirapāṇī hiện; anh ta trả lời"; 7 "Ngài cho thấy hai tướng còn thiếu; anh ta thấy đủ 32 tướng rồi bỏ đi". |
| 7 | 00-gioi-thieu.md | dòng 73–89 (mục 5) | "Hỏi lần hai. Im lặng. Hỏi lần ba. **Vẫn im lặng**." / "**Đến lần thứ tư**…" / "**Ba lần im lặng**…" / "**Lần thứ tư** chỉ là để anh ta nói ra." / "Sự lặp lại **ba lần**…" | Sai hệ thống. 1.20.6 im lặng lần 1; 1.20.8 hỏi lần 2; 1.20.9 im lặng lần 2; 1.20.11–12 Ngài cảnh báo; 1.21.1–2 Vajirapāṇī hiện; 1.21.4–6 Ambaṭṭha xin nhắc lại; 1.21.7–8 hỏi lần 3; 1.21.9 trả lời. Chỉ có **hai** lần im lặng; Vajirapāṇī hiện **trước** câu hỏi thứ ba; không có "lần thứ tư". | Đổi tiêu đề thành "Hai lần im lặng và lần hỏi thứ ba"; "Hỏi lần ba. Vẫn im lặng" → "Hỏi lần hai. Vẫn im lặng"; "Đến lần thứ tư" → "Đến lần hỏi thứ ba"; "Ba lần im lặng" → "Hai lần im lặng"; "Lần thứ tư" → "Câu hỏi thứ ba"; "Sự lặp lại ba lần" → "Sự lặp lại hai lần". Thêm: "Vajirapāṇī hiện ra trước khi Ngài hỏi lần thứ ba." |
| 8 | 00-gioi-thieu.md | dòng 108–111 | "Còn các vị thầy cổ của bà-la-môn… **thì chính họ cũng không có trí tuệ và hạnh tu ấy**." | Đọc ngược mục 6. 2.6–2.10: Đức Thế Tôn nói các vị ấy là **tác giả và người truyền bá** thần chú; Ngài hỏi Ambaṭṭha có phải các vị ấy sống đắm mình trong dục lạc như ông không — không. Kinh **không** nói các vị ấy thiếu `vijjācaraṇa`. Ý của mục 6 là: học thuộc lời các vị ấy không làm mình thành ẩn sĩ; và người bà-la-môn hôm nay sống khác các vị ấy. | "Còn các vị thầy cổ của bà-la-môn, những người đã sáng tác ra các bộ thần chú, thì Đức Thế Tôn dùng chính họ làm thước đo: các vị ấy sống đạm bạc, không đắm mình trong dục lạc như người bà-la-môn hôm nay. Học thuộc lòng lời các vị ấy không làm cho một người trở thành ẩn sĩ." |
| 9 | 00-gioi-thieu.md | dòng 17 | "rồi **quỳ xuống** xin quy y." | Sai động tác. 2.20.5: Pokkharasāti **ngồi xuống một bên** (`ekamantaṁ nisīdi`); 2.22.4: tuyên bố quy y. Không có động tác quỳ. | "rồi ngồi xuống một bên và xin quy y." |
| 10 | 00-gioi-thieu.md | dòng 132–133 | "bản *Mahāsaṅgīti* do **Hội Kinh điển Pali Thái Lan** ấn hành" | Sai tổ chức. Bản Mahāsaṅgīti Tipiṭaka Buddhavasse 2500 do **Dhamma Society** (M.L. Maniratana Bunnag Dhamma Society Fund), Thái Lan, ấn hành; "Pali Text Society" là tổ chức Anh, khác hẳn. | "(bản *Mahāsaṅgīti*, tức Đại kết tập lần thứ sáu, do Quỹ Dhamma Society ở Thái Lan ấn hành)" |
| 11 | 00-gioi-thieu.md | dòng 119 | "**Suốt phần đầu, Ngài chỉ hỏi.**" | Sai. 1.11.2 quở; 1.14.1–2 ví dụ chim cút; 1.15.6 tuyên bố "con của nữ tỳ"; 1.24–1.28 lập luận. Không phải "chỉ hỏi". | "Ngài không dùng lời lẽ mạnh, nhưng cũng không im lặng: Ngài quở, đặt câu hỏi, và dùng chính lập luận của Ambaṭṭha để bẻ lại." |
| 12 | 00-gioi-thieu.md | dòng 126–128 | "**trong bài không ai kết tội anh ta**" / "Pokkharasāti — người đã sai anh ta đi và **đã dạy anh ta những điều ấy**" | Sai. 1.22.2 các học trò chế giễu "dòng dõi xấu, con của nữ tỳ"; 1.15.6 Đức Thế Tôn gọi "con của nữ tỳ"; 2.17.9 Pokkharasāti gọi Ambaṭṭha là `bālo` ("kẻ si dại"). Kinh không nói Pokkharasāti dạy anh ta thái độ khinh miệt. | "Ambaṭṭha bị bóc trần, nhưng Đức Thế Tôn không để anh ta bị dày xéo: khi các học trò bạn xôn xao chế giễu, Ngài can ngăn và kể chuyện ẩn sĩ Kaṇha. Bài kinh để anh ta đi về. Còn Pokkharasāti — người đã sai anh ta đi — lại là người cuối cùng đạt được điều mà Ambaṭṭha không đạt được." |
| 13 | 00-gioi-thieu.md | dòng 156–157 | "Pokkharasāti — giọng một người trên cơ, **nóng khi bị chạm vào thể diện**." / "Các tỳ-kheo và các học trò — giọng đám đông, **đôi khi là tiếng cười**." | Nửa đúng. 2.17.9 có cảnh Pokkharasāti **nổi giận, đá Ambaṭṭha** — nên "nóng" không sai. Nhưng "giọng một người trên cơ" sai với thái độ của ông trước Đức Thế Tôn: cung kính, xin lỗi thay Ambaṭṭha, ngồi thấp, quy y (2.17.9, 2.20.5, 2.22.4). Và "đôi khi là tiếng cười" không có trong kinh: 1.22.1–2 là tiếng ồn chế giễu, không phải tiếng cười của tỳ-kheo/học trò. | "**Pokkharasāti** — giọng một người có địa vị: với Đức Thế Tôn thì cung kính, với học trò thì nghiêm khắc, và có một lần nổi giận thật sự." / "**Các tỳ-kheo và các học trò** — giọng đám đông: lúc dè dặt, lúc xôn xao." |
| 14 | 00-gioi-thieu.md | dòng 11 | "Rồi anh ta bị dồn vào một câu hỏi mà anh ta **không thể** trả lời" | Sai. 1.20.5–1.21.9: anh ta **biết** câu trả lời (chính lời giới thiệu nói vậy ở dòng 84–85), nhưng không chịu nói; sau khi bị dọa thì trả lời được. | "Rồi anh ta bị dồn vào một câu hỏi mà anh ta **không muốn** trả lời." |

## Lỗi nhẹ (đã sửa trực tiếp)

| # | Tệp | Đoạn | Đã sửa thành | Lý do |
|---|---|---|---|---|
| 1 | 01-opening.md | dn3:1.2.1 | "…đầy lúa gạo, là **đất của vua**, do vua Pasenadi nước Kosala ban cho…" | "thực ấp" là từ Hán-Việt tối nghĩa (fief), lại gợi ý vùng đất được ban cấp theo chế độ phong kiến; `rājabhogga` chỉ là "tài sản/đất của vua". |
| 2 | 01-opening.md, 02-ambattha.md | dn3:1.2.6, dn3:1.4.5 | "…có **dân chúng cùng hàng sa-môn và bà-la-môn**, có chư thiên và loài người…" | Bản cũ bỏ mất `pajaṁ` ("dân chúng") trong công thức `sassamaṇabrāhmaṇiṁ pajaṁ`; câu dịch chỉ còn "có hàng sa-môn và bà-la-môn", thiếu chủ ngữ tập thể. Đã sửa đồng thời cả hai lần xuất hiện. |
| 3 | 02-ambattha.md | dn3:1.4.1 | "Rồi bà-la-môn Pokkharasāti gọi thanh niên Ambaṭṭha **lại bảo**:" | "gọi… mà bảo" là lối nói nửa cổ, nửa dịch máy; "gọi… lại bảo" tự nhiên hơn. |
| 4 | 02-ambattha.md | dn3:1.4.8 | "**Đến nơi**, con hãy tìm hiểu sa-môn Gotama…" | "Đến rồi" là dịch sát `upasaṅkamitvā`, nhưng tiếng Việt phải là "đến nơi/đến đó". |
| 5 | 02-ambattha.md | dn3:1.6.1 | "…đi **vòng quanh ông, giữ ông ở bên phải**…" | "đi nhiễu quanh ông theo phía bên phải" là calque của `padakkhiṇaṁ`; cách nói rõ nghĩa là "đi vòng quanh, giữ người ấy ở bên phải". |
| 6 | 02-ambattha.md | dn3:1.6.1 | "…và cùng với **một số học trò trẻ** khởi hành…" | `sambahula` = "một số" (chính chú thích 1.6.1 đã nói vậy); "nhiều thanh niên trẻ" vừa sai số lượng vừa lặp nghĩa ("thanh niên" đã là trẻ). Đồng thời thống nhất với `ban-dich/12-pokkarasati-visits.md` ("các học trò trẻ"). |
| 7 | 02-ambattha.md | dn3:1.6.2 | "Đi xe đến **chỗ xe không đi được nữa**, anh ta xuống xe…" | "đến nơi nào xe có thể đi" dễ bị hiểu là "đi đến bất cứ đâu xe đi được"; `yāvatikā yānassa bhūmi` là "chừng nào đất còn đi xe được", tức đến chỗ hết đường xe. |
| 8 | 02-ambattha.md | dn3:1.6.2, 1.7.2, 1.9.3 | "**anh ta** xuống xe…" / "**anh ta** nói với các tỳ-kheo…" / "**anh ta** cũng nói…" | "chàng" là đại từ văn học/cổ, không hợp giọng người kể trung tính hiện đại; lời giới thiệu dùng "anh ta", các tệp khác cũng không dùng "chàng". |
| 9 | 02-ambattha.md | dn3:1.8.5 | "Ambaṭṭha, **đó là** chỗ trú của Đức Thế Tôn…" | "kia là" chỉ đúng khi vật ở xa người nói; ở đây các tỳ-kheo chỉ tay về chòi ngay trước mặt, và tiếng Việt hiện đại dùng "đó là". |
| 10 | 02-ambattha.md | dn3:1.9.2 | "**Các học trò trẻ** cũng bước vào…" | Thống nhất với 1.6.1 và với `māṇavaka` (chú thích 1.6.1: "học trò nhỏ"); "các thanh niên trẻ" là lặp nghĩa. |
| 11 | 02-ambattha.md | dn3:1.9.2 | "…sau khi trao đổi **những lời thăm hỏi thân thiện**, họ ngồi xuống một bên." | Câu trước đã có "chào hỏi Đức Thế Tôn"; "những lời chào hỏi và thăm hỏi" lặp ý. `sammodanīyaṁ kathaṁ sāraṇīyaṁ` vẫn được giữ bằng "lời thăm hỏi thân thiện". |
| 12 | 02-ambattha.md | dn3:1.9.3 | "Còn thanh niên Ambaṭṭha thì vừa đi đi lại lại vừa nói với Đức Thế Tôn đang ngồi vài câu xã giao; khi đứng, anh ta cũng nói với Đức Thế Tôn đang ngồi vài câu xã giao." | Câu cũ ("Nhưng thanh niên Ambaṭṭha, trong khi Đức Thế Tôn đang ngồi, chàng vừa đi…; và cả khi đứng, chàng cũng…") có ba lần đổi chủ ngữ, một mệnh đề chen giữa, và hai lần "Đức Thế Tôn đang ngồi" bị ngắt nhịp. Bản mới giữ nguyên ý và phép lặp của Pali (`caṅkamantopi… ṭhitopi… nisinnena bhagavatā`). |

## Câu công thức

| Câu (Pali → Việt) | Đúng | Lệch | Ghi chú |
|---|---|---|---|
| `evaṁ me sutaṁ` → "Tôi nghe như vầy." | 1 | 0 | dn3:1.1.1, đúng §4.3 từng chữ. |
| `ekaṁ samayaṁ` → "Một thuở nọ" | 1 | 0 | dn3:1.1.2, đúng §4.3. |
| `Atha kho bhagavā ambaṭṭhaṁ māṇavaṁ etadavoca:` → "Rồi Đức Thế Tôn nói với thanh niên Ambaṭṭha:" | 1 | 0 | dn3:1.9.4. Đây là câu §5 duy nhất xuất hiện trong phạm vi; toàn kinh 4 lần, phạm vi 1 lần, không đổi đại từ. |
| `Atha kho tesaṁ bhikkhūnaṁ etadahosi:` → "Rồi các tỳ-kheo ấy nghĩ như thế này:" | 1 | 0 | dn3:1.8.1; không nằm trong bảng §5 nhưng cùng khuôn `Atha kho…etadahosi`, dùng nhất quán. |
| Danh hiệu Phật `itipi so bhagavā… buddho bhagavā` (1.2.5–1.2.7 ↔ 1.4.4–1.4.6) | 2 | 0 | Hai lần giống hệt sau khi sửa `pajaṁ`. Khác với `08-knowledge-conduct.md` (ngoài phạm vi) ở cách dịch "bậc tối thượng…"; đề nghị thống nhất toàn dự án sau. |
| Công thức uy tín "Về ngài Gotama ấy, tiếng lành đã lan truyền như sau" (1.2.4–1.2.8 ↔ 1.4.3–1.4.7) | 2 | 0 | Chỉ khác "Này con Ambaṭṭha" ở 1.4.2 (đúng Pali `tāta ambaṭṭha`) và gloss "(Thích-ca)" ở lần đầu (đúng §4.1). |

Không có câu nào trong §5 bị lệch chữ. Không có `Taṁ kiṁ maññasi`, `Saccaṁ kira`, `Evaṁ vutte…tuṇhī ahosi` hay `idampissa hoti caraṇasmiṁ` trong phạm vi này.

## Xưng hô

- **Đức Thế Tôn → Ambaṭṭha:** đại từ "ông" ở 1.9.5 ("ông đàm luận"); lời các tỳ-kheo ở 1.8.5 cũng dùng "ông" ("mở cửa cho ông"). Không có "ngươi", "mày", "thằng" trong cả hai tệp.
- **Người kể → Đức Thế Tôn:** chuỗi "Đức Thế Tôn" xuất hiện 8 lần ở `01-opening.md`, 16 lần ở `02-ambattha.md` (kể cả chú thích); "Đức Phật" 0 lần. Đúng §3.
- **Các tỳ-kheo → Ambaṭṭha:** "Ông" (1.8.5). Đúng §3.
- **Pokkharasāti → Ambaṭṭha:** "Này con Ambaṭṭha", "con" (1.3.2, 1.4.2, 1.4.8). Đúng với `tāta`.
- **Ambaṭṭha → các tỳ-kheo:** "Thưa quý ngài" (1.7.3). Đúng §3.
- **Ambaṭṭha → Đức Thế Tôn:** không có lời trực tiếp nào trong phạm vi (anh ta chỉ trả lời từ 1.10 trở đi).

**Một điểm lệch §3 cần quyết định ở cấp hướng dẫn:** ở 1.5.1 và 1.7.3–1.7.4, Ambaṭṭha nói **về** Đức Thế Tôn với Pokkharasāti và các tỳ-kheo, và bản dịch dùng "ngài Gotama". §3 (dòng 65) quy định trường hợp này phải là "sa-môn Gotama". Pali ở 1.5.1 và 1.7.3–1.7.4 là `bhavaṁ gotamo` (kính ngữ), khác với `samaṇo gotamo` mà người khác dùng; vì vậy bản dịch đang theo Pali chứ không theo bảng. Đề nghị: hoặc sửa bảng §3 thành "`bhavaṁ gotamo` → ngài Gotama; `samaṇo gotamo` → sa-môn Gotama", hoặc sửa bản dịch cho đúng bảng. Không tự sửa ở đây vì đây là lỗi của quy chuẩn, không phải của câu dịch.

**Một điểm cần cân nhắc:** 1.9.5, Đức Thế Tôn tự gọi mình là "ta" ("trong khi **ta** đang ngồi… nói với **ta** vài câu xã giao"). §3 không cấm, nhưng "ta" đi với "ông" tạo giọng bề trên, hơi lệch mục tiêu "lịch sự đến mức lạnh lùng". Đề nghị đổi thành "tôi" (hoặc "Như Lai" nếu muốn trang trọng hơn) — xem mục Chất văn.

## Chất văn — chỗ cần viết lại

1. **1.4.9 — câu kết lời Pokkharasāti.** Hiện tại: "Ngài Gotama có như vậy hay không như vậy, rồi chúng ta sẽ biết rõ về ngài Gotama." Ba mệnh đề dồn vào một câu, hai lần "ngài Gotama" ngay cạnh nhau. Đề xuất: "Ngài Gotama có đúng là người như thế hay không, rồi chúng ta sẽ biết rõ về ngài."
2. **1.5.1 — câu hỏi của Ambaṭṭha.** Hiện tại: "Nhưng thưa ngài, làm sao con biết được ngài Gotama — tiếng đồn về ngài Gotama có đúng như thật hay không, ngài Gotama có như vậy hay không như vậy?" Dấu gạch ngang gánh ba mệnh đề, đọc không ra chỗ ngắt. Đề xuất: "Nhưng thưa ngài, làm sao con biết được ngài Gotama? Tiếng đồn về ngài có đúng như thật hay không, ngài có đúng là người như vậy hay không?"
3. **1.5.3 — "đạt được sự vững vàng cho dân nước".** `janapadatthāvariyappatto` là "đạt được sự ổn định của đất nước", không phải "cho dân nước". Đề xuất: "đạt được sự ổn định của đất nước".
4. **1.2.1 — câu 45 chữ.** Hiện tại: "Lúc bấy giờ, bà-la-môn Pokkharasāti sống tại Ukkaṭṭhā — một vùng đất đầy dẫy sinh vật, đầy cỏ, củi và nước, đầy lúa gạo, là đất của vua, do vua Pasenadi nước Kosala ban cho, một khu vườn của vua cấp cho bà-la-môn." Bốn tầng apposition trong một câu. Đề xuất tách đôi: "Lúc bấy giờ, bà-la-môn Pokkharasāti sống tại Ukkaṭṭhā, một vùng đất đầy dẫy sinh vật, đầy cỏ, củi và nước, đầy lúa gạo. Vùng đất ấy là đất của vua, do vua Pasenadi nước Kosala ban cho, một khu vườn của vua dành cho bà-la-môn."
5. **1.6.1 — câu 50 chữ, một chuỗi động tác.** Hiện tại: "Dạ, thưa ngài" — thanh niên Ambaṭṭha vâng lời bà-la-môn Pokkharasāti, rồi đứng dậy khỏi chỗ ngồi, đảnh lễ bà-la-môn Pokkharasāti, đi vòng quanh ông, giữ ông ở bên phải, lên cỗ xe do ngựa cái kéo, và cùng với một số học trò trẻ khởi hành… Đề xuất: "Dạ, thưa ngài" — thanh niên Ambaṭṭha vâng lời. Anh ta đứng dậy khỏi chỗ ngồi, đảnh lễ bà-la-môn Pokkharasāti, đi vòng quanh ông, giữ ông ở bên phải. Rồi anh ta lên cỗ xe do ngựa cái kéo, cùng một số học trò trẻ khởi hành đến khu rừng rậm Icchānaṅgala.
6. **1.9.5 — "ta".** Đề xuất: "…đi hay đứng trong khi **tôi** đang ngồi, nói với **tôi** vài câu xã giao?" Nếu muốn giữ sắc lạnh mà không bề trên, có thể dùng "Như Lai", nhưng "tôi" gần với tiếng Việt hiện đại hơn.
7. **1.3.1 — "cùng với sử thi là phần thứ năm".** `itihāsa` là truyền thuyết/lịch sử, không phải sử thi; "phần thứ năm" đứng trơ không rõ là phần thứ năm của cái gì. Đề xuất: "cùng với truyền thuyết, tính là phần thứ năm" (chú thích 1.3.1 đã giải thích `itihāsa`).
8. **1.3.2 và 1.5.9 — "ta" của Pokkharasāti.** "Điều **ta** biết, con cũng biết" và "còn **ta** là người trao thần chú". Pokkharasāti là thầy già, trang trọng; "thầy/con" ấm và tự nhiên hơn, vẫn giữ được vị thế. Đề xuất: "Điều **thầy** biết, con cũng biết…" và "còn **thầy** là người trao thần chú, con là người nhận lấy thần chú." (Không sửa vì đây là lựa chọn giọng.)
9. **1.2.7 — "có ý nghĩa và văn cú".** "Văn cú" là từ Hán-Việt ít người đọc phổ thông hiểu; `sātthaṁ sabyañjanaṁ` là "có ý nghĩa và lời lẽ". Đề xuất: "có ý nghĩa và lời lẽ sáng rõ".
10. **1.2.6 — "bằng thắng trí".** `abhiññā` là thắng trí/trực chứng; từ này đúng nhưng tối nghĩa với người mới. Có thể giữ (thuật ngữ Phật học quen) hoặc đổi thành "nhờ tuệ giác của mình". Không sửa vì là thuật ngữ, nhưng nên thống nhất với các tệp sau.
11. **Lời giới thiệu, dòng 134 — "rất ít thấy".** "Cảnh bị xúc phạm trực diện rất ít thấy trong kinh tạng." Đây là khẳng định thống kê không dẫn chứng; nên bỏ câu này và mở thẳng bằng dẫn chứng "Người ta gọi Đức Thế Tôn là 'tiện dân'…".
12. **Lời giới thiệu, dòng 138–139 — "một câu cụ thể".** "Ngài không đáp trả bằng một lời nặng hơn; Ngài hỏi một câu cụ thể, và để câu trả lời tự làm việc." Ngài quở (1.11.2), lập luận (1.14), tuyên bố "con của nữ tỳ" (1.15.6) — không phải "một câu". Đề xuất: "Ngài không đáp trả bằng một lời nặng hơn, nhưng cũng không né tránh: Ngài hỏi những câu cụ thể, và để câu trả lời tự làm việc."
13. **Lời giới thiệu, dòng 37 — "sống trên".** "Pokkharasāti sống trên một vùng đất của vua" — "trên" hơi lạ; "sống ở" tự nhiên hơn.
14. **Lời giới thiệu, dòng 162–163 — "thuật ngữ khó".** "thuật ngữ khó được giải thích bằng chú thích khi xuất hiện lần đầu" — không phải mọi thuật ngữ khó đều được chú thích (1.2.6 "thắng trí", 1.2.7 "văn cú"). Nên viết "một số thuật ngữ khó".

## Lời giới thiệu — kiểm chứng

Bảng này kiểm chứng **bản đầu 160 dòng**; cột "Đúng/Sai" nói về bản ấy. Ở bản 183 dòng, các dòng
ghi "Sai" đã được sửa (xem ghi chú phiên bản ở đầu báo cáo); các dòng còn lại vẫn đúng.

| # | Nhận định (dòng) | Đúng/Sai | Căn cứ trong kinh |
|---|---|---|---|
| 1 | Bối cảnh Kosala, khoảng 500 tỳ-kheo, rừng Icchānaṅgala (34–35) | Đúng | 1.1.2, 1.2.1, 1.2.3 |
| 2 | Ambaṭṭha là học trò Pokkharasāti, dòng Kaṇhāyana (24–25) | Đúng | 1.3.1, 1.15.5 |
| 3 | Pokkharasāti sai Ambaṭṭha đi kiểm tra 32 tướng (39–42) | Đúng | 1.4.8–1.5.2 |
| 4 | "Cách đó không xa có thị trấn Ukkaṭṭhā" (37) | Không có trong kinh | Kinh chỉ nói Pokkharasāti sống tại Ukkaṭṭhā (1.2.1); không nói khoảng cách, không gọi là thị trấn. |
| 5 | "một vùng đất **rộng**" (38) | Không có chữ "rộng" | 1.2.1 chỉ liệt kê: đầy dẫy sinh vật, cỏ, củi, nước, lúa gạo. |
| 6 | "**vì** Ambaṭṭha… rành về tướng mạo" (41–42) | Suy diễn | 1.4.8 chỉ nói "đi tìm hiểu"; 1.3.1 liệt kê phẩm chất, không nêu lý do được sai đi. |
| 7 | "không đứng dậy chào, **vẫn ngồi**" (44) | Sai | 1.9.2–1.9.3; xem lỗi nặng #1. |
| 8 | "Các tỳ-kheo thấy vậy thì bất bình" (45) | Sai | 1.8.1–1.8.3; xem lỗi nặng #2. |
| 9 | Câu hỏi của Ngài là "ngang hàng được không" (45–46) | Sai | 1.9.5; xem lỗi nặng #3. |
| 10 | "Đức Thế Tôn vẫn không tranh cãi" (48–49) | Sai | 1.11.2, 1.14.1–2, 1.15.6; xem lỗi nặng #4. |
| 11 | "Ambaṭṭha đáp: dòng Kaṇhāyana. Và đó chính là chỗ anh ta sợ." (52) | Nửa đúng | 1.15.4–1.15.5: đáp ngay, không sợ; sợ ở 1.21.4; xem lỗi nặng #5. |
| 12 | "không thể trả lời" (11) | Sai | 1.21.9: trả lời được sau khi bị dọa; xem lỗi nặng #14. |
| 13 | "chín mục" (54) | Đúng | 1.0–2.22, đủ 1, 2 (2.1–2.5), 3–9. |
| 14 | Bảng 2.1: "Đức Thế Tôn hỏi về dòng dõi" (60) | Sai | 1.11–1.12: chỉ có lời miệt thị lần đầu và lời quở; không có câu hỏi dòng dõi. |
| 15 | Bảng 2.2: "hỏi lại; Ambaṭṭha nói lảng" (61) | Sai | 1.13: Ngài hỏi dòng Sakya đã làm gì nên tội; Ambaṭṭha kể chuyện Kapilavatthu, không lảng. |
| 16 | Bảng 2.3: "Hỏi lần thứ ba; Ambaṭṭha vẫn lảng" (62) | Sai | 1.14.1–2: ví dụ chim cút và lập luận bốn giai cấp; Ambaṭṭha lặp "tiện dân" lần ba. |
| 17 | Bảng 2.4: "**Lần thứ tư**" (63) | Sai | 1.15.4: đây là **lần đầu** hỏi dòng dõi. |
| 18 | Bảng 2.5: "Đức Thế Tôn chấm dứt chuyện ấy" (64) | Chưa đúng | 1.22–1.23: Ngài can ngăn các học trò chế giễu và kể chuyện ẩn sĩ Kaṇha, không chỉ "chấm dứt". |
| 19 | Bảng 7: "hắn vẫn phân vân" (69) | Sai | 2.12.8: Ambaṭṭha kết luận Ngài đủ cả 32 tướng, không thiếu; rồi bỏ đi (2.12.12). |
| 20 | "Ba lần im lặng… lần thứ tư" (73–89) | Sai | 1.20.6, 1.20.9 (hai lần im lặng); 1.21.7 (hỏi lần ba); xem lỗi nặng #7. |
| 21 | "Vajirapāṇī… **nói rằng** nếu không trả lời thì sẽ đập đầu…" (80–82) | Sai | 1.21.1–2: đó là **ý nghĩ** của Vajirapāṇī (`…phālessāmīti`); lời cảnh báo công khai là của Đức Thế Tôn ở 1.20.12. |
| 22 | "quỳ xuống xin quy y" (17) | Sai | 2.20.5: ngồi xuống một bên; 2.22.4: tuyên bố quy y; xem lỗi nặng #9. |
| 23 | Mục 3 "so sánh nữ với nữ, nam với nam" (99–101) | Chưa chính xác | 1.24–1.26 là hai trường hợp hôn nhân **khác giai cấp** (sát-đế-lợi trai + bà-la-môn gái; bà-la-môn trai + sát-đế-lợi gái), rồi kết luận "xét phía nữ hay phía nam, sát-đế-lợi vẫn hơn". |
| 24 | "Các vị thầy cổ… không có trí tuệ và hạnh tu ấy" (108–111) | Sai | 2.6–2.10; xem lỗi nặng #8. |
| 25 | "Suốt phần đầu, Ngài chỉ hỏi" (119) | Sai | 1.11.2, 1.14.1–2, 1.15.6; xem lỗi nặng #11. |
| 26 | "Một trong số ít bài kinh… Trong đa số bài kinh, người đối thoại… lễ độ" (115–116) | Không có căn cứ | Không thể kiểm chứng trong bài; đây là khẳng định thống kê không dẫn chứng. Nên bỏ hoặc hạ giọng ("ít thấy cảnh bị xúc phạm trực diện như vậy"). |
| 27 | "trong bài không ai kết tội anh ta" (126–127) | Sai | 1.15.6, 1.22.2, 2.17.9; xem lỗi nặng #12. |
| 28 | "Pokkharasāti… đã dạy anh ta những điều ấy" (127–128) | Không có trong kinh | 2.17.9 chỉ nói Ambaṭṭha là học trò; không nói ông dạy thái độ khinh miệt. |
| 29 | "bản Mahāsaṅgīti do Hội Kinh điển Pali Thái Lan ấn hành" (132–133) | Sai | Mahāsaṅgīti Tipiṭaka Buddhavasse 2500 do Dhamma Society (Thái Lan) ấn hành; Pali Text Society là tổ chức Anh. |
| 30 | "Các thuật ngữ Phật học… giải thích ngay trong ngoặc ở lần đầu xuất hiện" (141) | Không đúng với bản dịch | 1.1.3 dùng "tỳ-kheo"; 1.2.1 dùng "bà-la-môn"; 1.2.3 dùng "sa-môn"; 1.2.8 dùng "A-la-hán" — đều không có ngoặc. |
| 31 | "Có bốn nhân vật với bốn giọng khác nhau" (151) | Chưa chính xác | Mục thứ tư là một **nhóm** ("Các tỳ-kheo và các học trò"), không phải một nhân vật. |
| 32 | "Pokkharasāti… nóng khi bị chạm vào thể diện"; "đôi khi là tiếng cười" (156–157) | Nửa đúng / Sai | "Nóng" đúng: 2.17.9 ông nổi giận, đá Ambaṭṭha. "Trên cơ" sai: 2.17.9, 2.20.5, 2.22.4 ông cung kính. "Tiếng cười" sai: 1.22.1–2 là tiếng ồn chế giễu. Xem lỗi nặng #13. |
| 33 | "Cả bài kinh xoay quanh anh ta" (25) | Nói quá | Mục 8–9 không có Ambaṭṭha; anh ta chỉ được nhắc đến gián tiếp ở 2.17.9. Nên viết "nhân vật chính của phần lớn bài kinh". |
| 34 | "Ambaṭṭha không phải tên một giáo lý" (24) | Đúng nhưng thừa | Không có căn cứ nào cần phủ định; câu này không thêm thông tin. |
| 35 | "Pokkharasāti… đích thân đến gặp, tự mình kiểm tra từng tướng" (15–17) | Đúng | 2.13–2.19 |
| 36 | "Bài kinh khép lại bằng hình ảnh ngược lại hoàn toàn" (15) | Đúng | 2.20–2.22: Pokkharasāti ngồi thấp và quy y, tương phản với Ambaṭṭha ở 2.12.12. |

## Chú thích

Các chú thích nhìn chung chính xác và có giá trị, nhưng quá nặng với người đọc phổ thông: nhiều chỗ dẫn tên văn bản, học giả, niên đại mà không cần cho việc hiểu chính văn. Dưới đây là các chỗ nên cắt gọn.

| # | Tệp: dòng | Vấn đề | Đề xuất |
|---|---|---|---|
| 1 | 01-opening.md:4 (chú thích 1.1.1) | Quá nặng: Pauṣkarasādi, Puṣkarāvati, Gandhāra, Kātyāyana, Patañjali, MN 99. | Giữ một câu: "Pokkharasāti là một vị thầy bà-la-môn có thật, sống cùng thời với Đức Thế Tôn; văn bản bà-la-môn sau này còn dẫn lời ông." Cắt phần ngữ pháp Kātyāyana/Patañjali. |
| 2 | 01-opening.md:20 (chú thích 1.2.1) | Quá nặng: `droṇamukha`, Subhaga, `rājadāya`/`migadāya`, `brahmadeyya`, "chế độ phong kiến Ấn Độ". | Giữ: "Ukkaṭṭhā là một thị trấn chợ lớn, đi lại được cả đường bộ lẫn đường thủy; vùng đất này do vua ban cho bà-la-môn." Cắt các so sánh từ nguyên. |
| 3 | 01-opening.md:37 (chú thích 1.2.6) | Tối nghĩa: "Đối chiếu với chỗ chính ông phủ nhận khả năng này ở MN 99:10.7." Không rõ "ông" là ai, "khả năng này" là gì. | Bỏ, hoặc viết rõ: "Ở MN 99:10.7, chính Pokkharasāti phủ nhận điều mà ở đây ông ca ngợi." Nếu không chắc nội dung MN 99, bỏ hẳn. |
| 4 | 02-ambattha.md:7 (chú thích 1.3.1) | Quá nặng: Nirukta của Yāska, Keṭubha, Śatapatha Brāhmaṇa, Pāṇinī, `akṣara-samāmnāya`, `padaprabheda`, `nirutti`, Chāndogya Upaniṣad. | Giữ 3–4 câu giải thích `nighaṇḍu`, `keṭubha`, `itihāsa`; cắt các chi tiết ngữ pháp Ấn. |
| 5 | 02-ambattha.md:52 (chú thích 1.5.2) | Nặng: Gārgīyajyotiṣa, Bṛhatsaṁhitā, sử thi Gilgamesh. | Giữ: "32 tướng không có trong văn bản bà-la-môn thời ấy; có lẽ là di sản của một truyền thống đã mất." Cắt Gilgamesh hoặc chỉ giữ một dòng. |
| 6 | 02-ambattha.md:57 (chú thích 1.5.3) | Nặng: tế ngựa Vệ-đà, người Ấn-Âu, Biển Đen, bánh xe mặt trời, DN 17, Rig Veda 8.63.8. | Giữ một câu về tế ngựa và một câu về biểu tượng bánh xe; cắt phần di cư Ấn-Âu. |
| 7 | 02-ambattha.md:68 (chú thích 1.5.6) | Lạc ý: chính văn nói "hơn một nghìn người con trai", chú thích nói "con ngựa tế lễ… được một trăm người con trai bảo vệ" — người đọc không hiểu vì sao. | Thêm cầu nối: "Trong tế ngựa Vệ-đà, con ngựa được một trăm con trai của vua bảo vệ; ở đây con số được phóng đại thành hơn một nghìn." Hoặc bỏ. |
| 8 | 02-ambattha.md:108 (chú thích 1.7.4) | Vô ích: "Đoạn tương ứng ở MN 35:7.4 có cách nói khác ở chỗ này." Không nói khác thế nào, cũng không ảnh hưởng nghĩa. | Bỏ. |
| 9 | 02-ambattha.md:119 (chú thích 1.8.3) | Jargon: "từ mang tính giới", "ngầm giả định địa vị xã hội của nam giới". | "Đây là từ chỉ đàn ông, và ngầm giả định người ấy thuộc tầng lớp có địa vị." |
| 10 | 02-ambattha.md:144 (chú thích 1.9.5) | Câu đầu thừa vì chính văn đã quá rõ: "Ở đây Đức Thế Tôn lưu ý đến cách cư xử khiếm nhã của Ambaṭṭha." | Bỏ câu đầu; giữ câu sau ("Trong các kinh, cách người ta chào Đức Thế Tôn thường hé lộ thái độ…"). |
| 11 | 01-opening.md:45 (chú thích 1.2.8) | "Người trí không **chấp** vào danh phận tôn giáo" — "chấp" là từ Phật học, tối nghĩa với người mới. | "Người trí không bận tâm đến nhãn mác tôn giáo." |
| 12 | 02-ambattha.md:44 (chú thích 1.4.9) | Chú thích nói về cách đọc `tayā` ở MN 91:4.9 nhưng không nói bản dịch đang theo cách đọc nào; người đọc dễ tưởng câu dịch sai. | Thêm: "Bản dịch này theo bản Mahāsaṅgīti, đọc là `tathā mayaṁ` ('như vậy chúng ta sẽ biết'); bản PTS/BJT đọc `tayā` ('qua con, ta sẽ biết')." Hoặc bỏ chú thích. |

## Kết luận

Bản đầu (160 dòng): **CẦN SỬA**. Bản hiện tại (183 dòng, md5 `a7cc57a19ced2d8867ede05757971212`):
**ĐẠT** — 14 lỗi nặng đã được khắc phục; còn 4 điểm nhỏ về giọng (dòng 37, 134, 138–139, 162–163),
không chặn phát hành.
