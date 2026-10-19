# Hướng dẫn dịch — Kinh Ambaṭṭha (DN 3)

Tài liệu này là **quy chuẩn bắt buộc** cho mọi tệp trong `ban-dich/`. Mục tiêu: một bản
tiếng Việt hiện đại, người đọc phổ thông đọc hiểu được ngay, nhưng vẫn trung thành với bản
Pali đến từng chi tiết.

---

## 1. Nguyên tắc

1. **Dịch từ PLI là chính.** Tệp nguồn trong `nguon/sections/` có ba lớp: `PLI` (nguyên bản),
   `EN` (bản dịch của Bhikkhu Sujato) và `NOTE` (chú giải của Sujato). EN dùng để tham khảo
   cách hiểu; **khi EN và PLI khác nhau thì theo PLI**. Nhiều chỗ Sujato rút gọn hoặc diễn
   giải thoáng hơn nguyên bản.
2. **Tiếng Việt hiện đại.** Viết như người Việt hôm nay nói và viết. Không dùng lối văn
   biền ngẫu, không đảo ngữ cho "cổ kính". Câu dài thì cắt. Chủ đề ẩn thì làm rõ.
3. **Thuật ngữ Phật học: giữ âm Hán-Việt quen thuộc, mở ngoặc giải thích ngay lần đầu.**
   Ví dụ: "tỳ-kheo", "bà-la-môn", "sát-đế-lợi". Từ nào tiếng Việt thường đã đủ nghĩa thì
   dịch hẳn (xem §4).
4. **Không thêm, không bớt.** Không thêm chi tiết không có trong PLI, không bỏ mệnh đề nào.
   Nếu PLI lặp thì bản dịch cũng lặp — cái lặp ấy thường là dụng ý của bản kinh.
5. **Dấu `…` (peyyāla) phải khai triển đầy đủ.** PLI viết tắt bằng `…pe…` hoặc `…` để chỉ
   một đoạn lặp lại phía trước. Trong bản dịch **luôn viết ra đầy đủ**, không giữ dấu lược.
   *Ngoại lệ duy nhất:* khi đoạn lược ấy trùng nguyên khối với một đoạn đã dịch đầy đủ ở bài
   trước trong cùng dự án (ví dụ các tầng thiền-na và sáu thắng trí ở DN 3 trùng với DN 2 mục
   4.3.2), thì được tóm lược, **với điều kiện** phải có chú thích nói rõ đang tóm lược cái gì
   và chỉ người đọc đến bản đầy đủ. Không được tóm lược mà im lặng.
6. **Đoạn đánh dấu `(Sujato gộp đoạn này vào câu trước — dịch trực tiếp từ PLI)`**: không có
   EN để đối chiếu. Dịch thẳng từ PLI, đọc cả đoạn trước và đoạn sau để biết nó thuộc mạch nào.
7. **Không dịch máy.** Đọc cả đoạn rồi mới viết. Câu tiếng Việt phải tự nhiên khi đọc lên.

---

## 2. Giọng văn

Bài này không phải bài giảng mà là **một cuộc đối thoại có tranh chấp**, và đó là chỗ khó
nhất của nó. Giọng phải đổi theo nhân vật:

- **Đức Thế Tôn**: điềm tĩnh, lịch sự đến mức lạnh lùng. Ngài không mắng ai; Ngài hỏi, và
  câu hỏi tự nó dồn người ta vào chỗ không trả lời được. Khi Ngài kết luận thì ngắn và dứt
  khoát. **Không** làm Ngài thành người gay gắt, cũng không làm Ngài thành người nhún nhường.
- **Ambaṭṭha**: trẻ, kiêu, nóng, quen được nể. Khi bị dồn thì cáu, nói lấp, nói lảng. Giọng
  hắn phải **khác hẳn** giọng Đức Thế Tôn — câu ngắn hơn, nhiều từ đệm, nhiều câu hỏi ngược.
