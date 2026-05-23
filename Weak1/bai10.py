
# BÀI 10: Vị trí xuất hiện cuối cùng

def vi_tri_cuoi_cung(a, x):
    i = 0
    vi_tri = -1

    while i < len(a):
        if a[i] == x:
            vi_tri = i

        i = i + 1

    return vi_tri


a = list(map(int, input("Nhap mang: ").split()))
x = int(input("Nhap x: "))

print("Vi tri xuat hien cuoi cung cua x la:", vi_tri_cuoi_cung(a, x))
