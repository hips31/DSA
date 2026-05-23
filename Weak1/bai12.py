
# BÀI 12: Min và Max trong một lần duyệt

def tim_min_max(a):
    min_value = a[0]
    max_value = a[0]
    min_index = 0
    max_index = 0

    i = 1
    while i < len(a):
        if a[i] < min_value:
            min_value = a[i]
            min_index = i

        if a[i] > max_value:
            max_value = a[i]
            max_index = i

        i = i + 1

    return min_value, min_index, max_value, max_index


a = list(map(int, input("Nhap mang: ").split()))

min_value, min_index, max_value, max_index = tim_min_max(a)

print("Gia tri nho nhat la:", min_value)
print("Vi tri cua gia tri nho nhat la:", min_index)

print("Gia tri lon nhat la:", max_value)
print("Vi tri cua gia tri lon nhat la:", max_index)
