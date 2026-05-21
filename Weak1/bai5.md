# BÀI 5. ĐIỀU KIỆN ÁP DỤNG

## Tìm kiếm tuyến tính có bắt buộc mảng phải sắp xếp không?

**Không bắt buộc.**

Tìm kiếm tuyến tính có thể áp dụng cho **mảng bất kỳ**, dù mảng đã sắp xếp hay chưa sắp xếp.

Lý do là thuật toán kiểm tra lần lượt từng phần tử trong mảng từ đầu đến cuối.

Ở mỗi bước:

```python
if A[i] == x:
    return i
else:
    i = i + 1
```

Nếu duyệt hết mảng mà vẫn không tìm thấy thì trả về:

```python
-1
```

---

# So sánh với tìm kiếm nhị phân

| Tiêu chí | Tìm kiếm tuyến tính | Tìm kiếm nhị phân |
|---|---|---|
| Điều kiện áp dụng | Mảng bất kỳ, không cần sắp xếp | Mảng phải được sắp xếp |
| Cách tìm kiếm | Duyệt lần lượt từng phần tử | Chia đôi phạm vi tìm kiếm |
| Khi so sánh sai | Tăng `i = i + 1` | Cập nhật `left` hoặc `right` |
| Độ phức tạp | `O(n)` | `O(log₂n)` |
| Tốc độ | Chậm hơn khi mảng lớn | Nhanh hơn khi mảng lớn |

---

# Kết luận

Tìm kiếm tuyến tính **dễ áp dụng hơn** vì không yêu cầu mảng phải sắp xếp trước.  
Tuy nhiên, nếu mảng đã được sắp xếp thì tìm kiếm nhị phân hiệu quả hơn vì có tốc độ tìm kiếm nhanh hơn và độ phức tạp thấp hơn.