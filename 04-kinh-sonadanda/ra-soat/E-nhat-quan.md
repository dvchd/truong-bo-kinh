# Rà soát E — Nhất quán thuật ngữ, xưng hô và nguồn tham khảo (DN 4)

**Phạm vi rà soát:** toàn bộ bản dịch DN 4 (7 tệp văn bản kinh, 297 đoạn), tập trung vào
`ban-dich/bang-thuat-ngu.md` và `ban-dich/nguon-tham-khao.md`.

**Tệp được phép sửa:** `ban-dich/bang-thuat-ngu.md`, `ban-dich/nguon-tham-khao.md`.

**Tệp chỉ đọc (đang được các rà soát viên khác sửa):** `00-gioi-thieu.md`, `00-title.md`,
`01-campa.md`, `02-sonadanda.md`, `03-buddha.md`, `04-second-thoughts.md`,
`05-brahmin.md`, `06-ethics-wisdom.md`, `07-conclusion.md`.

**Thời điểm chốt:** 09:45, sau khi các tệp 02, 05, 06, 07 vừa được sửa lần cuối (09:37–09:42).

**Phương pháp:** đọc từng đoạn theo marker `<!-- seg: dn4:X.Y -->`; đối chiếu Pali trong
`nguon/api_dn4.json` (297 khóa) và bản Sujato cùng API; đếm bằng script trên phần chữ của
7 tệp (không tính chú thích, nhan đề, marker); đối chiếu các tuyên bố trong
`nguon-tham-khao.md` với SuttaCentral suttaplex/bilarasuttas, mục lục *In the Buddha's Words*
và quy chuẩn của hai bài trước (DN 2, DN 3).

---

## Tóm tắt

- **24 điểm phát hiện:** 16 lỗi thực chất và 8 điểm bổ sung/vi chỉnh.
- **11 lỗi đã sửa trong hai tệp thuộc phạm vi:** 3 lỗi dữ kiện ở `nguon-tham-khao.md`,
  8 lỗi/nhầm lẫn ở `bang-thuat-ngu.md` (trong đó có 1 lỗi Pali và 1 lỗi nghĩa).
- **5 lỗi còn lại trong thân bản dịch** (không được sửa theo phân công):
  - **nặng:** `02-sonadanda.md` 5.19–5.20 dịch `rājabhogga` thành "đất vua ban" (đúng là
    "đất của vua") và thêm "khô" vào `satiṇakaṭṭhodaka`; câu 1.4 đã được sửa đúng nên
    cùng một công thức mà hai chỗ nói khác nhau;
  - **nhẹ:** `07-conclusion.md` 24.5 dùng "Xin Ngài" thay vì "thưa ngài Gotama";
  - **nhẹ:** `05-brahmin.md` 13.7 và 20.5 dùng "có vẻ đẹp rạng rỡ tột bậc", khác với
    "sắc vóc thanh tú tột bậc" ở 5.11/6.11 dù Pali giống hệt;
  - **nhẹ:** `02-sonadanda.md` chú thích 5.11 viết "Phạm thiên" thường, trong khi chính văn
    viết "Phạm Thiên".
- **Kết luận: CẦN SỬA.** Hai tệp thuộc phạm vi đã ĐẠT sau khi sửa. Toàn bản dịch còn 1 lỗi
  nghĩa đáng kể ở 5.19–5.20; nếu hai câu ấy được sửa theo 1.4 thì có thể chuyển sang ĐẠT
  (ba điểm nhẹ còn lại không chặn).

---

## A. Bảng thuật ngữ đối chiếu với bản dịch

Số lần đếm trên 7 tệp văn bản kinh (01–07), không tính `00-title.md` và lời giới thiệu.
"Đạt" nghĩa là cách dịch trong bảng khớp với cách dùng thực tế.