- **Pokkharasāti**: già, trọng, tự phụ nhưng biết điều. Giọng chậm và trang trọng.
- **Người kể chuyện**: trung tính, không bình luận, không thêm cảm thán.

Giữ nhịp: đoạn tranh luận thì câu ngắn; đoạn giảng giải thì câu dài hơn một chút. Đọc lên
phải nghe ra ai đang nói.

---

## 3. Xưng hô

Đây là chỗ dễ sai nhất. Bảng dưới là quy định, không tự đổi:

| Ai nói → ai | Pali | Tiếng Việt |
|---|---|---|
| Ambaṭṭha → Đức Thế Tôn | `bho gotama` | "thưa ngài Gotama" (kể cả khi anh ta đang cáu) |
| Ambaṭṭha → Đức Thế Tôn | `bhavaṁ gotamo` (1.5.1, 1.7.3–4) | "ngài Gotama" — kính ngữ ngôi thứ ba, khác `bho`; không thêm "thưa" |
| Pokkharasāti → Đức Thế Tôn | `bho gotama` | "thưa ngài Gotama" |
| Đức Thế Tôn → Ambaṭṭha | `ambaṭṭha` | gọi tên: "này Ambaṭṭha"; đại từ: **"ông"** |
| Đức Thế Tôn → Pokkharasāti | `brāhmaṇa` | "này bà-la-môn"; đại từ: **"ông"** |
| Đức Thế Tôn → các tỳ-kheo | `bhikkhave` | "này các tỳ-kheo" |
| Ambaṭṭha → các tỳ-kheo | — | "quý ngài" |
| người kể → Đức Thế Tôn | `bhagavā` | "Đức Thế Tôn" (không dùng "Đức Phật") |

- **Không dùng "ngươi", "mày", "thằng".** Dù Ambaṭṭha xúc phạm, Đức Thế Tôn vẫn gọi "ông".
  Cái sắc lạnh của Ngài nằm ở nội dung câu, không nằm ở đại từ.
- Ambaṭṭha gọi Đức Thế Tôn là "ngài", **không** gọi "ông" — hắn vẫn giữ lễ với một sa-môn.
- Khi Ambaṭṭha nói về Đức Thế Tôn với người khác: "sa-môn Gotama".
- Các tỳ-kheo gọi Ambaṭṭha: "ông".

---

## 4. Thuật ngữ

### 4.1. Nhân danh và địa danh

| Pali | Tiếng Việt |
|---|---|
| Ambaṭṭha | Ambaṭṭha (ghi chú: truyền thống Hán-Việt gọi là A-ma-trú) |
| Pokkharasāti | Pokkharasāti |
| Todeyya | Todeyya |
| Gotama | Gotama |
| Pasenadi | Pasenadi (vua nước Kosala) |
| Kosala | Kosala (Kiều-tát-la) |
| Ukkaṭṭhā | Ukkaṭṭhā |
| Icchānaṅgala | Icchānaṅgala |
| Sakya | Sakya (Thích-ca) |
| Kapilavatthu | Kapilavatthu (Ca-tỳ-la-vệ) |
| Manasākaṭa | Manasākaṭa |
| Cāṭuma | Cāṭuma |
| Pokkharasāti's park | khu vườn của Pokkharasāti |

Địa danh: **giữ nguyên dạng Pali**, mở ngoặc chú thích tên Hán-Việt quen thuộc ở lần đầu.
Không dịch nghĩa địa danh.

### 4.2. Thuật ngữ Phật học và Bà-la-môn

