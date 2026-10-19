# C — Rà soát quả thứ nhất, quả thứ hai và ba tầng giới hạnh (DN 2, dn2:34–63)

**Tệp rà soát:**

- `10-first-fruit.md` — dn2:34–36, quả thứ nhất (33 đoạn, 6 chú thích)
- `11-second-fruit.md` — dn2:37–38, quả thứ hai (27 đoạn, 3 chú thích)
- `12-finer-intro.md` — dn2:39–42, chuyển tiếp sang các quả vi tế hơn (17 đoạn, 6 chú thích)
- `13-shorter-ethics.md` — dn2:43–45, giới hạnh ngắn (38 đoạn, 15 chú thích)
- `14-middle-ethics.md` — dn2:46–55, giới hạnh trung (39 đoạn, 13 chú thích)
- `15-long-ethics.md` — dn2:56–63, giới hạnh rộng lớn (35 đoạn, 14 chú thích)

**Nguồn đối chiếu:** `nguon/sections/10-first-fruit.md` … `15-long-ethics.md` (PLI, EN Sujato,
NOTE). Đối chiếu trực tiếp với PLI; bản EN và NOTE chỉ dùng để tham khảo. Tham chiếu
`HUONG-DAN-DICH.md` §3–§4 và ba tầng giới hạnh tương ứng ở DN 1
(`01-kinh-pham-vong/ban-dich/03-shorter-ethics.md`, `04-middle-ethics.md`, `05-large-ethics.md`).

**Ngày:** 2026-10-19.

**Cách làm:** đọc bản dịch từng tệp, mở tệp nguồn, đối chiếu từng segment với PLI; kiểm tra
danh sách, công thức lặp, chú thích, dấu câu và tính song song giữa 10 và 11. Sau khi sửa,
chạy lại `kiem-tra-marker.py` cho từng tệp đã sửa và đếm lại các công thức pin.

---

## 1. Kiểm tra tự động

| Tệp | Marker / segment | Chú thích | Kết quả |
|---|---:|---:|---|
| `10-first-fruit.md` | 33/33 | 6 | ĐẠT |
| `11-second-fruit.md` | 27/27 | 3 | ĐẠT |
| `12-finer-intro.md` | 17/17 | 6 | ĐẠT |
| `13-shorter-ethics.md` | 38/38 | 15 | ĐẠT |
| `14-middle-ethics.md` | 39/39 | 13 | ĐẠT |
| `15-long-ethics.md` | 35/35 | 14 | ĐẠT |
| **Tổng** | **189/189** | **57** | **6/6 ĐẠT** |

- Không có marker thiếu, thừa, lặp hay sai thứ tự; các đoạn được gộp nhiều segment (34.2–34.4,
  35.13–35.15, 37.16–37.18, 41.2–41.3) đều giữ đủ marker liền nhau trước đoạn gộp.
- Câu chốt `Idampissa hoti sīlasmiṁ` — “Và điều này cũng thuộc về giới hạnh của vị ấy.” — xuất
  hiện đúng **25 lần**: 13 có 8, 14 có 10, 15 có 7.
- Ở tệp 15, câu mở đầu `Yathā vā paneke…` xuất hiện đúng **7 lần**, câu kết
  `iti vā iti evarūpāya…` đúng **7 lần**, và 7 câu chốt giới hạnh đúng **7 lần**; cả 7 lần đều
  nguyên văn, không biến tấu.
- Không có dấu lược `…` trong chính văn, không có chữ Anh, không có từ trong danh sách cấm
  (`như thị`, `nhất thời`, `vô lượng vô biên`, `chấp trước`…), không có ngoặc kép cong.
- Số dấu `"` trong mỗi tệp đều chẵn; các dấu ngoặc kép mở/đóng đúng đoạn.

---

## 2. Lỗi đã sửa