| Pali | Cách dịch trong bảng | Số lần | Nơi xuất hiện | Đối chiếu |
|---|---|---:|---|---|
| `sīla` | giới | 64 | 5.12, 6.12, 13.8, 14.8, 15.7, 16.6, 20.11, 21.4–22.10, 23.4–23.7 | Đạt |
| `sīla` | giới hạnh | 4 | 23.4 (ba tầng: ngắn, trung, rộng lớn) | Đạt — chỉ dùng đúng chỗ |
| `paññā` | tuệ | 32 | 06 (21.4–22.10, 23.4–23.7) | Đạt — không dùng "trí tuệ" cho `paññā` |
| `paññavā` | thông minh, sáng dạ | 5 | 13.9, 14.9, 15.8, 16.7, 20.12 | Đạt |
| `sīlapaññāṇa` | giới và tuệ | 4 (+1 tiêu đề) | 21.7, 21.12, 22.4, 22.9 | Đạt |
| `vaṇṇa` | sắc vóc | 10 | 5.11, 6.11, 14.4, 14.5, 17.3, 19.5, 19.6, 20.5, 20.10 | Đạt về nghĩa; xem B4 về công thức 13.7/20.5 |
| `jāti` | dòng dõi | 27 | 5.6–5.7, 6.4–6.5, 6.17, 6.46, 13.5, 14.6, 15.6, 16.4–16.5, 17.3, 19.5–19.6, 20.8, 20.10, 23.12 | Đạt |
| `manta` | thần chú | 14 | 5.10, 5.14, 13.6, 14.7, 15.4–15.5, 17.3, 19.5–19.6, 20.6–20.7, 20.10 | Đạt |
| `aṅga` | yếu tố | 23 | 11.5, 13.2, 13.4, 13.10, 14.1, 14.4, 14.10, 15.1, 15.4, 15.9, 16.1, 16.4, 16.8, 20.13, 21.1 | Đạt — "chi phần" không dùng |
| `khatta` | quản gia | 4 | 3.3, 3.4, 3.9, 3.12 | Đạt |
| `vijjācaraṇa` | trí tuệ và hạnh tu | 4 | 2.4, 3.7, 6.22, 6.29 | Đạt — `vijjā` = "trí tuệ", khác `paññā` = "tuệ" |
| `jhāna` | sơ thiền, nhị thiền, tam thiền, tứ thiền | 4 | 23.7–23.10 | Đạt — "thiền-na" chỉ trong chú thích 23.4 |
| `nibbāna` | — (đã bỏ) | 0 | — | Đã bỏ khỏi bảng |
| `yañña` | — (đã bỏ) | 0 | — | Đã bỏ khỏi bảng |
| `brāhmaṇa` | bà-la-môn | 130 | toàn bài | Đạt |
| `māṇavaka` | thanh niên | 7 | 5.14, 20.1, 20.5–20.6, 20.8, 20.10 | Đạt |
| `gahapati` | gia chủ | 13 | 1.0, 2.1, 2.8, 3.2, 3.4, 3.9, 3.12, 6.25, 9.3, 23.4 | Đạt |
| `ajjhāyaka` | người tụng đọc | 4 | 5.10, 13.6, 14.7, 20.6 | Đạt |
| `suja` | muôi tế lễ | 5 | 13.9, 14.9, 15.8, 16.7, 20.12 | Đạt |
| `rājabhogga` | đất của vua | 1 (01) + 2 (02) | 1.4; 5.19–5.20 | **Không đạt ở 02**: 5.19–5.20 còn "đất vua ban" |
| `brahmadeyya` | ân tứ của vua ban cho bà-la-môn | 3 | 1.4, 5.19, 5.20 | Đạt |
| `titthakara` | người sáng lập giáo phái | 1 | 6.28 | Đạt |
| `upāsaka` | người cư sĩ | 2 | 24.0, 24.5 | Đạt |
| `saṅgha` | Tăng đoàn | 4 | 24.4, 24.6, 25.1, 25.2 | Đạt |
| `Pātimokkha` | giới bổn Pātimokkha | 1 | 23.4 | Đạt |
| `pañca nīvaraṇa` | năm triền cái | 3 | 23.4, 23.6, 23.7 | Đạt |
| `mahāpurisalakkhaṇa` | tướng của bậc đại nhân | 5 | 5.10, 6.23, 13.6, 14.7, 20.6 | Đạt |
| `Sakya` | Sakya (Thích-ca) | 4 | 2.2 (×2), 3.5 (×2) | Đã bổ sung vào bảng |
| `khattiya` | Sát-đế-lỵ | 2 | 6.17, 6.25 | Đã bổ sung vào bảng |
| `brahmacariya` | phạm hạnh | 4 | 2.6, 23.4 (×2), 23.13 | Đã bổ sung vào bảng |
| `sugata` | Thiện thệ | 3 | 2.4, 3.7, 6.22 | Đã bổ sung vào bảng |

