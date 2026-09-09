# Test Case – Bài 7: Tìm UCLN của a và b

## 1. Mô tả bài toán

Tìm ước chung lớn nhất của hai số nguyên `a` và `b`.

Quy ước: không xác định UCLN khi `a = 0` và `b = 0`.

## 2. Phân lớp tương đương

| Lớp | Điều kiện | Loại |
|---|---|---|
| EP1 | `a > 0`, `b > 0` | Hợp lệ |
| EP2 | `a = 0`, `b != 0` | Hợp lệ |
| EP3 | `b = 0`, `a != 0` | Hợp lệ |
| EP4 | Có số âm | Hợp lệ, lấy trị tuyệt đối |
| EP5 | `a = 0`, `b = 0` | Không hợp lệ |
| EP6 | Không phải số nguyên | Không hợp lệ |

## 3. Phân tích giá trị biên

Các biên quan trọng: `a = 0`, `b = 0`, `(a,b) = (0,0)`.

## 4. Test case

| ID | a | b | Expected Output | Kỹ thuật | Loại |
|---|---:|---:|---|---|---|
| TC01 | 12 | 18 | `UCLN = 6` | Phân lớp tương đương | Hợp lệ |
| TC02 | 18 | 12 | `UCLN = 6` | Phân lớp tương đương | Hợp lệ |
| TC03 | 5 | 7 | `UCLN = 1` | Phân lớp tương đương | Hợp lệ |
| TC04 | 10 | 10 | `UCLN = 10` | Giá trị đặc biệt | Hợp lệ |
| TC05 | 0 | 5 | `UCLN = 5` | Giá trị biên | Hợp lệ |
| TC06 | 5 | 0 | `UCLN = 5` | Giá trị biên | Hợp lệ |
| TC07 | -12 | 18 | `UCLN = 6` | Phân lớp tương đương | Hợp lệ |
| TC08 | 0 | 0 | `Loi: Khong xac dinh UCLN(0, 0)` | Giá trị biên | Không hợp lệ |

## 5. Tiêu chí PASS/FAIL

PASS nếu UCLN chính xác và `(0,0)` được xử lý là không hợp lệ.