| Vị trí | Vấn đề | Đã sửa thành / Đề xuất |
|---|---|---|
| `11-second-fruit.md` · dn2:37.20 | **NHẸ.** Câu thêm “cho ta”: PLI `rāsivaḍḍhako` chỉ là “người làm cho đống của cải cao thêm”, không có “cho ta”; cách thêm này còn phá thế song song với 37.5 và 37.10. | **Đã sửa:** “… làm kẻ gây dựng của cải” (bỏ “cho ta”). |
| `12-finer-intro.md` · dn2:40.3 | **NHẸ.** `sātthaṁ sabyañjanaṁ` = “có ý nghĩa và lời lẽ khéo léo”; bản cũ “có ý nghĩa và có lời lẽ” bỏ mất vế “well-phrased”, đọc như câu dịch máy. | **Đã sửa:** “… có ý nghĩa và lời lẽ khéo léo”. |
| `15-long-ethics.md` · dn2:56.2 | **NHẸ.** `kaṇahomaṁ` được DN 1 (1.21.2) dịch “bột gạo”; bản cũ “tấm vụn” cũng có cơ sở (`kaṇa` = gạo tấm/bột gạo), nhưng chưa khớp cụm chuẩn của bản dịch và lệch với cách hiểu nghi lễ dâng bột. | **Đã sửa:** “lễ dâng bột gạo” cho thống nhất với DN 1. |
| `15-long-ethics.md` · dn2:57.2 | **TRUNG BÌNH.** `usulakkhaṇaṁ` = “tướng mũi tên” (`usu` = mũi tên); bản cũ “tướng giáo” là giáo mác, một loại vũ khí không có trong danh sách Pali. | **Đã sửa:** “tướng mũi tên”. |
| `15-long-ethics.md` · dn2:57.2 | **NHẸ.** `mahiṁsalakkhaṇaṁ` được DN 1 dịch “tướng trâu”; “trâu rừng” là cách hiểu hẹp (buffalo hoang), trong khi `mahiṁsa` chỉ chung “trâu”. | **Đã sửa:** “tướng trâu” cho khớp DN 1. |
| `15-long-ethics.md` · dn2:61.2 (chính văn và chú thích) | **TRUNG BÌNH.** `viruddhagabbhakaraṇaṁ` bị dịch “thuật làm cho thai nhi trái vị” — nghĩa là gây ra tình trạng sai vị, trong khi chú giải và Sujato hiểu là **chữa trị** thai nhi bị cản trở cho nó sống được; DN 1 dịch “chữa cho thai nhi bị trắc trở”. | **Đã sửa:** “thuật chữa cho thai nhi bị trắc trở” (cả chính văn và chú thích). |
| `15-long-ethics.md` · dn2:62.2 | **NHẸ.** `paccañjanaṁ` là thuốc xoa/ thuốc nhỏ mắt đối trị; “thuốc xoa ngược” dịch sát chữ `pati + añj` nhưng tối nghĩa trong tiếng Việt. DN 1 dịch “thuốc xoa đối trị”. | **Đã sửa:** “thuốc xoa đối trị”. |
| `15-long-ethics.md` · dn2:63.4 | **NHẸ.** Cùng một `ariya` nhưng chỗ này dịch “cao quý”, trong khi 16.64.10 và 19.67.1 dịch “cao thượng”; đây là lỗi nhất quán đã được báo cáo D ghi nhận. | **Đã sửa:** “khối giới hạnh cao thượng này”. |

**Tổng: 8 lỗi, 9 chỗ sửa** (lỗi 61.2 sửa cả chính văn và chú thích). Không đụng marker, không
đụng bất kỳ câu công thức nào đã pin trong `HUONG-DAN-DICH.md` §4. Ba tệp đã sửa đều in
`==> ĐẠT` khi chạy `kiem-tra-marker.py`.

---

## 3. Đối chiếu quả thứ nhất và quả thứ hai

### 3.1. Khuôn truyện

