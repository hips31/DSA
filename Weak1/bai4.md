# BÀI 4. PHÂN TÍCH ĐỘ PHỨC TẠP

Với mảng có `n` phần tử, thuật toán tìm kiếm tuyến tính sẽ kiểm tra lần lượt từng phần tử từ đầu đến cuối mảng.

---

## (a) Trường hợp tốt nhất

Phần tử cần tìm nằm ngay ở đầu mảng.

Ví dụ:

```python
A[0] == x
```

Thuật toán chỉ cần so sánh 1 lần là tìm thấy.

### Số phép so sánh

```python
1
```

---

## (b) Trường hợp xấu nhất

Phần tử cần tìm nằm ở cuối mảng hoặc không có trong mảng.

Khi đó thuật toán phải duyệt toàn bộ `n` phần tử.

Ví dụ:

```python
A[n-1] == x
```

hoặc:

```python
x không tồn tại trong mảng
```

### Số phép so sánh

```python
n
```

---

## (c) Trường hợp trung bình

Giả sử phần tử có thể xuất hiện ở bất kỳ vị trí nào với xác suất như nhau.

Số phép so sánh trung bình là:

```python
(n + 1) / 2
```

---

# Độ phức tạp thời gian theo ký hiệu Big O

Trong trường hợp tổng quát, số phép so sánh tăng theo số lượng phần tử `n`.

Vì vậy độ phức tạp thời gian của thuật toán tìm kiếm tuyến tính là:

```python
O(n)
```

---

# Kết luận

- Tìm kiếm tuyến tính đơn giản, dễ cài đặt.
- Không yêu cầu mảng phải sắp xếp.
- Khi số lượng phần tử tăng lớn thì thời gian tìm kiếm tăng tuyến tính theo `n`.