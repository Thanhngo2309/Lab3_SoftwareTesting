# Test Case – Bài 6: Tính S = 1 − 2 + 3 − 4 + ... + n

## 1. Mô tả bài toán

Tính:

**S = 1 − 2 + 3 − 4 + ... + n**

Quy ước `n >= 1`.

## 2. Phân lớp tương đương

| Lớp | Điều kiện | Loại |
|---|---|---|
| EP1 | `n = 1` | Hợp lệ/biên |
| EP2 | `n > 1`, n chẵn | Hợp lệ |
| EP3 | `n > 1`, n lẻ | Hợp lệ |
| EP4 | `n = 0` | Không hợp lệ |
| EP5 | `n < 0` | Không hợp lệ |
| EP6 | Không phải số nguyên | Không hợp lệ |

## 3. Phân tích giá trị biên


Biên là `n = 1`; kiểm tra `0`, `1`, `2`.

## 4. Test case

| ID | Input | Expected Output | Kỹ thuật | Loại |
|---|---:|---|---|---|
| TC01 | 1 | `S = 1` | Giá trị biên | Hợp lệ |
| TC02 | 2 | `S = -1` | Giá trị biên | Hợp lệ |
| TC03 | 3 | `S = 2` | Phân lớp tương đương | Hợp lệ |
| TC04 | 4 | `S = -2` | Phân lớp tương đương | Hợp lệ |
| TC05 | 5 | `S = 3` | Phân lớp tương đương | Hợp lệ |
| TC06 | 10 | `S = -5` | Phân lớp tương đương | Hợp lệ |
| TC07 | 0 | `Loi: n phai >= 1` | Giá trị biên | Không hợp lệ |
| TC08 | -5 | `Loi: n phai >= 1` | Phân lớp tương đương | Không hợp lệ |
| TC09 | abc | Báo lỗi chuyển đổi dữ liệu | Dữ liệu không hợp lệ | Không hợp lệ |

## 5. Tiêu chí PASS/FAIL

PASS nếu tổng đúng theo dấu của từng số hạng và dữ liệu `n < 1` bị từ chối.