Hai tệp theo cùng một khuôn: câu hỏi của vua → “Được chứ, này Đại vương.” → “Vậy thì… ta sẽ hỏi
lại ngài.” → “Này Đại vương, ngài nghĩ thế nào?” → mô tả nhân vật → “Vị ấy nghĩ như thế này:” →
“Thật lạ lùng thay!…” → so sánh với vua → quyết định xuất gia → bỏ tài sản/thân quyến (chỉ ở
quả thứ hai) → sống phạm hạnh → người của vua báo tin → vua không bắt về mà đảnh lễ, cúng
dường → kết luận “đây là quả thứ nhất/thứ hai…”.

### 3.2. Các cặp đoạn giống hệt

Đã so khớp từng cặp và xác nhận **17 cặp giống hệt từng chữ** (chỉ khác số đoạn):

`34.7/37.2`, `34.8/37.3`, `35.1/37.4`, `35.3/37.6`, `35.4/37.7`, `35.5/37.8`, `35.6/37.9`,
`35.8/37.11`, `35.9/37.12`, `35.11/37.14`, `35.12/37.15`, `35.16/37.19`, `36.1/38.1`,
`36.2/38.2`, `36.3/38.3`, `36.4/38.4`, `36.5/38.5`.

### 3.3. Các chỗ khác biệt

| Quả thứ nhất (tệp 10) | Quả thứ hai (tệp 11) | Khác biệt | Đánh giá |
|---|---|---|---|
| 35.2 | 37.5 | Nhân vật là nô lệ, có các chi tiết hầu hạ (dậy trước, đi ngủ sau, nhìn mặt chờ lệnh). | Đúng PLI: 37.5 không có các chi tiết ấy. |
| 35.7 | 37.10 | Lời tự mô tả của người nô lệ. | Đúng PLI: 37.10 đổi thành nông dân, gia chủ, người chịu khó làm ăn. |
| 35.10 | 37.13 | 35.10 chỉ nói “làm đúng như vậy”; 37.13 thêm “bỏ lại một khối tài sản lớn hay nhỏ, bỏ lại một vòng thân quyến lớn hay nhỏ”. | Đúng PLI: chi tiết bỏ tài sản/thân quyến chỉ có ở 37.13. |
| 35.13–35.15 | 37.16–37.18 | Lời báo tin, danh sách nghề và thân phận. | Đúng PLI; ba đoạn tương ứng một-một. |
| 35.17 | 37.20 | Lệnh gọi người ấy về, danh sách nghề. | Đúng PLI; đã sửa “cho ta” để khớp 37.5/37.10. |
| 36.6 | 38.6 | Kết luận “quả thứ nhất” / “quả thứ hai”. | Đúng PLI. |

### 3.4. Kết luận

Khuôn truyện khớp, không có đoạn nào bị chép lẫn giữa hai quả, không có chú thích hay danh sách
nghề nào đi sai chỗ. Khác biệt duy nhất ngoài dự kiến là “cho ta” ở 37.20, đã sửa. Sau khi sửa,
17 cặp đoạn dùng chung vẫn giống hệt từng chữ; 6 chỗ khác biệt đều rơi đúng vào chỗ PLI khác.

---

## 4. Đề xuất chưa áp dụng

### 4.1. Thống nhất danh sách nghề nghiệp giữa dn2:14/16 và dn2:34

Cùng một danh sách Pali xuất hiện 8 lần: một lần ở `03-question.md` (dn2:14.2–14.3) và bảy lần
trong `04-purana.md` … `09-sanjaya.md` (dn2:16.2–16.3 và các đoạn tương ứng). Bảy lần sau dùng
**cùng một bản dịch, giống hệt từng chữ**. Riêng `10-first-fruit.md` (dn2:34.3–34.4) dùng một
bản dịch khác:

