# Rà soát D — Chặng thiền định (dn2:64–82)

**Phạm vi:** `16-sense-restraint.md`, `17-mindfulness.md`, `18-contentment.md`,
`19-hindrances.md`, `20-first-jhana.md`, `21-second-jhana.md`, `22-third-jhana.md`,
`23-fourth-jhana.md` — 8 tệp, 95 segment (13 + 4 + 6 + 47 + 6 + 7 + 6 + 6).
**Ngày rà soát:** 2026-10-19.
**Cách làm:** đọc `HUONG-DAN-DICH.md` §3–§4, đọc bản dịch từng tệp, rồi mở tệp nguồn tương ứng
trong `nguon/sections/` và đối chiếu **từng segment với PLI**. Bản EN của Sujato và các dòng
`NOTE` chỉ dùng để tham khảo; chỗ EN rút gọn khác PLI thì lấy PLI làm chuẩn.
**Kiểm tra marker:** `python3 kiem-tra-marker.py ban-dich/<tệp>.md` — cả 8 tệp in `==> ĐẠT`
(đủ segment, đúng thứ tự, không lặp marker, không có marker lạ).

**Kết quả tóm tắt:** 5 lỗi nhỏ đã sửa trực tiếp; 4 điểm đề xuất chưa áp dụng; không có lỗi lớn
về giáo lý, không có sai lệch công thức bốn tầng thiền.

---

## 1. Bảng lỗi đã sửa

| Vị trí | Vấn đề | Đã sửa thành / Đề xuất |
|---|---|---|
| `17-mindfulness.md` — dn2:65.2 | Cụm “khi mang y, bát và các y phục” lặp nghĩa (“y” và “y phục” cùng chỉ y phục), không làm rõ `saṅghāṭi` (y ngoài) khác `cīvara` (y phục) trong PLI `saṅghāṭipattacīvaradhāraṇe`. | **Đã sửa:** “khi mang **y ngoài**, bát và y phục”. |
| `18-contentment.md` — dn2:66.3 | Thiếu hô cách `mahārāja` (“này Đại vương”) có trong PLI; các dụ ngôn ở tệp 19 và các dụ ngôn 20–23 đều giữ hô cách này. | **Đã sửa:** “Ví như, **này Đại vương**, một con chim: bay đi đâu, đôi cánh chính là hành lý duy nhất của nó.” |
| `19-hindrances.md` — dn2:67.3 (chú thích) | Chú thích nói “Ở đây dịch theo nghĩa thứ hai” (hiện tại), nhưng chính văn vẫn là “đặt chánh niệm **trước mặt**” — tức cách nói của nghĩa thứ nhất. Chú thích mô tả sai chính bản dịch. | **Đã sửa:** “**Bản dịch giữ cách nói ‘trước mặt’**, hàm ý đặt chánh niệm vào những gì đang diễn ra ngay trước mình.” |
| `19-hindrances.md` — dn2:68.2 | PLI `byāpādapadosā cittaṁ parisodheti` có cả `padosa`; bản dịch theo EN của Sujato (EN cũng rút gọn) nên mệnh đề cuối chỉ còn “sân hận”. Như vậy là dịch thiếu so với PLI. | **Đã sửa:** “…và làm cho tâm trong sạch khỏi sân hận **và ác ý**.” |
| `19-hindrances.md` — dn2:74.2–74.3 | Câu “cũng vậy, này Đại vương, **khi** vị ấy thấy trong mình…” là mệnh đề phụ (`khi…`) không có mệnh đề chính, câu bị treo. PLI `evameva kho… samanupassati` là mệnh đề chính, không có “khi”. | **Đã sửa:** bỏ “khi” → “…cũng vậy, này Đại vương, vị ấy thấy trong mình năm triền cái này đã được từ bỏ.” |

Cả 5 sửa đổi đều không đụng tới marker, không đụng tới bất kỳ câu công thức nào đã pin trong
`HUONG-DAN-DICH.md` §4.

---

## 2. Bảng đối chiếu bốn tầng thiền