**Kết luận mục A:** tám cặp thuật ngữ trọng tâm đều nhất quán:
`sīla` → "giới", `paññā` → "tuệ", `vaṇṇa` → "sắc vóc", `jāti` → "dòng dõi",
`manta` → "thần chú", `aṅga` → "yếu tố", `khatta` → "quản gia",
`vijjācaraṇa` → "trí tuệ và hạnh tu". Ngoại lệ duy nhất là `rājabhogga` ở 02 5.19–5.20.

---

## B. Lỗi nhất quán còn lại trong thân bản dịch

| # | Đoạn | Hiện tại | Vấn đề | Mức | Đề nghị |
|---|---|---|---|---|---|
| B1 | 02 5.19, 5.20 | "đầy cỏ khô, củi và nước… là đất vua ban" | `satiṇakaṭṭhodaka` = "có cỏ, củi và nước", không có "khô"; `rājabhogga` = đất thuộc quyền vua, không phải "vua ban" (việc ban nằm ở `dinnaṁ`). Câu 1.4 đã sửa thành "đầy cỏ… là đất của vua", nên 5.19–5.20 lặp lại công thức ấy với hai chữ sai | **Nặng** | Chép đúng câu 1.4 cho cả hai đoạn |
| B2 | 02 5.19, 5.20 | "là đất vua ban, do vua… ban cho, là ân tứ của vua ban cho bà-la-môn" | Hệ quả của B1: "ban" lặp ba lần trong một câu, hai lần là do dịch sai `rājabhogga` | **Nặng** | "là đất của vua, do vua… ban cho, là ân tứ của vua ban cho bà-la-môn" |
| B3 | 07 24.5 | "Xin Ngài nhận con làm người cư sĩ…" | Quy ước Soṇadaṇḍa → Đức Thế Tôn là "thưa ngài Gotama"; "Ngài" là đại từ thay thế, không sai hẳn, nhưng lệch quy ước ở câu quy y | Thấp | "Thưa ngài Gotama, xin ngài nhận con…" (giữ "ngài" thường) |
| B4 | 05 13.7, 20.5 | "có ngoại hình đẹp, dễ nhìn, dễ mến, có vẻ đẹp rạng rỡ tột bậc" | Pali 5.11 = 6.11 = 13.7 = 20.5 (`abhirūpo… paramāya vaṇṇapokkharatāya samannāgato…`), nhưng 5.11/6.11 dịch "dung mạo đẹp đẽ… sắc vóc thanh tú tột bậc", còn 13.7/20.5 dịch khác; `vaṇṇa` không hiện trong cụm "vẻ đẹp rạng rỡ" | Thấp | Thống nhất theo 5.11/6.11: "sắc vóc thanh tú tột bậc" |
| B5 | 02 chú thích 5.11 | "ánh sáng như Phạm thiên" | Cùng một chú thích dùng "Phạm thiên" thường, trong khi chính văn 5.11 và 03 6.11 viết "Phạm Thiên"; không thống nhất cách viết hoa | Thấp | "Phạm Thiên" cho thống nhất |

