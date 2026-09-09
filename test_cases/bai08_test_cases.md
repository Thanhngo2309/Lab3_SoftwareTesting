# Test Case – Bài 8: Tính S = 1! + 2! + ... + n!

## 1. Mô tả bài toán

Tính:

**S = 1! + 2! + 3! + ... + n!**

Ví dụ `n = 4`:

`S = 1 + 2 + 6 + 24 = 33`.

## 2. Đầu vào và đầu ra


- Input: `n`, số nguyên.
- Điều kiện hợp lệ: `n >= 1`.
- Output: tổng các giai thừa.
- `n < 1` hoặc không phải số nguyên: không hợp lệ.

## 3. Phân lớp tương đương

| Lớp | Điều kiện | Loại |
|---|---|---|
| EP1 | `n >= 1` | Hợp lệ |
| EP2 | `n = 0` | Không hợp lệ |
| EP3 | `n < 0` | Không hợp lệ |
| EP4 | Không phải số nguyên | Không hợp lệ |

## 4. Phân tích giá trị biên

Biên là `n = 1`; kiểm tra `0`, `1`, `2`.

## 5. Test case

| ID | Input | Expected Output | Kỹ thuật | Loại |
|---|---:|---|---|---|
| TC01 | 1 | `S = 1` | Giá trị biên | Hợp lệ |
| TC02 | 2 | `S = 3` | Giá trị biên | Hợp lệ |
| TC03 | 3 | `S = 9` | Phân lớp tương đương | Hợp lệ |
| TC04 | 4 | `S = 33` | Phân lớp tương đương | Hợp lệ |
| TC05 | 5 | `S = 153` | Phân lớp tương đương | Hợp lệ |
| TC06 | 0 | `Loi: n phai >= 1` | Giá trị biên | Không hợp lệ |
| TC07 | -3 | `Loi: n phai >= 1` | Phân lớp tương đương | Không hợp lệ |
| TC08 | abc | Báo lỗi chuyển đổi dữ liệu | Dữ liệu không hợp lệ | Không hợp lệ |

## 6. Tiêu chí PASS/FAIL

PASS nếu tổng giai thừa chính xác và chương trình từ chối `n < 1`.
