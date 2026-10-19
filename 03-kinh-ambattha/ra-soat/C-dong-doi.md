# Rà soát C — mục 2.5 và mục 3

## Tóm tắt

Phạm vi: `ban-dich/06-heritage.md` (dn3:1.22.0–1.23.22, 26 đoạn) và
`ban-dich/07-aristocrats.md` (dn3:1.24.0–1.28.12, 65 đoạn). Đối chiếu `root_text` và
`translation_text` trong `nguon/api_dn3.json`, và bản section trong `nguon/sections/`.

Kết quả chính:

- **Không có lỗi đảo nghĩa.** Toàn bộ 18 câu trả lời ngắn ở 1.24–1.27 đúng chiều
  (được/không được, bị ngăn/không bị ngăn); hai câu lý do đúng cặp: 1.24.15 "dòng mẹ"
  (`mātito`) và 1.25.14 "dòng cha" (`pitito`).
- **Phép so sánh kép 1.24 ↔ 1.25 được giữ nguyên**: khattiya trai + bà-la-môn gái, rồi
  bà-la-môn trai + khattiya gái; mọi vế đối xứng, chỉ đổi vai.
- **Kết luận đúng**: 1.26.1 và 1.27.12 đều "sát-đế-lợi … cao quý nhất, bà-la-môn … thấp kém".
- **Câu công thức §5 trong phạm vi: đúng 100%** — 1.23.1 và 4 lần "Ambaṭṭha, ông nghĩ thế
  nào" (1.24.2, 1.25.1, 1.26.2, 1.27.1). Kiểm tra toàn cục: 4/4 và 14/14.
- **Xưng hô đúng bảng §3** — xem mục riêng.
- Đã sửa **6 nhóm** (5 lỗi nhẹ + 1 điểm nặng về tác động).
- **Một điểm nặng duy nhất**: bước ngoặt ở 1.28 thiếu từ nối đối lập; đã sửa bằng một chữ.
  Đây là chỗ duy nhất trong phạm vi có thể làm người đọc hiểu sai cả lập luận.

Ghi chú về đề bài: các chuỗi ví dụ "chim, cây, hạt" **không nằm trong mục 3**. Trong DN 3
chúng ở mục 2.2–2.3 (chim cút: dn3:1.14.1, tệp `04-primitives-2-3.md`); mục 3 là văn nghị
luận, không có dụ ngôn. Vì vậy bảng song song dưới đây lập cho các chuỗi lặp thật sự có
trong phạm vi: chuỗi hỏi–đáp 5 câu × 4 vòng và công thức trục xuất.

## Lỗi nặng (phải sửa)

Không có lỗi nặng nào còn tồn đọng. Một điểm được xếp vào diện nặng vì tác động lên toàn
bộ lập luận; cách sửa chỉ là thêm một chữ nên đã áp dụng ngay.

| # | Tệp | Đoạn | Hiện tại | Vấn đề | Đề xuất |
|---|---|---|---|---|---|
| 1 | 07-aristocrats.md | dn3:1.28.3–1.28.4 và 1.28.9–1.28.10 | `…lấy dòng dõi làm chuẩn,` / `nhưng người có đủ trí tuệ và hạnh tu` (trước khi sửa: `…làm chuẩn;` / `người có đủ…`, không có từ nối) | Pali 1.28.4–1.28.5: `Vijjācaraṇasampanno / so seṭṭho devamānuse`. `so` hồi chỉ chủ ngữ mới; vế 3 mở ra một tiêu chuẩn khác. Thiếu từ nối đối lập, người đọc có thể gán "người có đủ trí tuệ và hạnh tu" cho "sát-đế-lợi" → câu kệ bị đọc thành khẩu hiệu sát-đế-lợi thượng đẳng, mất bước ngoặt sang `vijjācaraṇa`. | Thêm "nhưng" đầu vế 3, đổi ";" cuối vế 2 thành ",". **Đã áp dụng**, giữ giống hệt ở cả hai lần tụng (1.28.4 và 1.28.10). |

