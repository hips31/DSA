
# BÀI 8: Đếm số lần xuất hiện

def dem_xuat_hien(a, x):
    i = 0
    dem = 0

    while i < len(a):
        if a[i] == x:
            dem = dem + 1

        i = i + 1

    return dem


a = list(map(int, input("Nhap mang: ").split()))
x = int(input("Nhap x: "))

print("So lan xuat hien cua x la:", dem_xuat_hien(a, x))