| Pali | Tiếng Việt | Ghi chú |
|---|---|---|
| bhagavā | Đức Thế Tôn | |
| tathāgata | Như Lai | |
| bhikkhu | tỳ-kheo | |
| samaṇa | sa-môn | |
| brāhmaṇa | bà-la-môn | |
| māṇava | thanh niên | chỉ học trò bà-la-môn trẻ; "thanh niên Ambaṭṭha" |
| jāti | giai cấp | khi nói về bốn giai cấp |
| vaṇṇa | giai cấp, đẳng cấp | |
| khattiya | sát-đế-lợi | giai cấp vua chúa, chiến binh |
| brāhmaṇa (giai cấp) | bà-la-môn | |
| vessa | phệ-xá | giai cấp thương nhân |
| sudda | thủ-đà-la | giai cấp lao động |
| caṇḍāla | chiên-đà-la | hạng cùng đinh; dịch thoáng: "kẻ hạ tiện" khi cần rõ nghĩa |
| ibbha | tiện dân | **từ khinh miệt** của bà-la-môn dành cho người ngoài giai cấp của họ |
| kaṇha | đen | dùng như lời miệt thị trong bài |
| vijjā | trí tuệ | trong cặp `vijjācaraṇa` |
| caraṇa | hạnh tu | trong cặp `vijjācaraṇa` |
| vijjācaraṇasampanna | có đủ trí tuệ và hạnh tu | **cặp khái niệm trung tâm của bài** |
| satthā | bậc đạo sư | |
| mante vāceti | dạy thần chú | |
| manta | thần chú | |
| yañña | tế lễ | |
| saddhā | tín thí | |
| bhojana | bữa ăn, đồ ăn cúng | |
| dāsī | nữ tỳ, người nữ nô tỳ | |
| dāsīputta | con của người nữ tỳ | **lời miệt thị nặng nhất trong bài** |
| mahāpurisa | bậc đại nhân | |
| lakkhaṇa | tướng | |
| dvattiṁsa mahāpurisalakkhaṇa | ba mươi hai tướng của bậc đại nhân | |
| brahmacariya | phạm hạnh | |
| nibbāna | Niết-bàn | |
| āsava | lậu hoặc | |
| jhāna | thiền-na | |
| upāsaka | người cư sĩ | |
| saṅgha | Tăng đoàn | |
| dhamma | Pháp | |
| ariya | cao thượng | | 
| brahmuno | Phạm Thiên | |

**Những từ Pali giữ nguyên, không dịch:** Ambaṭṭha, Pokkharasāti, Gotama, Ukkaṭṭhā,
Icchānaṅgala, Sakya, Kosala, Kapilavatthu, Manasākaṭa, Todeyya, Pasenadi, jambu (cây hồng
liên), sāla (cây sa-la), tinduka (cây thị), udumbara (cây sung), vaṭṭakā (chim cút),
kappāsa (cây bông), bimbikā / nimbikā (tên loại quả), karavīka (chim ca-lăng-tần-già).

### 4.3. Cụm cố định

| Pali | Tiếng Việt cố định |
|---|---|
| evaṁ me sutaṁ | Tôi nghe như vầy. |
| ekaṁ samayaṁ | Một thuở nọ |
| **cattāro apāyamukhāni** | **bốn lối rời bỏ** — `apāya` là "sự rời đi", `mukha` là "cửa, lối"; chỉ bốn lối tu khổ hạnh người ta chọn khi không đạt được trí tuệ và hạnh tu. Không dịch "đọa lạc" |
| **catūhi ṭhānehi … vijjācaraṇaṁ … anussāveyya** | "xưng bừa về trí tuệ và hạnh tu" |
| **dvīsu mahāpurisalakkhaṇesu kaṅkhati vicikicchati nādhimuccati na sampasīdati** | "còn phân vân về hai tướng của bậc đại nhân, còn nghi ngờ, chưa dứt khoát, chưa tin" |
| **khattiyaseṭṭha** | "sát-đế-lợi là cao quý nhất" |
| **porāṇaṁ aggaññaṁ** | "truyền thuyết cổ xưa về nguồn gốc" |

---

## 5. Câu công thức bắt buộc

