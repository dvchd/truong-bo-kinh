# Nguồn

Thư mục này chứa dữ liệu gốc dùng để dịch, lưu lại để **bất kỳ ai cũng đối chiếu được từng câu**.

## `sections/` — 33 tệp, 650 đoạn

Mỗi tệp ứng với một phần của bài kinh. Trong tệp, mỗi đoạn có dạng:

```markdown
## dn2:1.1.1

- **PLI**: Evaṁ me sutaṁ — ekaṁ samayaṁ bhagavā antarā ca rājagahaṁ antarā ca nāḷandaṁ ...
- **EN**: So I have heard. At one time the Buddha was traveling along the road between Rājagaha and Nāḷandā ...
- **NOTE**: (chú thích, nếu có)
```

- **PLI** — nguyên bản Pali, tách theo đúng mã đoạn của SuttaCentral.
- **EN** — bản dịch tiếng Anh của **Bhikkhu Sujato** (SuttaCentral), dùng làm bản tham chiếu khi dịch.
- **NOTE** — chú thích của Bhikkhu Sujato hoặc ghi chú của người dịch về chỗ khó.

Mã `dn2:X.Y.Z` chính là mã đoạn của SuttaCentral. Dán vào:

- Pali: <https://suttacentral.net/dn1/pli/ms>
- Anh: <https://suttacentral.net/dn1/en/sujato>

để mở đúng đoạn gốc.

## `api_dn2.json`

Toàn bộ phản hồi API SuttaCentral: nguyên bản Pali, bản dịch Anh của Sujato, chú thích, tham chiếu chéo, và các biến bản.. Dùng cho các script kiểm tra.

## Giấy phép của dữ liệu nguồn

| Thành phần | Giấy phép |
|---|---|
| Nguyên bản Pali (Tipiṭaka) | Phạm vi công cộng |
| Bản dịch tiếng Anh — Bhikkhu Sujato | **CC0** (hiến tặng vào phạm vi công cộng) |
| Chú thích của Bhikkhu Sujato | CC0 |

Bhikkhu Sujato đã hiến tặng toàn bộ bản dịch Trường Bộ Kinh của mình vào phạm vi công cộng qua Creative Commons Zero, nên việc lưu lại nguyên văn ở đây là hoàn toàn hợp lệ. Xem <https://suttacentral.net/licensing>.

## Nguồn thứ cấp khác

Các nguồn tham khảo thêm (Wikipedia, Encyclopedia of Buddhism, Phật Sự Online, Access to Insight, các bản dịch của Bhikkhu Bodhi và Maurice Walshe) được liệt kê đầy đủ, kèm liên kết, trong [`../ban-dich/nguon-tham-khao.md`](../ban-dich/nguon-tham-khao.md).