## Lỗi nhẹ (đã sửa trực tiếp)

| # | Tệp | Đoạn | Đã sửa thành | Lý do |
|---|---|---|---|---|
| 1 | 06-heritage.md | dn3:1.23.9 | "Nhưng vua không thể **buông** mũi tên ấy **ra**, cũng không thể thu nó lại." | "bắn mũi tên ấy đi" không phải cách nói tự nhiên; `muñcituṁ` là nhả/buông dây cung, đối lập với `paṭisaṁharituṁ` ("thu lại") ngay sau đó. |
| 2 | 06-heritage.md | dn3:1.23.17 | "Nhưng **vua hãy bắn** mũi tên vào thái tử, thái tử sẽ bình an vô sự." | Pali dùng mệnh lệnh `patiṭṭhāpetu` ("hãy đặt/bắn"), không phải điều kiện `yadi` như 1.23.13 và 1.23.15. "Nếu" làm mất mệnh lệnh của Kaṇha — mà chính mệnh lệnh ấy được các đại thần truyền lại ở 1.23.19. |
| 3 | 06-heritage.md | dn3:1.23.5 (chú thích) | "**Cách gọi ấy không nhằm tán thành sự khinh miệt**, mà là một thủ pháp tu từ để bẻ gãy lòng kiêu ngạo của Ambaṭṭha." | Câu cũ "Ở đây nó không phải là lời tán thành" có đại từ "nó" không rõ tiền ngữ; người đọc dễ hiểu ngược (như thể Đức Thế Tôn tán thành cách gọi khinh miệt). |
| 4 | 07-aristocrats.md | dn3:1.24.3 và 1.25.2 | "Giả sử có một **cậu trai** dòng sát-đế-lợi **chung sống với** một cô gái bà-la-môn…" (và vế đối xứng ở 1.25.2) | "ăn nằm với" là tiếng lóng thô, lệch giọng điềm tĩnh của Đức Thế Tôn; `saṁvāsaṁ kappeyya` là "chung sống" trung tính. Đồng thời thống nhất "cậu trai" với 1.24.4/1.25.3 (trước đó 1.24.3 dùng "cậu con trai", 1.24.4 dùng "cậu trai" — lệch trong cùng một cặp). |
| 5 | 07-aristocrats.md | dn3:1.27.11 và 1.27.12 | "…đã bị đẩy xuống mức **thấp kém** nhất…" | Bảng thuật ngữ: `hīna` = "thấp kém". "Thấp hèn" là từ khác nghĩa (hèn hạ, đáng khinh), làm mất liên hệ với `hīnā brāhmaṇā` ở 1.26.1 và 1.27.12. |

## Bảng song song các chuỗi ví dụ lặp