**Ghi chú:** B1 và B2 là cùng một câu ở hai đoạn, nên thực tế chỉ cần sửa hai dòng. Đây là
lỗi đáng kể nhất còn lại vì 1.4 đã đúng, người đọc thấy ngay sự khác nhau giữa hai lần
cùng một công thức.

**Những điểm đã kiểm tra, không còn lỗi:**

- `Đức Phật`: 0 lần trong cả 7 tệp; chỉ dùng "Đức Thế Tôn".
- Đại từ thô: 0 lần "ngươi", "mày", "thằng".
- Đức Thế Tôn gọi Soṇadaṇḍa: "này bà-la-môn", đại từ "ông"; 0 lần "ngài" khi Ngài nói với ông.
- Soṇadaṇḍa gọi Đức Thế Tôn: "ngài Gotama" (24.4, 24.6), "thưa ngài Gotama" (24.10);
  ngoại lệ duy nhất là "Xin Ngài" viết hoa ở 24.5 (B3).
- 500 bà-la-môn gọi Soṇadaṇḍa: "thưa ngài Soṇadaṇḍa" (2.1, 5.1); Soṇadaṇḍa gọi họ:
  "thưa quý vị" (2.1, 20.1, 20.2).
- 297/297 marker đoạn, khớp `keys_order` của `api_dn4.json`.

---

## C. Lỗi trong `nguon-tham-khao.md`

| # | Chỗ | Lỗi | Căn cứ | Đã sửa |
|---|---|---|---|---|
| C1 | Bảng "Nguyên bản" | PTS **i.111–127** | SuttaCentral suttaplex của DN 4 ghi `volpages` = PTS 1.111…1.126; đoạn cuối của bài nằm ở 1.126, bài kế tiếp bắt đầu 1.127 | **i.111–126** |
| C2 | Mục "Các bản dịch khác" | "Bhikkhu Bodhi (chủ biên), *In the Buddha's Words* (Wisdom, 2005) — có trích đoạn phần lập luận về giới và tuệ" | Mục lục *In the Buddha's Words* không có DN 4; các bài Trường Bộ được trích là DN 5, 15, 16, 21, 26, 31, không có Soṇadaṇḍa. Tuyên bố này không có cơ sở | **Đã bỏ** |
| C3 | Mục "Bản Hán tương ứng" | "bản Hán **cổ nhất**" | SuttaCentral ghi bản DA 22 là bản đầy đủ (type "full"); không có bản Hán đầy đủ thứ hai để so, nên "cổ nhất" là so sánh không có cơ sở. Chữ "đầy đủ" mới đúng điều cần nói | **"bản Hán đầy đủ"** |
| C4 | Bảng "Nguyên bản" + ghi chú | Chỉ ghi "chú thích của Bhikkhu Sujato", không nói có chú thích của người dịch | Bản dịch có 30 chú thích: 28 chú thích Sujato (1.1, 1.2, 1.3, 1.4, 2.1, 5.2, 5.6, 5.11, 5.14, 6.10, 6.16, 6.24, 6.25, 6.28, 6.30, 6.31, 6.32, 6.46, 8.5, 9.1, 9.3, 11.3, 13.9, 14.1, 22.1, 22.10, 23.7, 26.13) và 2 chú thích của người dịch (0.2, 23.4) | **Đã thêm đoạn nói rõ** |

**Những tuyên bố đã kiểm tra và thấy đúng:**

- **297 đoạn** — khớp đúng 297 khóa của `nguon/api_dn4.json` (kể cả `0.1`, `0.2`).
- **DA 22 / T i 094a18** — đúng; bản dịch Hán bắt đầu ở 94a19, còn tham chiếu kinh là 94a18.
- **SHT Sutta 56 (SHT 1251, 1352c)** — đúng theo `parallels` của SuttaCentral.
- **SF 42 (Hartmann 1989: 57–61)** — đúng.
- **MN 95 (Caṅkī) và MN 36** — đúng; MN 95 có công thức lập luận, MN 36 có khối mô tả
  con đường tu tập.