| Tầng | Câu mở | Tân ngữ của câu “thấm đẫm…” | Đối chiếu PLI |
|---|---|---|---|
| **Sơ thiền** (20, dn2:75–76) | “Vị ấy ly khai các dục lạc, ly khai các pháp bất thiện, chứng và trú vào sơ thiền — tầng thiền thứ nhất — có tầm, có tứ, với niềm vui và sự dễ chịu sinh ra từ sự ly khai.” | “niềm vui và sự dễ chịu sinh ra từ sự ly khai” (`vivekajena pītisukhena`). | **Khớp.** 75.1 mở bằng `So vivicceva…`, **không** có `Puna caparaṁ` — đúng như bản dịch (không có “Lại nữa”). 75.2 và 76.2 đúng nguyên công thức §4.2. |
| **Nhị thiền** (21, dn2:77–78) | “Khi tầm và tứ đã lắng xuống, vị ấy chứng và trú vào nhị thiền — tầng thiền thứ hai — có sự an tĩnh nội tâm, có nhất tâm, không tầm không tứ, với niềm vui và sự dễ chịu sinh ra từ định.” | “niềm vui và sự dễ chịu sinh ra từ định” (`samādhijena pītisukhena`). | **Khớp.** 77.1 có `Puna caparaṁ`; đủ cả năm yếu tố: tầm-tứ lắng, an tĩnh nội tâm, nhất tâm, không tầm không tứ, lạc hỷ sinh từ định. 77.2 và 78.3 giống hệt nhau. |
| **Tam thiền** (22, dn2:79–80) | “Khi niềm vui đã phai nhạt, vị ấy chứng và trú vào tam thiền — tầng thiền thứ ba — sống với tâm xả, có chánh niệm và tỉnh giác, và tự mình cảm nhận nơi thân sự dễ chịu mà các bậc thánh vẫn nói đến: ‘Vị ấy sống với tâm xả, có chánh niệm, an trú trong sự dễ chịu.’” | “sự dễ chịu **không còn niềm vui**” (`nippītikena sukhena`). | **Khớp, và cố ý khác tầng 1–2.** 79.1 có `Puna caparaṁ`; `pītiyā virāgā`, `upekkhako`, `sato sampajāno`, `sukhañca kāyena paṭisaṁvedeti`, câu trích của các bậc thánh — đủ cả. 79.2/80.2 giữ nguyên bốn động từ nhưng đổi tân ngữ, đúng PLI. **Không được “sửa” cho giống tầng 1–2.** |
| **Tứ thiền** (23, dn2:81–82) | “Khi đã từ bỏ sự dễ chịu và đã từ bỏ sự đau khổ, và khi niềm vui cùng nỗi buồn trước đó đã lắng xuống, vị ấy chứng và trú vào tứ thiền — tầng thiền thứ tư — không khổ cũng không vui, với tâm xả và chánh niệm hoàn toàn trong sạch.” | **Không có câu “thấm đẫm…”**; câu tương ứng là “tỏa khắp thân này bằng **tâm thanh tịnh và trong sáng**” (`parisuddhena cetasā pariyodātena`). | **Khớp, và cố ý khác tầng 1–3.** 81.1 có `Puna caparaṁ`; đủ `sukha`/`dukkha`/`somanassa`/`domanassa`/`adukkhamasukha`/`upekkhāsatipārisuddhi`. 81.2/82.2 dùng `pharitvā… nisinno hoti` (tỏa khắp rồi ngồi), **không** dùng bốn động từ — đúng PLI, không phải thiếu. |

**Kiểm tra câu chốt quả:** câu “Thưa Đại vương, đây cũng là một quả của đời sống sa-môn thấy
được ngay trong đời này — vi diệu hơn và cao quý hơn những quả trước.” có **đúng 1 lần** ở cuối
mỗi tệp 20, 21, 22, 23; đếm toàn bộ `ban-dich/` được **11 lần** (20–30), khớp quy định §4.
Câu chữ khớp 100% với bản pin, không có biến thể.