| Chuỗi | Số vế | Vế nào lệch khuôn | Đề xuất |
|---|---|---|---|
| Tiền đề hôn nhân 1.24.3 ↔ 1.25.2 | 2 | Sau khi sửa: không lệch. Trước khi sửa: 1.24.3 "cậu con trai" / 1.24.4 "cậu trai" — lệch ngay trong một cặp. | Giữ "cậu trai" ở cả 4 vế (đã làm). |
| Q1 "chỗ ngồi và nước" — 1.24.4, 1.25.3, 1.26.4, 1.27.3 | 4 | 1.24.4/1.25.3 có thêm mệnh đề "Đứa con sinh ra từ…" — **đúng Pali**, vì 1.26/1.27 đã có tiền ngữ "một người…" riêng. Không phải lỗi. | Giữ nguyên. |
| Q2 "thết đãi … bốn lễ" — 1.24.6, 1.25.5, 1.26.6, 1.27.5 | 4 | Không lệch — 4 vế giống hệt từng chữ. | — |
| Q3 "dạy thần chú" — 1.24.8, 1.25.7, 1.26.8, 1.27.7 | 4 | Không lệch. | — |
| Q4 "bị ngăn … phụ nữ" — 1.24.10, 1.25.9, 1.26.10, 1.27.9 | 4 | Không lệch. | — |
| Q5 "quán đỉnh" — 1.24.12, 1.25.11 | 2 | 1.24.12 có "(lễ đăng quang)", 1.25.11 không. | Khác biệt **có chủ ý**: §1.3 giải thích thuật ngữ ngay lần đầu. Không cần sửa; nếu muốn tuyệt đối song song thì chuyển gloss thành chú thích riêng. |
| Cặp lý do 1.24.15 ↔ 1.25.14 | 2 | Không lệch — "dòng mẹ" / "dòng cha" đúng chiều với phép so sánh. | — |
| Công thức trục xuất 1.26.3, 1.27.2, 1.27.11 | 3 | 1.27.11 dùng dấu hai chấm thay cho mệnh đề "khi…" (đã sửa) — nội dung khớp 1.26.3/1.27.2. | — |
| Bài kệ 1.28.2–1.28.5 ↔ 1.28.8–1.28.11 | 2 | Trước khi sửa: cả hai lần đều thiếu "nhưng" (lệch giống nhau, nên không lộ ra khi đối chiếu). Sau khi sửa: hai lần giống hệt. | Giữ nguyên sau khi sửa. |
| Chuỗi câu trả lời ngắn 1.24.5–1.27.10 | 18 | Không lệch: "nó sẽ được" (3), "họ sẽ thết đãi" (3), "họ sẽ dạy" (3), "nó không bị ngăn" (3), "không được" (5), "nó bị ngăn" (1) — dùng đúng chỗ. | — |

Kết luận của bảng: trong phạm vi này, các chuỗi lặp **rất nhất quán**; chỗ lệch duy nhất
đáng kể là bài kệ (đã sửa). Không có chuỗi chim/cây/hạt nào ở mục 3 để so.

## Câu công thức và xưng hô

**Câu công thức §5 xuất hiện trong phạm vi:**

- `Atha kho bhagavato etadahosi:` → "Rồi Đức Thế Tôn nghĩ như thế này:" — 1.23.1, đúng
  nguyên văn. Toàn cục 4/4 (05, 06, 11, 12).
- `Taṁ kiṁ maññasi, ambaṭṭha,` → "Ambaṭṭha, ông nghĩ thế nào" — 1.24.2, 1.25.1, 1.26.2,
  1.27.1, đúng nguyên văn (dấu "?" cuối câu là dấu câu, không tính vào công thức). Toàn
  cục 14/14.
- 1.22.1 là `Evaṁ vutte` không có `tuṇhī`, nên chỉ mượn nửa đầu công thức: "Khi nghe vậy,
  các thanh niên ấy nhao nhao, làm ầm ĩ cả lên" — chấp nhận được.
- Các câu §5 còn lại không xuất hiện trong hai tệp này.

**Xưng hô:**

- Đức Thế Tôn → Ambaṭṭha: đại từ "ông" trong 4 lần công thức (1.24.2, 1.25.1, 1.26.2,
  1.27.1); gọi tên "này Ambaṭṭha" ở 1.26.1, 1.27.11, 1.27.12, 1.28.1, 1.28.7.
- Ambaṭṭha → Đức Thế Tôn: "thưa ngài Gotama" **20/20** lần (1.24.5–1.27.12), kể cả khi
  bị dồn vào chỗ không trả lời được. Mọi phát ngôn của Ambaṭṭha trong 07 đều mở bằng cụm
  này; không có chỗ nào ông gọi Đức Thế Tôn bằng "ông" hay "ngài" trống.
