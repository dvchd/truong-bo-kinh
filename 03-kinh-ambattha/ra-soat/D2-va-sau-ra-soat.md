# D2 — Báo cáo sửa lỗi sau rà soát

## 1. Tóm tắt

Đã xử lý năm việc nêu trong yêu cầu, chỉ sửa `ban-dich/08-knowledge-conduct.md` và
`ban-dich/09-four-causes.md`. Không đổi số marker, không đổi thứ tự, không thêm hay bớt
marker. Cả hai tệp đều qua `kiem-tra-marker.py` với kết quả `==> ĐẠT`.

Các khối peyyāla ở 2.2.8, 2.2.10, 2.2.12, 2.2.14, 2.2.17 và 2.2.18 đã được khai triển đầy
đủ. Riêng 2.2.7 vẫn tóm lược theo ngoại lệ §1.5, nhưng đã có chú thích ngay tại chỗ nói rõ
đang tóm lược những bước nào và chỉ người đọc đến Kinh Sa-môn Quả (DN 2), mục 4.3.2.

## 2. Bảng việc đã làm

| Việc | Tệp | Đoạn | Kết quả |
|---|---|---|---|
| Rà lại thuật ngữ `apāyamukha`, sửa các câu đọc lủng củng sau khi đổi sang "lối rời bỏ" | `09-four-causes.md` | 2.3.1, 2.3.6, 2.3.10, 2.3.13, 2.3.17, 2.3.18 | Đã sửa 6 câu. Không còn cụm "căn nguyên đọa lạc" hay "đọa lạc" trong tệp |
| Khai triển bốn tầng thiền-na và bốn ví dụ đi kèm | `08-knowledge-conduct.md` | 2.2.8, 2.2.10, 2.2.12, 2.2.14 | Viết đủ công thức thiền-na, phần tỏa khắp thân, ví dụ và phần ứng dụng: bột tắm nhào kỹ, hồ nước có mạch phun, hoa súng và hoa sen trong nước, người quấn vải trắng |
| Khai triển ví dụ viên ngọc lưu ly | `08-knowledge-conduct.md` | 2.2.17 | Đủ tám mặt, đủ các màu chỉ (xanh, vàng, đỏ, trắng hoặc vàng nhạt), đủ cảnh người có mắt sáng cầm ngọc nhìn kỹ và lặp lại trọn vẹn lời nhận xét |
| Khai triển sáu thắng trí | `08-knowledge-conduct.md` | 2.2.18 | Viết đủ thân do tâm tạo, mười phép thần thông, thiên nhĩ, tha tâm với 16 trạng thái, túc mạng, thiên nhãn và tri kiến đoạn tận lậu hoặc |
| Thêm chú thích peyyāla cho khối con đường tu tập | `08-knowledge-conduct.md` | 2.2.7 | Chú thích nêu rõ Pali dùng peyyāla, liệt kê các bước bị tóm lược, nói rõ bản dịch tóm lược và chỉ DN 2 mục 4.3.2 |
| Thêm gloss các thuật ngữ xuất hiện lần đầu | `08-knowledge-conduct.md` | 2.2.3, 2.2.7, 2.2.8, 2.2.12, 2.2.17, 2.2.18 | Đã thêm 6 chú thích gloss, không lặp lại về sau; riêng 2.2.7 thay chú thích cũ bằng bản mở rộng (chi tiết ở mục 4) |
| Thêm gloss cho "ba minh" và "bà con chúng ta" | `09-four-causes.md` | 2.5.4 | Đã thêm chú thích phân biệt ba bộ Vệ-đà với ba minh của Phật, và giải thích cách gọi Phạm Thiên |
| Dịch lại `sācariyaka` theo nghĩa truyền thống, phe phái | `09-four-causes.md` | 2.4.2, 2.4.4, 2.4.5, 2.4.7, 2.4.11, 2.4.15, 2.4.18, 2.5.1, 2.5.2 | Đã đổi đủ 9 chỗ; cập nhật chú thích tại 2.4.2 |
| Khôi phục sự leo thang `ceva ... ca` | `09-four-causes.md` | 2.5.1, 2.5.2 | Đã dùng cấu trúc "chẳng những ... mà còn ...", bỏ cách nói "thiếu cả bốn lối rời bỏ" |
| Kiểm tra marker và hình thức | cả hai tệp | toàn bộ | 31/31 và 44/44 marker; cả hai `==> ĐẠT` |

## 3. Số từ trước và sau

Số liệu lấy từ dòng "số từ nội dung" của `kiem-tra-marker.py` (không tính tiêu đề và marker).
Cột "tổng số từ" là kết quả `wc -w`, dùng để đối chiếu thêm.

