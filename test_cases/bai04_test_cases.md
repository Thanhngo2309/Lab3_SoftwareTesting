# Test Case – Bài 4: Tính tổng các chữ số

## 1. Mô tả bài toán

Tính tổng các chữ số của số nguyên `n`.

Ví dụ: `12345 → 15`.

## 2. Đầu vào và đầu ra

- Input: `n`, số nguyên.
- Điều kiện hợp lệ: `n >= 0`.
- Output: tổng các chữ số.
- `n < 0` hoặc dữ liệu không phải số nguyên: không hợp lệ.

## 3. Phân lớp tương đương

| Lớp | Điều kiện | Loại |
|---|---|---|
| EP1 | `n > 0` | Hợp lệ |
| EP2 | `n = 0` | Hợp lệ/biên |
| EP3 | `n < 0` | Không hợp lệ |
| EP4 | Không phải số nguyên | Không hợp lệ |

## 4. Phân tích giá trị biên

Biên là `n = 0`; kiểm tra `-1`, `0`, `1`.

## 5. Test case

| ID | Input | Expected Output | Kỹ thuật | Loại |
|---|---:|---|---|---|
| TC01 | 12345 | `Tong cac chu so = 15` | Phân lớp tương đương | Hợp lệ |
| TC02 | 0 | `Tong cac chu so = 0` | Giá trị biên | Hợp lệ |
| TC03 | 9 | `Tong cac chu so = 9` | Giá trị biên | Hợp lệ |
| TC04 | 1000 | `Tong cac chu so = 1` | Phân lớp tương đương | Hợp lệ |
| TC05 | 99999 | `Tong cac chu so = 45` | Phân lớp tương đương | Hợp lệ |
| TC06 | -123 | `Loi: n phai >= 0` | Phân lớp tương đương | Không hợp lệ |
| TC07 | abc | Báo lỗi chuyển đổi dữ liệu | Dữ liệu không hợp lệ | Không hợp lệ |

## 6. Tiêu chí PASS/FAIL

PASS nếu tổng chữ số chính xác và dữ liệu không hợp lệ được xử lý đúng.