**Về `Puna caparaṁ` và nhịp đọc:** đã kiểm tra đúng vị trí — 75.1 (sơ thiền) **không** có
`Puna caparaṁ`; 77.1, 79.1, 81.1 (nhị, tam, tứ thiền) **đều có** `Puna caparaṁ, mahārāja,
bhikkhu…`. Vì vậy việc 21/22/23 có câu dẫn “Lại nữa, này Đại vương.” đứng riêng, còn 20 không
có, là **đúng nguồn**, không phải lỗi. Nhận xét nhịp đọc: câu dẫn ngắn đứng riêng tạo một quãng
ngắt đều trước mỗi tầng, có tác dụng như dấu chuyển đoạn khi tụng đọc; nhưng khi đọc liền mạch
bằng mắt, nó là một câu không có vị ngữ nên hơi rời rạc, và làm mất sự liền mạch của tầng 1
(đi thẳng từ 74.4). **Đề nghị giữ nguyên**, vì đúng PLI và không sai nghĩa; nếu muốn mượt hơn
thì phải nhập câu dẫn vào câu công thức — tức sửa câu đã pin, không nên làm.

---

## 3. Đề xuất chưa áp dụng

| Vị trí | Vấn đề | Đề xuất |
|---|---|---|
| `19-hindrances.md` — dn2:68.3 | “Hôn trầm và thụy miên” là thuật ngữ Hán-Việt khó, chưa được giải thích ở lần đầu; trong khi “trạo cử và hối quá” có chú thích ngay ở 68.4. Như vậy không đều với quy chuẩn §3 (“thuật ngữ phải giải thích ngay trong ngoặc ở lần đầu xuất hiện”). | Thêm vào chú thích 68.3: “Hôn trầm là sự uể oải, nặng nề của tâm; thụy miên là sự buồn ngủ.” |
| `23-fourth-jhana.md` — dn2:81.2 | Chú thích nguồn của Sujato bị bỏ: “Tâm xả của tứ thiền không phải là sự mờ nhạt, thờ ơ, mà là một sự nhận biết sáng rỡ và tỏa chiếu.” Đây là chú thích hữu ích, nhất là vì câu “tâm thanh tịnh và trong sáng” dễ bị hiểu là trạng thái trống rỗng. | Thêm sau 81.2: `[Chú thích: Tâm xả của tứ thiền không phải là sự mờ nhạt, thờ ơ, mà là một sự nhận biết sáng rỡ và tỏa chiếu.]` |
| `22-third-jhana.md` — dn2:80.1 | Bốn động từ của công thức (“thấm đẫm, tràn ngập, làm đầy và tỏa khắp”) được dùng khi chủ ngữ là “chúng” (những hoa sen), không có tân ngữ; “làm đầy” và “tỏa khắp” hơi treo. PLI ở đây là bị động: `abhisannāni parisannāni paripūrāni paripphuṭāni`. | Cân nhắc dạng bị động: “chúng **được** thấm đẫm, tràn ngập, làm đầy và tỏa khắp bằng nước mát”; hoặc thêm “chính mình”. Không bắt buộc — nghĩa hiện tại vẫn rõ, và câu sau đã có “không phần nào… không được nước mát thấm nhuần”. |
| `15-long-ethics.md` 63.4 so với `16-sense-restraint.md` 64.10 và `19-hindrances.md` 67.1 | Cùng một tính từ `ariya` nhưng chỗ dịch “cao quý” (15.63.4), chỗ dịch “cao thượng” (16.64.10, 19.67.1). Chưa thống nhất toàn sách; đây là lỗi nhất quán, không phải lỗi nghĩa. | Chọn một cách gọi. Nếu chọn “cao thượng” (đang dùng trong hai tệp thuộc phạm vi này) thì sửa 15.63.4 — **ngoài phạm vi của tôi**; nếu chọn “cao quý” thì sửa 16 và 19. |

### Ghi nhận nhỏ (không cần sửa)

- `19-hindrances.md` 69.2: “**Về sau**, công việc làm ăn…” — PLI không có `aparena samayena`
  như bốn dụ ngôn sau; đây là hư từ nối thời gian, không đổi nghĩa. Có thể bỏ nếu muốn sát PLI
  tuyệt đối.
- `19-hindrances.md` 69.3/69.7: `dārabharaṇāya` chỉ nói “nuôi **vợ**”; bản dịch thêm “con”
  (“vợ con”). Đây là cách nói gộp quen thuộc, không sai hẳn, nhưng nếu muốn sát PLI thì bỏ “con”.
- `19-hindrances.md` 73.1: “**phải** đi qua một con đường sa mạc” — `paṭipajjeyya` là “lên
  đường”, không hàm ý bắt buộc; “phải” là thêm nhẹ, không ảnh hưởng nghĩa.
