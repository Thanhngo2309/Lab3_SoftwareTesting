import math


def giai_pt_bac_2(a, b, c):
    if a == 0:
        raise ValueError("a phai khac 0")

    delta = b * b - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Co 2 nghiem: x1 = {x1}, x2 = {x2}"

    elif delta == 0:
        x = -b / (2 * a)
        return f"Co nghiem kep: x = {x}"

    else:
        return "Khong co nghiem thuc"


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print(giai_pt_bac_2(a, b, c))

except ValueError as e:
    print("Loi:", e)
    