Các câu dưới đây lặp lại nhiều lần trong bài. **Viết giống hệt từng chữ ở mọi lần xuất
hiện** (trừ đại từ nếu ngữ cảnh buộc phải đổi, và khi đổi thì ghi chú trong báo cáo).

| Pali | Tiếng Việt bắt buộc | Số lần |
|---|---|---|
| `idampissa hoti caraṇasmiṁ.` | **"Và điều này cũng thuộc về hạnh tu của vị ấy."** | 4 |
| `idampissa hoti vijjāya.` | **"Và điều này cũng thuộc về trí tuệ của vị ấy."** | 2 |
| `So aññadatthu vijjācaraṇasampannasseva paricārako sampajjati.` | **"Nhưng người ấy rốt cuộc chỉ trở thành kẻ hầu hạ cho người có đủ trí tuệ và hạnh tu."** | 4 |
| `Atha kho bhagavato etadahosi:` | **"Rồi Đức Thế Tôn nghĩ như thế này:"** | 4 |
| `Atha kho ambaṭṭho māṇavo … etadahosi:` | **"Rồi thanh niên Ambaṭṭha nghĩ như thế này:"** | 1 |
| `Atha kho brāhmaṇassa pokkharasātissa etadahosi:` | **"Rồi bà-la-môn Pokkharasāti nghĩ như thế này:"** | 1 |
| `Taṁ kiṁ maññasi, ambaṭṭha,` | **"Ambaṭṭha, ông nghĩ thế nào"** | 14 |
| `Atha kho bhagavā ambaṭṭhaṁ māṇavaṁ etadavoca:` | **"Rồi Đức Thế Tôn nói với thanh niên Ambaṭṭha:"** | 4 |
| `"Saccaṁ kira …"` | **"Nghe nói … có thật vậy không?"** | 4 |
| `… ti. "Saccaṁ, bho gotama."` | **"… — Thưa ngài Gotama, đúng vậy."** | 4 |
| `Evaṁ vutte, … tuṇhī ahosi.` | **"Khi nghe vậy, … im lặng."** | nhiều |
| `"Sādhu, sādhu, ambaṭṭha."` | **"Lành thay, lành thay, Ambaṭṭha!"** | 2 |

**Câu kết mỗi đoạn đối thoại:** khi Ambaṭṭha im lặng, Đức Thế Tôn nói:
`"Kiṁ pana, ambaṭṭha, tuṇhī …"` → **"Sao vậy, Ambaṭṭha, ông im lặng?"**

---

## 6. Định dạng

### 6.1. Khung một đoạn

Mỗi đoạn đúng theo mẫu này, **không thêm bớt dòng trống**:

```
<!-- seg: dn3:1.10.1 -->
Nội dung tiếng Việt của đoạn.

[Chú thích: Nội dung chú thích nếu có.]

<!-- seg: dn3:1.10.2 -->
...
```

- Mỗi đoạn trong nguồn là **một** marker `<!-- seg: dn3:X.Y -->`, đúng thứ tự nguồn,
  không bỏ sót, không lặp, không tự chế marker mới.
- Nếu nguồn là một tiêu đề (PLI dạng `2.1. Paṭhamaibbhavāda`) thì đoạn dịch là dòng tiêu đề
  markdown, xem §6.2.
- Chú thích viết ngay sau đoạn nó chú thích, dạng `[Chú thích: …]`, trên một dòng riêng.
  Nội dung chú thích dịch từ `NOTE` của Sujato, viết lại cho dễ hiểu, không cần sát chữ.
- Nếu một đoạn nguồn không có PLI và không có EN (marker rỗng), giữ marker rồi để trống —
  **không xóa marker**.

### 6.2. Quy tắc tiêu đề

Tiêu đề lấy số từ bản PLI. Luật:

- Số **một thành phần** (`1.`, `2.`, `3.` … `9.`) → **`##`**
- Số **nhiều thành phần** (`2.1.`, `2.2.` … `2.5.`) → **`###`**

