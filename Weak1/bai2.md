# BÀI 2. MÔ PHỎNG TỪNG BƯỚC

Cho:

```python
A = [7, 3, 9, 12, 5, 8, 1]
x = 5
```

Ta thực hiện tìm kiếm tuyến tính bằng cách so sánh lần lượt từng phần tử với `x`.

| Bước | i | A[i] | So sánh A[i] với x | Kết luận |
|---|---|---|---|---|
| 1 | 0 | 7 | 7 ≠ 5 | Chưa tìm thấy → `i = i + 1` |
| 2 | 1 | 3 | 3 ≠ 5 | Chưa tìm thấy → `i = i + 1` |
| 3 | 2 | 9 | 9 ≠ 5 | Chưa tìm thấy → `i = i + 1` |
| 4 | 3 | 12 | 12 ≠ 5 | Chưa tìm thấy → `i = i + 1` |
| 5 | 4 | 5 | 5 = 5 | Tìm thấy phần tử → Dừng |

---

## Kết luận

- Phần tử `x = 5` được tìm thấy tại vị trí:

```python
i = 4
```

- Giá trị hàm trả về là:

```python
4
```