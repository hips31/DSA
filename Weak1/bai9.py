
# BÀI 9: Tìm tất cả vị trí

def tim_tat_ca(a, x):
    i = 0
    vi_tri = []

    while i < len(a):
        if a[i] == x:
            vi_tri.append(i)

        i = i + 1

    return vi_tri


a = list(map(int, input("Nhap mang: ").split()))
x = int(input("Nhap x: "))

print("Cac vi tri xuat hien cua x la:", tim_tat_ca(a, x))