| Pali | Bản 03–09 (7 chỗ) | Bản 10 (dn2:34) |
|---|---|---|
| assārohā | kỵ binh | người cưỡi ngựa |
| celakā | người cầm cờ | người cầm cờ hiệu |
| calakā | người làm phụ tá | người tùy tùng |
| piṇḍadāyakā | người lo cơm nước | người phân phát thức ăn |
| uggā | người làm thủ lĩnh chiến binh | các thủ lĩnh quân binh |
| rājaputtā | hoàng tử | các vương tử |
| mahānāgā | chiến binh dũng mãnh | những chiến binh giỏi |
| sūrā | anh hùng | những dũng sĩ |
| cammayodhino | lính mặc giáp da | quân lính mặc giáp da |
| dāsikaputtā | con của những người nô tỳ | con của các nữ nô lệ |
| mālakārā | thợ kết vòng hoa | thợ kết hoa |
| naḷakārā | thợ đan lát | thợ đan sậy |
| gaṇakā | kế toán | người giữ sổ sách |
| muddikā | người đếm bằng ngón tay | người tính đếm bằng ngón tay |

Không có mục nào bị thiếu hay thêm; tất cả đều là từ đồng nghĩa hoặc cách diễn đạt khác. Đây là
lỗi nhất quán, không phải lỗi nghĩa. **Đề xuất:** chọn một bản chuẩn cho toàn kinh. Vì 7/8 chỗ
đang dùng bản 03–09, cách ít thay đổi nhất là đưa 10 về bản ấy; nhưng bản 10 sát nghĩa hơn ở
`dāsikaputtā` (“con của các nữ nô lệ”) và `naḷakārā` (“thợ đan sậy”), nên cũng có thể chọn bản
10 rồi cập nhật 03–09. Không sửa trong lượt này vì tệp 03 ngoài phạm vi và đây là quyết định
biên tập xuyên tệp, không phải lỗi nghĩa của riêng tệp nào.

### 4.2. Ba chỗ tệp 15 khác DN 1 cần tác giả quyết

1. **`saṁvaraṇaṁ vivaraṇaṁ` (61.2).** 15 dịch “thuật che khăn và thuật mở khăn”, DN 1 dịch
   “dính hôn và ly dị” (theo Sujato: “engagement and divorce”). Cả hai đều là cách hiểu có cơ
   sở; chú thích của 15 đã tự nói “nhiều khả năng”. Nên đối chiếu chú giải trước khi chọn.
2. **`vossakammaṁ` (62.2).** 15 dịch “lễ nhượng đất”; DN 1 dịch “lễ phân định đất đai”; Sujato
   hiểu là “property settlement”. Nên thống nhất với DN 1. Ngoài ra chú thích của 15 ghi
   “cũng có bản hiểu là lễ cầu cho mưa tạnh” — cách hiểu này không thấy trong EN/NOTE của nguồn
   (EN chỉ ghi “for property settlement”), nên cần kiểm tra lại chú thích dù chọn cách dịch nào.
3. **`muddā` (60.2).** 15 dịch “làm dấu”, chú thích nói “có bản hiểu là lối tính bằng ngón
   tay”; DN 1 dịch “tính bằng ngón tay”, Sujato dịch “arithmetic”. Nên chọn “tính đếm” hoặc
   “tính bằng ngón tay” cho khớp DN 1; giữ “làm dấu” thì nên nói rõ đây là cách hiểu thiểu số.

### 4.3. Ghi chú nhỏ ở tệp 11

- `11-second-fruit.md` · dn2:37.13 (chú thích): “Đó là chỗ khác nhau **duy nhất** giữa hai
  trường hợp.” Thực ra hai trường hợp còn khác nhau ở nghề nghiệp và thân phận (chính chú thích
  trước đó đã nói). Đề xuất đổi “duy nhất” thành “rõ nhất” hoặc “đáng kể nhất”. Không sửa vì
  đây là chú thích tu từ, không ảnh hưởng nghĩa.