| Tệp | Trước (nội dung) | Sau (nội dung) | Chênh lệch | Trước (`wc -w`) | Sau (`wc -w`) |
|---|---:|---:|---:|---:|---:|
| `ban-dich/08-knowledge-conduct.md` | 1.560 | 3.120 | +1.560 | 1.637 | 3.168 |
| `ban-dich/09-four-causes.md` | 1.248 | 1.312 | +64 | 1.365 | 1.423 |

## 4. Các gloss đã thêm

Mỗi thuật ngữ chỉ được giải thích một lần, ở chỗ xuất hiện đầu tiên trong tệp. Gloss đặt
trong `[Chú thích: ...]` ngay sau đoạn, không chen vào lời Phật.

| Thuật ngữ | Đoạn | Nội dung gloss |
|---|---|---|
| thắng trí | 2.2.3 | Sự hiểu biết trực tiếp, vượt xa hiểu biết thông thường, có được nhờ thiền định |
| năm triền cái | 2.2.7 | Nêu đủ năm: tham dục, sân hận, hôn trầm và thụy miên, trạo cử và hối quá, hoài nghi |
| thiền-na, tầm, tứ | 2.2.8 | Thiền-na là tầng định sâu, tâm lắng đọng và hợp nhất; tầm là hướng tâm tới đối tượng; tứ là giữ tâm nơi đối tượng ấy |
| tâm xả | 2.2.12 | Tâm bình đẳng, không thiên vị, không bám vào sự dễ chịu hay khó chịu |
| sắc, bốn đại | 2.2.17 | "Sắc" chỉ vật chất, không phải màu; bốn đại là đất, nước, lửa, gió |
| lậu hoặc | 2.2.18 | Những ô nhiễm sâu kín của tâm, gồm lậu hoặc của dục, của hữu và của vô minh |
| ba minh, bà con chúng ta | 2.5.4 | "Ba minh" là ba bộ Vệ-đà của bà-la-môn, không phải ba minh của Phật; "bà con chúng ta" là cách gọi Phạm Thiên theo thần thoại bà-la-môn, bốn giai cấp sinh ra từ các phần thân của Ngài |

Chú thích tại 2.2.7 gộp hai nội dung trong cùng một dòng: gloss "năm triền cái" và chú thích
peyyāla. Chú thích tại 2.4.2 cũng được viết lại để khớp với cách dịch mới của `sācariyaka`.

## 5. Peyyāla đã khai triển

- **2.2.8, 2.2.10, 2.2.12, 2.2.14**: mỗi đoạn nay có đủ bốn phần: công thức thiền-na, phần
  thấm đẫm và tỏa khắp thân, ví dụ tương ứng, rồi lặp lại phần ứng dụng. Bốn ví dụ lần lượt
  là bột tắm nhào kỹ trong chậu đồng, hồ nước sâu có mạch nước phun từ lòng hồ, hoa súng
  xanh và hoa sen hồng, hoa sen trắng chìm trong nước, và người quấn kín mình bằng vải trắng.
- **2.2.17**: ví dụ ngọc lưu ly được viết đủ, gồm tám mặt, mài giũa kỹ, trong suốt, sáng tỏ,
  không gợn đục, hội đủ mọi vẻ tốt đẹp; sợi chỉ xanh, vàng, đỏ, trắng hoặc vàng nhạt xuyên
  qua; người có mắt sáng cầm ngọc trên tay, nhìn kỹ và nhận xét; sau đó lặp lại đầy đủ.
- **2.2.18**: viết đủ từng phần, không gộp: thân do tâm tạo; mười phép thần thông (một thân
  thành nhiều thân, nhiều thân thành một thân, hiện ra, biến mất, xuyên vách tường và núi,
  lặn xuống trồi lên trong đất, đi trên nước, bay trên hư không, chạm vào mặt trời và mặt
  trăng, làm chủ thân đến cõi Phạm thiên); thiên nhĩ nghe xa gần; tha tâm với 16 trạng thái;
  túc mạng nhớ nhiều đời và nhiều kiếp; thiên nhãn thấy chúng sinh chết và tái sinh theo
  nghiệp; tri kiến đoạn tận lậu hoặc với bốn sự thật về khổ và bốn sự thật về lậu hoặc.
- **2.2.7**: vẫn tóm lược theo ngoại lệ §1.5. Chú thích tại chỗ nêu rõ Pali dùng peyyāla,
  liệt kê các bước bị tóm lược (xuất gia, thành tựu giới hạnh, hộ trì các căn, chánh niệm và
  tỉnh giác, biết đủ, tìm chỗ vắng vẻ, từ bỏ năm triền cái), nói rõ bản dịch tóm lược và chỉ
  người đọc đến Kinh Sa-môn Quả (DN 2), mục 4.3.2.