- **Vị trí thứ tư, sau Kinh Ambaṭṭha** — đúng.
- **Peyyāla ở mục 2–3 và mục 6** — đúng: root có `…pe…` ở 5.9–6.29, và 23.4 mở đầu bằng
  `…pe…` cho trọn khối con đường tu tập.
- **Khối văn ấy đã dịch đầy đủ ở DN 2, mục 4.3** — đúng; `02-kinh-sa-mon-qua/ban-dich/`
  có các tệp `12-finer-intro.md`…`16-...` với tiêu đề §4.3.
- **8.000 từ** trong lời giới thiệu — phù hợp với số đo nội dung (khoảng 8.050 từ không
  tính chú thích/marker).

---

## D. Thuật ngữ thiếu đã bổ sung

| Thuật ngữ | Cách dịch | Vì sao cần | Đoạn |
|---|---|---|---|
| `Sakya` | Sakya (Thích-ca) | Xuất hiện 4 lần trong công thức giới thiệu Đức Thế Tôn; người đọc cần biết đây là dòng họ, không phải địa danh | 2.2, 3.5 |
| `khattiya` | Sát-đế-lỵ | Xuất hiện trong lập luận về bốn giai cấp; nếu không có trong bảng, người đọc dễ nhầm với `vaṇṇa` | 6.17, 6.25 |
| `brahmacariya` | phạm hạnh | Là khái niệm trung tâm của đời sống xuất gia trong bài; xuất hiện ở phần mở đầu và đoạn cuối mục 6 | 2.6, 23.4, 23.13 |
| `sugata` | Thiện thệ | Một trong chín danh hiệu trong công thức ca ngợi; nếu thiếu, công thức bị hiểu như một chuỗi tính từ rời | 2.4, 3.7, 6.22 |

**Cân nhắc nhưng không thêm:** `yojana` ("do-tuần", 6.46) đã được dịch quen thuộc;
`kammavāda` ("chủ trương hành động có quả báo", 6.16) là một cụm miêu tả hơn là thuật ngữ
cố định; `sattussada` ("đông đúc sinh vật") là tính từ của công thức địa danh. Cả ba không
phải thiếu nghiêm trọng.

---

## E. Xưng hô — đối chiếu quy ước

| Quy ước | Kết quả | Ghi chú |
|---|---|---|
| "Đức Thế Tôn", không "Đức Phật" | **Đạt** | 0 lần "Đức Phật" trong 7 tệp |
| Đức Thế Tôn → Soṇadaṇḍa: "này bà-la-môn" + "ông" | **Đạt** | 9 lần "này bà-la-môn"; không có "ngài" khi Ngài nói với ông |
| Soṇadaṇḍa → Đức Thế Tôn: "thưa ngài Gotama" | **Đạt, 1 ngoại lệ nhẹ** | 24.4, 24.6, 24.10 dùng "ngài Gotama"; 24.5 "Xin Ngài" viết hoa (B3) |
| Không "ngươi", "mày", "thằng" | **Đạt** | 0 lần |
| 500 bà-la-môn → Soṇadaṇḍa: `bhavaṁ soṇadaṇḍo` | **Đạt** | Bảng cũ ghi sai `bho soṇadaṇḍa`; đã sửa thành `bhavaṁ soṇadaṇḍo` |
| Soṇadaṇḍa → 500 bà-la-môn: `bho`, `bhavanto`, `bhonto` | **Đạt** | Đã thêm `bhavanto`, `bhonto` vào bảng |
| `bhavaṁ gotamo` (14 lần) | **Đạt** | Đã thêm ghi chú: dịch là "ngài Gotama", dùng trong lời cả hai phía |

---

