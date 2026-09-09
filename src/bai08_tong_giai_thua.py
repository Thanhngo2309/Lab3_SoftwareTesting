def tong_giai_thua(n):
    if n < 1:
        raise ValueError("n phai >= 1")

    factorial = 1
    s = 0

    for i in range(1, n + 1):
        factorial *= i
        s += factorial
    return s


try:
    n = int(input("Nhap n: "))
    print("S =", tong_giai_thua(n))

except ValueError as e:
    print("Loi:", e)