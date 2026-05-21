# BÀI 1. TRÌNH BÀY Ý TƯỞNG

## Ý tưởng thuật toán tìm kiếm tuyến tính

Thuật toán tìm kiếm tuyến tính (Linear Search) thực hiện bằng cách duyệt lần lượt từng phần tử của mảng từ đầu đến cuối.

Ở mỗi bước, so sánh phần tử hiện tại `A[i]` với giá trị cần tìm `x`.

- Nếu `A[i] == x` → tìm thấy phần tử, dừng thuật toán.
- Nếu `A[i] != x` → tăng chỉ số:

```python
i = i + 1
```

rồi tiếp tục kiểm tra phần tử kế tiếp.

Nếu đã duyệt hết mảng mà vẫn chưa tìm thấy thì kết luận phần tử không tồn tại trong mảng và trả về `-1`.

---

## Input

- Mảng số nguyên `A`
- Số phần tử của mảng `n`
- Giá trị cần tìm `x`

Ví dụ:

```python
A = [7, 3, 9, 12, 5, 8, 1]
x = 5
```

---

## Output

- Vị trí của phần tử `x` trong mảng nếu tìm thấy.
- Nếu không tìm thấy thì trả về `-1`.

---

## Thuật toán dừng trong các trường hợp

### Trường hợp 1: Tìm thấy phần tử

Khi:

```python
A[i] == x
```

→ Thuật toán dừng và trả về vị trí `i`.

---

### Trường hợp 2: Duyệt hết mảng

Sau nhiều lần:

```python
i = i + 1
```

nếu:

```python
i >= n
```

→ Hết mảng nhưng chưa tìm thấy `x`, thuật toán dừng và trả về `-1`.