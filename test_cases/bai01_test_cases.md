# Test Case – Bài 1: Tính chu vi hình vuông

## 1. Mô tả bài toán

Tính chu vi hình vuông theo công thức:

**P = 4 × a**

Trong đó `a` là độ dài cạnh hình vuông.

## 2. Đầu vào và đầu ra

- Input: `a`, số thực biểu diễn độ dài cạnh.
- Điều kiện hợp lệ: `a > 0`.
- Output: `P = 4 × a`.
- Nếu `a <= 0` hoặc không phải số: báo dữ liệu không hợp lệ.

## 3. Phân lớp tương đương 


| Lớp | Điều kiện | Loại |
|---|---|---|
| EP1 | `a > 0` | Hợp lệ |
| EP2 | `a = 0` | Không hợp lệ |
| EP3 | `a < 0` | Không hợp lệ |
| EP4 | `a` không phải số | Không hợp lệ |

## 4. Phân tích giá trị biên

Biên là `a = 0`; kiểm tra `-1`, `0`, `1`.

## 5. Test case

| ID | Input | Expected Output | Kỹ thuật | Loại |
|---|---:|---|---|---|
| TC01 | 5 | `Chu vi = 20` | Phân lớp tương đương | Hợp lệ |
| TC02 | 1 | `Chu vi = 4` | Giá trị biên | Hợp lệ |
| TC03 | 0.5 | `Chu vi = 2.0` | Phân lớp tương đương | Hợp lệ |
| TC04 | 0 | `Loi: a phai > 0` | Giá trị biên | Không hợp lệ |
| TC05 | -5 | `Loi: a phai > 0` | Phân lớp tương đương | Không hợp lệ |
| TC06 | abc | `Loi: could not convert string to float: 'abc'` | Dữ liệu không hợp lệ | Không hợp lệ |

## 6. Tiêu chí PASS/FAIL

PASS khi output thực tế phù hợp Expected Output.
