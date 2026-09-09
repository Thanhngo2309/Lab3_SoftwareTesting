# Test Case – Bài 5: Kiểm tra số nguyên tố

## 1. Mô tả bài toán

Kiểm tra `n` có phải số nguyên tố hay không.

Số nguyên tố là số nguyên lớn hơn 1 và chỉ có hai ước dương là 1 và chính nó.

## 2. Đầu vào

- `n`: số nguyên.
- Quy ước: `n >= 0`.

## 3. Phân lớp tương đương

| Lớp | Điều kiện | Loại |
|---|---|---|
| EP1 | `n < 0` | Không hợp lệ |
| EP2 | `n = 0` | Hợp lệ, không nguyên tố |
| EP3 | `n = 1` | Hợp lệ, không nguyên tố |
| EP4 | `n = 2` | Hợp lệ, nguyên tố |
| EP5 | `n > 2`, là số nguyên tố | Hợp lệ |
| EP6 | `n > 2`, là hợp số | Hợp lệ |

## 4. Phân tích giá trị biên

Các giá trị quanh mốc 2: `1`, `2`, `3`, `4`.

## 5. Test case

| ID | Input | Expected Output | Kỹ thuật | Loại |
|---|---:|---|---|---|
| TC01 | 2 | `La so nguyen to` | Giá trị biên | Hợp lệ |
| TC02 | 3 | `La so nguyen to` | Giá trị biên | Hợp lệ |
| TC03 | 4 | `Khong phai so nguyen to` | Giá trị biên | Hợp lệ |
| TC04 | 1 | `Khong phai so nguyen to` | Giá trị biên | Hợp lệ |
| TC05 | 0 | `Khong phai so nguyen to` | Phân lớp tương đương | Hợp lệ |
| TC06 | -5 | `Loi: n phai >= 0` | Phân lớp tương đương | Không hợp lệ |
| TC07 | 97 | `La so nguyen to` | Phân lớp tương đương | Hợp lệ |
| TC08 | 100 | `Khong phai so nguyen to` | Phân lớp tương đương | Hợp lệ |

## 6. Tiêu chí PASS/FAIL

PASS nếu chương trình phân loại đúng số nguyên tố/hợp số và xử lý dữ liệu âm đúng specification.
