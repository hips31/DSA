
# BÀI 7: Kiểm tra tồn tại

def ton_tai(a, x):
    i = 0

    while i < len(a):
        if a[i] == x:
            return True

        i = i + 1

    return False


a = list(map(int, input("Nhap mang: ").split()))
x = int(input("Nhap x: "))

print(ton_tai(a, x))
