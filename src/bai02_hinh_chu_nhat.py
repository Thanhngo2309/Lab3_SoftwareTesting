def chu_vi_hinh_vuong(a):
    if a <= 0:
        raise ValueError("a phai > 0")
    return 4 * a


a = float(input("Nhap a: "))

try:
    print("Chu vi =", chu_vi_hinh_vuong(a))
except ValueError as e:
    print("Loi:", e)
    