### 4.4. Ghi nhận khác biệt có lý (không sửa)

- **`aṅgaṁ` (56.2):** 15 dịch “xem tướng tay chân”, DN 1 dịch “xem điềm”. Chú giải
  (`Sv i.92`: `hattha-pādādisu… aṅgena`) hiểu đây là tướng tay chân để đoán tuổi thọ, nên cách
  dịch của 15 có cơ sở; Sujato không theo cách ấy mà chọn “augury”. Không sửa.
- **`saraparittāṇaṁ` (56.2, chú thích):** 15 ghi “bùa hộ mệnh chống tên bắn”; DN 1 theo Sujato
  ghi `sara` = “âm thanh”. Đa số từ điển và bản dịch hiểu `sara` = “mũi tên”, nên chú thích của
  15 vẫn đứng vững; đây là khác biệt giữa hai bản dịch, không phải lỗi.
- **`migacakkaṁ` (56.2):** 15 dịch “thuật xem dấu thú rừng”, DN 1 dịch “thuật đoán điềm qua
  thú rừng”. Cả hai đều diễn đạt được ý “điềm từ thú rừng”; 15 hơi nghiêng về dấu vết, nhưng
  không sai hẳn. Không sửa.

---

## 5. Điểm mạnh

- **Ba tầng giới hạnh bám sát DN 1.** 13 và 14 gần như dùng lại bản dịch đã rà soát của DN 1,
  chỉ đổi chủ thể “Sa-môn Gotama/Ngài” thành “tỳ-kheo/vị ấy” và thay câu kết bằng công thức
  `Idampissa hoti sīlasmiṁ`; không có lệch giáo lý hay lệch danh sách.
- **Tệp 15 là bản dịch công phu.** Các danh sách dài (30 mục ở 56.2, 27 mục ở 57.2, 10+1 dự
  đoán ở 58.2, 21 mục ở 61.2, 26 mục ở 62.2) đều đủ mục, đúng thứ tự; chú thích giải thích
  `homa`, `vijjā`, `muddā`, `sālākiya`, `sīlakkhandha`… rõ ràng và có ích.
- **Khuôn song song 10–11 được giữ nghiêm.** 17 cặp đoạn dùng chung giống hệt từng chữ; sáu chỗ
  khác biệt đều đúng chỗ PLI khác.
- **Công thức lặp nguyên vẹn.** 25 câu chốt giới hạnh, 7 câu mở đầu và 7 câu kết của tệp 15
  đều đúng số lần, đúng nguyên văn.
- **Văn phong tự nhiên.** Các câu dài được ngắt bằng dấu chấm phẩy hợp lý; không còn câu kiểu
  “có ý nghĩa và có lời lẽ” hay “thuốc xoa ngược” sau khi sửa.
- **Chú thích đặt đúng chỗ.** Không có chú thích nào gán sai đoạn hoặc mô tả sai chính văn
  (trừ ghi chú nhỏ ở 4.3).

---

## 6. Kết luận

**ĐẠT.**

Đã sửa 8 lỗi (9 chỗ) tại `11-second-fruit.md`, `12-finer-intro.md` và `15-long-ethics.md`;
cả ba tệp đều in `==> ĐẠT` khi chạy `kiem-tra-marker.py`. Các công thức pin còn nguyên: 25 câu
chốt giới hạnh (13: 8, 14: 10, 15: 7), 7 câu mở đầu và 7 câu kết ở tệp 15.

Các đề xuất còn lại (mục 4) chủ yếu là lựa chọn biên tập xuyên tệp — đáng chú ý nhất là việc
thống nhất danh sách nghề nghiệp giữa 10 và 03–09 — không phải lỗi nghĩa trong phạm vi 6 tệp.
Có thể ghép bản ngay; nếu muốn toàn kinh thật nhất quán thì nên xử lý mục 4.1 trước khi ghép.
