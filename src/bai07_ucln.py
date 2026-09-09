def ucln(a, b):
    if a == 0 and b == 0:
        raise ValueError("Khong xac dinh UCLN(0, 0)")

    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a
try:
    a = int(input("a = "))
    b = int(input("b = "))

    print("UCLN =", ucln(a, b))

except ValueError as e:
    print("Loi:", e)