Các câu công thức vẫn giữ nguyên số lần: "Và điều này cũng thuộc về hạnh tu của vị ấy" 4 lần;
"Và điều này cũng thuộc về trí tuệ của vị ấy" 2 lần; "Nhưng người ấy rốt cuộc chỉ trở thành
kẻ hầu hạ cho người có đủ trí tuệ và hạnh tu" 4 lần; "Ambaṭṭha, ông nghĩ thế nào" 5 lần.

## 6. `sācariyaka` và 2.5.1–2.5.2

### 6.1. Chín chỗ dịch `sācariyaka`

| Đoạn | Trước | Sau |
|---|---|---|
| 2.4.2 | nơi mình và nơi thầy của mình | nơi bản thân ông và nơi truyền thống của ông |
| 2.4.4 | tôi cùng với thầy của tôi | tôi và truyền thống của tôi |
| 2.4.5 | tôi cùng với thầy của tôi | tôi và truyền thống của tôi |
| 2.4.7 | ông cùng với thầy của mình | ông và truyền thống của ông |
| 2.4.11 | ông cùng với thầy của mình | ông và truyền thống của ông |
| 2.4.15 | ông cùng với thầy của mình | ông và truyền thống của ông |
| 2.4.18 | ông cùng với thầy của mình | ông và truyền thống của ông |
| 2.5.1 | ông cùng với thầy của mình đã thiếu hẳn sự thành tựu... | ông cùng với truyền thống của mình chẳng những thiếu sự thành tựu... — |
| 2.5.2 | Và ông cùng với thầy của mình còn thiếu cả bốn lối rời bỏ... | mà còn chưa đạt tới cả bốn lối rời bỏ... |

Chú thích tại 2.4.2 nay giải thích `sācariyaka` là cách nói chỉ phe phái, truyền thống tôn
giáo hay triết học của một người, nghĩa đen là "cái bắt nguồn từ vị thầy của mình", chứ không
chỉ riêng cá nhân người thầy.

Hai chỗ 2.5.3 và 2.5.5 vẫn giữ "thầy của ông" là đúng, vì Pali ở đó dùng `ācariyena` (vị
thầy), không phải `sācariyaka`; chỗ này không nằm trong phạm vi phải sửa.

### 6.2. Leo thang ở 2.5.1–2.5.2

Pali dùng `ceva ... ca` bắc qua hai đoạn:

- 2.5.1: "Này Ambaṭṭha, như vậy là ông cùng với truyền thống của mình chẳng những thiếu sự
  thành tựu trí tuệ và hạnh tu tối thượng này —"
- 2.5.2: "mà còn chưa đạt tới cả bốn lối rời bỏ của sự thành tựu ấy nữa."

Cách viết này giữ đúng ý "không chỉ thiếu trí tuệ và hạnh tu, mà còn chưa đạt tới cả bốn lối
rời bỏ", tránh câu cũ đọc thành "thiếu cả bốn lối rời bỏ" — vô lý vì thiếu thì không thể nói
là đủ bốn.

## 7. Kết quả kiểm tra

```
$ python3 kiem-tra-marker.py ban-dich/08-knowledge-conduct.md
== ban-dich/08-knowledge-conduct.md
   marker trong bài dịch : 31
   segment trong nguồn   : 31
   số từ nội dung        : 3120
   ==> ĐẠT

$ python3 kiem-tra-marker.py ban-dich/09-four-causes.md
== ban-dich/09-four-causes.md
   marker trong bài dịch : 44
   segment trong nguồn   : 44
   số từ nội dung        : 1312
   ==> ĐẠT
```

Các kiểm tra hình thức khác:

- Không có ngoặc kép cong.
- Trong hai tệp bản dịch: không có `...`, không có `…` ngoài phạm vi `[Chú thích: ...]`
  (thực tế cả hai tệp không dùng `…`).
- Không có "Đức Phật", "ngươi", "mày" và các từ cấm khác.
- Không còn "cùng với thầy của mình" trong `09-four-causes.md`.
- Không còn "căn nguyên đọa lạc" trong `09-four-causes.md`.

## 8. Ghi chú

- Không sửa `HUONG-DAN-DICH.md`, không sửa `nguon/`, không đụng các tệp khác, không chạy
  `ghep.py`.
- Các tệp đã ghi: `ban-dich/08-knowledge-conduct.md`, `ban-dich/09-four-causes.md`,
  `ra-soat/D2-va-sau-ra-soat.md`.
