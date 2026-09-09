def tong_xen_ke(n):
    if n < 1:
        raise ValueError("n phai >= 1")

    s = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            s -= i
        else:
            s += i

    return s

try:
    n = int(input("Nhap n: "))
    print("S =", tong_xen_ke(n))

except ValueError as e:
    print("Loi:", e)