- Người kể → Đức Thế Tôn: "Đức Thế Tôn" (1.23.1, 1.23.3, 1.24.1). Không có "Đức Phật".
- Các thanh niên → nhau: "thưa các ngài" (1.22.2) — đúng bảng thuật ngữ (`bho` = "thưa
  ngài" giữa các bà-la-môn).
- Các đại thần → Kaṇha: "thưa ngài" (1.23.11, 1.23.12, 1.23.14, 1.23.16).
- Không có "ngươi", "mày", "thằng" trong cả hai tệp.

Một điểm nhỏ: Pali 1.22.2 lặp `kira, bho` bốn lần; bản dịch giữ đủ bốn "Nghe nói" nhưng
gộp bốn `bho` thành một "thưa các ngài". Đây là nén có chủ ý cho xuôi tai, không phải lỗi
nghĩa; nếu muốn theo §1.4 (PLI lặp thì bản dịch lặp) thì phải lặp "thưa các ngài" bốn lần —
đọc sẽ rất nặng, tôi không đề nghị.

## Chất văn — chỗ cần viết lại

1. **1.27.11 — câu nặng nhất mục 3 (đã xử lý).** Câu cũ: "Đến mức ấy, này Ambaṭṭha, một
   người sát-đế-lợi đã bị đẩy xuống mức thấp kém nhất, khi giới sát-đế-lợi cạo trọc đầu nó,
   lấy bao tro đánh vào nó, rồi trục xuất nó ra khỏi nước hoặc khỏi thành." Ba lần "nó" và
   mệnh đề "khi…" làm chùng đà kết luận ngay trước 1.27.12. Nay đã thành: "Đến mức ấy, này
   Ambaṭṭha, một người sát-đế-lợi đã xuống tới mức thấp kém nhất: giới sát-đế-lợi cạo trọc
   đầu nó, lấy bao tro đánh vào nó, rồi trục xuất nó ra khỏi nước hoặc khỏi thành." Đã đồng
   bộ 1.27.12 thành "đã xuống tới mức thấp kém nhất" để giữ đúng điệp khuôn của Pali
   (`paramanihīnataṁ patto hoti` lặp ở cả hai đoạn).
2. **Chuỗi câu hỏi 1.24–1.27 — hơi hành chính.** "Và liệu giới bà-la-môn có thết đãi nó
   trong lễ cúng tổ tiên, trong lễ dâng cơm sữa, trong tế lễ, hay trong bữa tiệc đãi khách
   không?" đúng nghĩa nhưng bốn chữ "trong" và "Và liệu… không?" làm câu chậm, trong khi
   đây là loạt câu hỏi dồn. Nếu muốn siết: "Thế giới bà-la-môn có thết đãi nó ở lễ cúng tổ
   tiên, lễ dâng cơm sữa, tế lễ, hay bữa tiệc đãi khách không?" — nhưng phải đổi đồng loạt
   cả 4 vòng (1.24.6, 1.25.5, 1.26.6, 1.27.5) mới giữ được khuôn.
3. **1.28.6 — "nói đúng chứ không nói sai".** `subhāsitā no dubbhāsitā` là "nói khéo/hay,
   không nói vụng/dở" (cặp với `sugītā no duggītā` ngay trước); "đúng/sai" chuyển sang trục
   chân–ngụy. Trong ngữ cảnh Ngài tán thành bài kệ thì vẫn có thể biện luận, nhưng sát hơn
   là "nói khéo chứ không nói vụng".
4. **1.26.1 — "vẫn".** "…thì sát-đế-lợi **vẫn** là cao quý nhất, bà-la-môn **vẫn** là thấp
   kém." Pali 1.26.1 không có `pi`; chỉ 1.27.12 mới có `tadāpi` ("ngay cả khi ấy"). Giữ
   "vẫn" tạo được điệp khúc, nhưng nếu ưu tiên sát nghĩa thì bỏ ở 1.26.1, giữ ở 1.27.12.
5. **1.24.1 — "hỏi".** `āmantesi` là "ngỏ lời/gọi", không phải "hỏi". Không sai nghĩa vì
   câu kế là câu hỏi, nhưng nếu muốn sát: "Rồi Đức Thế Tôn ngỏ lời với thanh niên Ambaṭṭha:".

## Bước ngoặt lập luận ở cuối mục 3

Bước ngoặt nằm trọn trong bài kệ 1.28.2–1.28.5 (lặp lại 1.28.8–1.28.11) và hai câu xác nhận
1.28.6–1.28.7, rồi mục 4 mở ra bằng câu hỏi của Ambaṭṭha (dn3:2.1.1: "hạnh tu ấy là gì, và
trí tuệ ấy là gì?") và câu trả lời 2.1.2 ("trong sự thành tựu trí tuệ và hạnh tu tối thượng,
người ta không nói đến chuyện giai cấp, không nói đến chuyện dòng dõi…").

Bản dịch **không làm mất** bước ngoặt, nhờ ba chỗ:

- vế điều kiện "đối với những ai lấy dòng dõi làm chuẩn" biến "sát-đế-lợi là cao quý nhất"
  thành một chân lý *có điều kiện*, không phải tuyệt đối;
- chủ ngữ vế 3 là "người có đủ trí tuệ và hạnh tu", và phạm vi mở rộng thành "giữa chư
  thiên và loài người" — rõ là một tiêu chuẩn khác, cao hơn;
- 1.28.7 "chính ta cũng nói như vậy" + lặp nguyên bài kệ khẳng định cả hai vế, không phải
  chỉ vế đầu.

Nhưng bản dịch **đã làm yếu** bước ngoặt ở đúng một chỗ: vế 3 không có từ nối đối lập. Đọc
liền (trước khi sửa) "…cao quý nhất trong loài người, / đối với những ai lấy dòng dõi làm
chuẩn; / người có đủ trí tuệ và hạnh tu / là cao quý nhất…", người đọc có thể hiểu "người có
đủ trí tuệ và hạnh tu" là một thuộc ngữ của "sát-đế-lợi" — tức là "vị sát-đế-lợi có đủ trí
tuệ và hạnh tu là cao quý nhất". Hiểu như vậy thì cả mục 4 mất chỗ đứng: mục 4 không còn là
*tiêu chuẩn khác*, mà chỉ là phần mô tả phẩm chất của sát-đế-lợi. Sujato cũng dịch "But one
accomplished in knowledge and conduct…"; Walshe cũng "But".

Đánh giá: **có bước ngoặt, nhưng trước khi sửa là "có mà yếu"** — đủ để người đọc kỹ nhận
ra, chưa đủ để người đọc phổ thông không hiểu lệch. Sau khi thêm "nhưng" (và đổi ";" thành
"," ở cuối vế 2), bước ngoặt đã rõ mà không thêm nghĩa mới. Nếu người biên tập muốn mạnh
hơn nữa thì có thể dùng "còn … mới là", nhưng "mới" sẽ ngầm phủ định vế đầu — trong khi
Đức Thế Tôn tán thành *cả* bài kệ, nên tôi không đề nghị.

Một lưu ý ngoài phạm vi: câu mở mục 4 (dn3:2.1.1) dùng "Nhưng thưa ngài Gotama…", nối rất
tốt với "nhưng" ở cuối mục 3; giữ được cặp này thì mạch chuyển rõ hơn.

## Kết luận

**ĐẠT.** Không còn lỗi nghĩa; 6 nhóm chỉnh sửa đã áp dụng (5 nhẹ + 1 nặng về tác động), cùng
một chỉnh câu ở 1.27.11–1.27.12; các gợi ý còn lại ở mục Chất văn là tuỳ chọn, không bắt buộc.
Kiểm tra marker:

- `06-heritage.md`: 26/26 đoạn — `==> ĐẠT`
- `07-aristocrats.md`: 65/65 đoạn — `==> ĐẠT`
