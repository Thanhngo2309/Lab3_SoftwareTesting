def tong_chu_so(n):
    if n < 0:
        raise ValueError("n phai >= 0")

    return sum(int(c) for c in str(n))


try:
    n = int(input("Nhap n: "))
    print("Tong cac chu so =", tong_chu_so(n))

except ValueError as e:
    print("Loi:", e)
    