## F. Các sửa đổi đã làm trong hai tệp thuộc phạm vi

### `ban-dich/nguon-tham-khao.md`

1. PTS i.111–127 → **i.111–126**.
2. Bỏ dẫn *In the Buddha's Words* (không có DN 4).
3. "bản Hán cổ nhất" → **"bản Hán đầy đủ"**.
4. Thêm đoạn: 28 chú thích Sujato + 2 chú thích người dịch (0.2, 23.4).

### `ban-dich/bang-thuat-ngu.md`

5. `Soṇadaṇḍa`: "học vị cao" → **"học thức uyên bác"** (tránh nghĩa bằng cấp hiện đại).
6. Thêm `Sakya` (mục 1).
7. "năm chữ" → **"năm yếu tố"** (mục 2).
8. Thêm ghi chú `paññavā` = "thông minh, sáng dạ" (mục 2).
9. Thêm `khattiya` (mục 3).
10. `rājabhogga`: "đất vua ban" → **"đất của vua"**, kèm ghi chú `dinnaṁ` mới là "ban cho".
11. Bỏ `yañña` (0 lần; "tế lễ" không phải từ của bài).
12. Thêm `brahmacariya`, `sugata`; sửa ghi chú `vijjācaraṇa` (thêm 6.29 và phân biệt
    `vijjā`/`paññā`).
13. `jhāna`: "thiền-na" → **"sơ thiền, nhị thiền, tam thiền, tứ thiền"**; ghi rõ "thiền-na"
    chỉ có trong chú thích 23.4.
14. Bỏ `nibbāna` (0 lần).
15. Bảng xưng hô: `bho soṇadaṇḍa` → **`bhavaṁ soṇadaṇḍo`**; thêm `bhonto`; ghi chú
    `bhavaṁ gotamo` (14 lần); "đại từ 'ông'" → "khi cần đại từ thì dùng 'ông'".
16. Ghi chú `sīla`/`paññā`: chỉ rõ "giới hạnh" chỉ dùng ở 23.4 (ba tầng), không phải
    "đoạn con đường tu tập" nói chung.
17. Ghi chú `imināpaṅgena`: thêm chi tiết Pali chỉ ghi rõ 3 lần (5.4, 5.7, 6.5), phần còn
    lại lược bằng peyyāla.
18. `brahmadeyya`: "cho" → **"ban cho"** cho khớp chính văn.
19. `vijjācaraṇa`: "ở phần kết (6.29)" → **"ở 6.29"** (6.29 không phải phần kết bài).

---

## G. Kết luận

**Hai tệp thuộc phạm vi: ĐẠT.** Sau 19 điểm sửa, bảng thuật ngữ phản ánh đúng cách dùng
thực tế; nguồn tham khảo không còn tuyên bố sai về PTS, về *In the Buddha's Words* hay về
"bản Hán cổ nhất", và đã ghi đủ công lao của cả Sujato lẫn người dịch.

**Toàn bản dịch: CẦN SỬA.** Lỗi nặng nhất còn lại là `02-sonadanda.md` 5.19–5.20: cùng một
công thức địa danh với 1.4 nhưng dịch `rājabhogga` thành "đất vua ban" và thêm "khô" vào
`satiṇakaṭṭhodaka`; câu 1.4 đã đúng nên mâu thuẫn hiện rõ. Sửa hai câu này theo 1.4 là đủ
để hết lỗi nghĩa. Ba điểm nhẹ còn lại (07 24.5 "Xin Ngài"; 05 13.7/20.5 lệch công thức;
02 chú thích 5.11 "Phạm thiên") không chặn việc chuyển sang ĐẠT, nhưng nên sửa để bản dịch
nhất quán hoàn toàn.

**Số lỗi:** 16 lỗi thực chất (11 đã sửa trong phạm vi, 5 còn lại trong thân bản dịch) và
8 điểm bổ sung/vi chỉnh; tổng 24 điểm.
