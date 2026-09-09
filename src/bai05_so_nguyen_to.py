def la_so_nguyen_to(n):
    if n < 0:
        raise ValueError("n phai >= 0")

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

try:
    n = int(input("Nhap n: "))

    if la_so_nguyen_to(n):
        print("La so nguyen to")
    else:
        print("Khong phai so nguyen to")

except ValueError as e:
    print("Loi:", e)