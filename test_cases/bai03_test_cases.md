# Test Case – Bài 3: Giải phương trình bậc 2

## 1. Mô tả bài toán

Giải phương trình:

**ax² + bx + c = 0**

Điều kiện: `a != 0`.

Tính `Δ = b² - 4ac`.

- `Δ > 0`: hai nghiệm thực phân biệt.
- `Δ = 0`: một nghiệm kép.
- `Δ < 0`: không có nghiệm thực.
- `a = 0`: không phải phương trình bậc 2.

## 2. Phân lớp tương đương

| Lớp | Điều kiện | Loại |
|---|---|---|
| EP1 | `a != 0`, `Δ > 0` | Hợp lệ |
| EP2 | `a != 0`, `Δ = 0` | Hợp lệ |
| EP3 | `a != 0`, `Δ < 0` | Hợp lệ |
| EP4 | `a = 0` | Không hợp lệ |

## 3. Phân tích giá trị biên


Hai biên quan trọng:

- `a = 0`.
- `Δ = 0`.

## 4. Test case

| ID | a | b | c | Δ | Expected Output | Kỹ thuật | Loại |
|---|---:|---:|---:|---:|---|---|---|
| TC01 | 1 | -3 | 2 | 1 | `Co 2 nghiem: x1 = 2.0, x2 = 1.0` | Phân lớp tương đương | Hợp lệ |
| TC02 | 1 | -2 | 1 | 0 | `Co nghiem kep: x = 1.0` | Giá trị biên | Hợp lệ |
| TC03 | 1 | 1 | 1 | -3 | `Khong co nghiem thuc` | Phân lớp tương đương | Hợp lệ |
| TC04 | 0 | 2 | 1 | - | `Loi: a phai khac 0` | Giá trị biên | Không hợp lệ |
| TC05 | -1 | 2 | 3 | 16 | Có 2 nghiệm thực | Phân lớp tương đương | Hợp lệ |
| TC06 | 2 | 4 | 2 | 0 | `Co nghiem kep: x = -1.0` | Giá trị biên | Hợp lệ |

## 5. Tiêu chí PASS/FAIL

PASS nếu chương trình xác định đúng số nghiệm, nghiệm và xử lý `a = 0` là không hợp lệ.
