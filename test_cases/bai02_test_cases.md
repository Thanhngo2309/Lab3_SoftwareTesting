# Test Case – Bài 2: Tính diện tích hình chữ nhật

## 1. Mô tả bài toán

Tính diện tích hình chữ nhật:

**S = dài × rộng**

## 2. Đầu vào và đầu ra 

- Input: `dai`, `rong`.
- Điều kiện hợp lệ: `dai > 0` và `rong > 0`.
- Output: diện tích.
- Nếu một giá trị `<= 0` hoặc không phải số: báo dữ liệu không hợp lệ.

## 3. Phân lớp tương đương

| Lớp | Điều kiện | Loại |
|---|---|---|
| EP1 | `dai > 0`, `rong > 0` | Hợp lệ |
| EP2 | `dai = 0` | Không hợp lệ |
| EP3 | `rong = 0` | Không hợp lệ |
| EP4 | `dai < 0` | Không hợp lệ |
| EP5 | `rong < 0` | Không hợp lệ |
| EP6 | Một giá trị không phải số | Không hợp lệ |

## 4. Phân tích giá trị biên

Biên của cả hai biến là `0`.

## 5. Test case

| ID | Input (dài, rộng) | Expected Output | Kỹ thuật | Loại |
|---|---|---|---|---|
| TC01 | (5, 3) | `Dien tich = 15` | Phân lớp tương đương | Hợp lệ |
| TC02 | (1, 1) | `Dien tich = 1` | Giá trị biên | Hợp lệ |
| TC03 | (0.5, 2) | `Dien tich = 1.0` | Phân lớp tương đương | Hợp lệ |
| TC04 | (0, 5) | `Loi: Chieu dai va chieu rong phai > 0` | Giá trị biên | Không hợp lệ |
| TC05 | (5, 0) | `Loi: Chieu dai va chieu rong phai > 0` | Giá trị biên | Không hợp lệ |
| TC06 | (-2, 5) | `Loi: Chieu dai va chieu rong phai > 0` | Phân lớp tương đương | Không hợp lệ |
| TC07 | (abc, 5) | Báo lỗi chuyển đổi dữ liệu | Dữ liệu không hợp lệ | Không hợp lệ |

## 6. Tiêu chí PASS/FAIL

PASS khi diện tích đúng và dữ liệu không hợp lệ được phát hiện.