Dạng viết: `## 2. Thanh niên Ambaṭṭha` — số, dấu chấm, khoảng trắng, rồi tên.

Tiêu đề tiếng Việt (dùng đúng các tên này, không tự đổi):

| Số | Pali | Tiếng Việt |
|---|---|---|
| 1. | Pokkharasātivatthu | Chuyện về Pokkharasāti |
| 2. | Ambaṭṭhamāṇava | Thanh niên Ambaṭṭha |
| 2.1. | Paṭhamaibbhavāda | Lần thứ nhất dùng chữ "tiện dân" |
| 2.2. | Dutiyaibbhavāda | Lần thứ hai |
| 2.3. | Tatiyaibbhavāda | Lần thứ ba |
| 2.4. | Dāsiputtavāda | Dùng chữ "con của người nữ tỳ" |
| 2.5. | Ambaṭṭhavaṁsakathā | Bàn về dòng dõi Ambaṭṭha |
| 3. | Khattiyaseṭṭhabhāva | Giai cấp sát-đế-lợi là cao quý nhất |
| 4. | Vijjācaraṇakathā | Trí tuệ và hạnh tu |
| 5. | Catuapāyamukha | Bốn lối rời bỏ |
| 6. | Pubbakaisibhāvānuyoga | Giống các ẩn sĩ thời xưa |
| 7. | Dvelakkhaṇādassana | Thấy hai tướng |
| 8. | Pokkharasātibuddhūpasaṅkamana | Pokkharasāti đến gặp Đức Thế Tôn |
| 9. | Pokkharasātiupāsakattapaṭivedanā | Pokkharasāti xin làm người cư sĩ |

### 6.3. Dấu câu

- Dùng ngoặc kép thẳng `"` — **tuyệt đối không dùng** `"` `"` `'` `'`.
- Trích dẫn lời nói nằm trong ngoặc kép; lời dẫn truyện nằm ngoài.
- Dùng gạch ngang dài `—` (em dash) để ngắt ý, có khoảng trắng hai bên.
- Số: viết bằng chữ khi nhỏ ("ba mươi hai tướng", "hai tướng"), bằng số khi là số hiệu
  tiêu đề. Năm tháng, số lượng lớn thì dùng số có dấu chấm phân cách ("1.000").

---

## 7. Từ ngữ cấm

**Tuyệt đối không dùng** các từ sau (đã bị loại vì sáo, mờ nghĩa, hoặc không phải tiếng Việt
hiện đại):

`như thị` · `nhất thời` · `bất khả tư nghì` · `vô lượng vô biên` · `chấp trước` ·
`Phật giáo đồ` · `như trên` · `lược đi` · `nói rằng là` · `một cách ... rằng` ·
`tiền thân là` (khi không có `pubbe` trong PLI)

Ngoài ra:

- **Không dùng dấu `...`** (ba chấm kiểu máy tính). Nếu cần lược, khai triển ra.
- **Không để nguyên chữ tiếng Anh** trong chính văn (trừ tên riêng trong ngoặc chú thích).
- **Không dùng "Đức Phật"** — luôn là "Đức Thế Tôn".
- **Không dùng "ngươi", "mày"** trong bất kỳ ngữ cảnh nào.

---

## 8. Danh sách kiểm tra trước khi ghi tệp

1. Đủ marker, đúng thứ tự, không lặp: `python3 kiem-tra-marker.py ban-dich/<tệp>.md` → `ĐẠT`
2. Không còn `…` ngoài `[Chú thích: …]`.
3. Không còn ngoặc kép cong, không còn `...`.
4. Các câu trong §5 viết đúng nguyên văn.
5. Tiêu đề đúng cấp `##` / `###` theo §6.2.
6. Đọc lại một lượt: có câu nào đọc lên thấy lạ không? Nếu có thì sửa.
