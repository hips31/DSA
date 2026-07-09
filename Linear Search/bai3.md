# BÀI 3. ĐẾM SỐ PHÉP SO SÁNH

Cho mảng:

```python
A = [7, 3, 9, 12, 5, 8, 1]
```

Thuật toán tìm kiếm tuyến tính sẽ so sánh lần lượt từng phần tử với `x`.

---

# (a) Tìm x = 7

| Lần so sánh | A[i] | Kết quả |
|---|---|---|
| 1 | 7 | 7 = 7 → Tìm thấy |

## Số phép so sánh

```python
1 phép so sánh
```

---

# (b) Tìm x = 1

| Lần so sánh | A[i] | Kết quả |
|---|---|---|
| 1 | 7 | 7 ≠ 1 → `i = i + 1` |
| 2 | 3 | 3 ≠ 1 → `i = i + 1` |
| 3 | 9 | 9 ≠ 1 → `i = i + 1` |
| 4 | 12 | 12 ≠ 1 → `i = i + 1` |
| 5 | 5 | 5 ≠ 1 → `i = i + 1` |
| 6 | 8 | 8 ≠ 1 → `i = i + 1` |
| 7 | 1 | 1 = 1 → Tìm thấy |

## Số phép so sánh

```python
7 phép so sánh
```

---

# (c) Tìm x = 100 (không có trong mảng)

| Lần so sánh | A[i] | Kết quả |
|---|---|---|
| 1 | 7 | 7 ≠ 100 → `i = i + 1` |
| 2 | 3 | 3 ≠ 100 → `i = i + 1` |
| 3 | 9 | 9 ≠ 100 → `i = i + 1` |
| 4 | 12 | 12 ≠ 100 → `i = i + 1` |
| 5 | 5 | 5 ≠ 100 → `i = i + 1` |
| 6 | 8 | 8 ≠ 100 → `i = i + 1` |
| 7 | 1 | 1 ≠ 100 → `i = i + 1` |

Sau khi duyệt hết mảng:

```python
i >= n
```

→ Không tìm thấy phần tử.

## Số phép so sánh

```python
7 phép so sánh
```

---

# Nhận xét

- Nếu phần tử nằm ở đầu mảng → số phép so sánh ít.
- Nếu phần tử nằm cuối mảng → số phép so sánh nhiều hơn.
- Nếu phần tử không có trong mảng → phải duyệt hết mảng nên số phép so sánh là lớn nhất.