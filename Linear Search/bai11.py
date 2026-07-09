
# BÀI 11: Tìm giá trị lớn nhất

def tim_lon_nhat(a):
    max_value = a[0]
    max_index = 0

    i = 1
    while i < len(a):
        if a[i] > max_value:
            max_value = a[i]
            max_index = i

        i = i + 1

    return max_value, max_index


a = list(map(int, input("Nhap mang: ").split()))

gia_tri, vi_tri = tim_lon_nhat(a)

print("Gia tri lon nhat la:", gia_tri)
print("Vi tri cua gia tri lon nhat la:", vi_tri)