- `22-third-jhana.md` 79.1: “mà các bậc thánh **vẫn** nói đến” — “vẫn” thêm sắc thái “từ xưa
  đến nay”, không có trong PLI, nhưng đọc tự nhiên.
- `23-fourth-jhana.md` 81.1: `adukkhamasukhaṁ` dịch “không khổ cũng không vui” — thành ngữ
  Việt chấp nhận được; nếu muốn bám sát hơn thì “không khổ cũng không dễ chịu”, nhưng câu sẽ
  nặng hơn. **Giữ nguyên.**
- Đề bài có nhắc “năm triền cái ví với năm loại nước”; thực tế PLI so năm triền cái với
  **nợ, bệnh, ngục tù, nô lệ, sa mạc** — không phải nước. Bản dịch bám đúng năm ẩn dụ này
  (19.69–74). Các ẩn dụ nước chỉ thuộc ba tầng thiền đầu (bột tắm, hồ nước, sen), còn tứ thiền
  là ẩn dụ **vải trắng**. Không có lỗi ở điểm này.

---

## 4. Điểm mạnh

1. **Marker và cấu trúc:** 95/95 segment có marker, đúng thứ tự, không lặp, không sót; cả 8 tệp
   đều `==> ĐẠT`. Các segment bị Sujato gộp (69.5–69.7, 70.4–70.7, 71.4–71.5, 72.4–72.5,
   73.4–73.5, 74.3) đều được dịch đủ từ PLI, không bỏ sót.
2. **Công thức bốn tầng thiền:** câu mở, câu “thấm đẫm…”, câu chốt quả đều đúng khuôn §4.
   Đặc biệt, người dịch **không** “san phẳng” tam thiền và tứ thiền: `nippītikena sukhena`
   được giữ là “sự dễ chịu không còn niềm vui”; `parisuddhena cetasā pariyodātena` được giữ là
   “tâm thanh tịnh và trong sáng”, và tứ thiền không bị ép dùng lại bốn động từ của tầng 1–3.
   Đây là điểm dễ sai nhất của chặng này và đã làm đúng.
3. **Thuật ngữ:** `tầm`/`tứ`, `niềm vui`/`sự dễ chịu`, `tâm xả`, `nhất tâm`, `hộ trì các giác
   quan`, `chánh niệm và tỉnh giác`, `triền cái`, `thiền-na`/`tầng thiền` đều dùng đúng bảng
   §3.2 và nhất quán trong cả 8 tệp. Không có chỗ nào đổi `pīti` thành “sự dễ chịu” hay ngược lại.
4. **Ẩn dụ:** năm dụ ngôn triền cái đủ và đúng thứ tự (nợ → bệnh → ngục → nô lệ → sa mạc);
   cặp “chưa từ bỏ / đã từ bỏ” ở 74.1–74.3 đủ năm vế đối ứng (hết nợ, khỏi bệnh, ra khỏi ngục,
   được tự do, đến đất an toàn). Ba ẩn dụ nước (bột tắm, hồ nước, sen) giữ đủ bốn động từ và vế
   “không chỗ nào… không được thấm nhuần”. Ẩn dụ vải trắng giữ đúng hình ảnh “quấn kín từ đầu
   đến chân”, không thu gọn thành “khăn trùm đầu”.
5. **Chú thích:** đặt đúng chỗ (giải thích thuật ngữ ở lần xuất hiện đầu, chú thích dụ ngôn đặt
   ngay sau dụ ngôn), nội dung sát NOTE gốc, không có chú thích nào gán lệch segment.
6. **Văn phong:** câu tiếng Việt nhìn chung tự nhiên, giữ được nhịp liệt kê của bản gốc; không
   còn Pali/tiếng Anh trong chính văn (chỉ có trong chú thích, đúng quy ước); không còn dấu `…`
   trong chính văn; không có lỗi chính tả hay khoảng trắng bất thường.

---

## 5. Kết luận

**ĐẠT.** Sau khi sửa 5 lỗi nhỏ, chặng thiền định đã sạch về marker, thuật ngữ, ẩn dụ và công
thức bốn tầng thiền; không còn lỗi nào chặn việc phát hành. Bốn đề xuất ở mục 3 là tùy chọn
(không bắt buộc), trong đó đề xuất về `ariya` cần một lượt thống nhất chung với tệp 15 — ngoài
phạm vi rà soát này.
