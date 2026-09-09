# Bài thực hành: Kiểm thử hộp đen

Repository này chứa mã nguồn, test case và kết quả kiểm thử cho 8 bài toán trong bài thực hành.

## 1. Danh sách bài toán

1. Tính chu vi hình vuông.
2. Tính diện tích hình chữ nhật.
3. Giải phương trình bậc 2.
4. Tính tổng các chữ số của một số.
5. Kiểm tra `n` có phải số nguyên tố không.
6. Tính `S = 1 - 2 + 3 - 4 + ... + n`.
7. Tìm UCLN của `a` và `b`.
8. Tính `S = 1! + 2! + 3! + ... + n!`.

## 2. Quy ước dữ liệu

| Bài | Điều kiện hợp lệ |
|---|---|
| Bài 1 | `a > 0` |
| Bài 2 | `dai > 0`, `rong > 0` |
| Bài 3 | `a != 0` |
| Bài 4 | `n >= 0`, n là số nguyên |
| Bài 5 | `n >= 0`, n là số nguyên |
| Bài 6 | `n >= 1`, n là số nguyên |
| Bài 7 | `a,b` là số nguyên và không đồng thời bằng 0 |
| Bài 8 | `n >= 1`, n là số nguyên |

## 3. Kỹ thuật kiểm thử

### Phân lớp tương đương

Miền đầu vào được chia thành các nhóm dữ liệu có hành vi tương đương. Chọn một hoặc một số giá trị đại diện cho từng lớp.

### Phân tích giá trị biên

Kiểm tra các giá trị tại biên và gần biên của miền hợp lệ, ví dụ `-1`, `0`, `1` khi biên là `0`.

### Dữ liệu hợp lệ và không hợp lệ

Mỗi bài có các trường hợp dữ liệu đúng và ít nhất một trường hợp dữ liệu sai/không hợp lệ theo yêu cầu đề bài.

## 4. Cấu trúc repository

```text
black-box-testing/
├── README.md
├── run_tests.py
├── src/
│   ├── bai01_hinh_vuong.py
│   ├── bai02_hinh_chu_nhat.py
│   ├── bai03_pt_bac2.py
│   ├── bai04_tong_chu_so.py
│   ├── bai05_so_nguyen_to.py
│   ├── bai06_tong_xen_ke.py
│   ├── bai07_ucln.py
│   └── bai08_tong_giai_thua.py
├── test_cases/
│   ├── bai01_test_cases.md
│   ├── bai02_test_cases.md
│   ├── bai03_test_cases.md
│   ├── bai04_test_cases.md
│   ├── bai05_test_cases.md
│   ├── bai06_test_cases.md
│   ├── bai07_test_cases.md
│   └── bai08_test_cases.md
├── results/
│   └── test_results.md
└── issues/
    ├── issue_1_valid_test_cases.md
    ├── issue_2_invalid_boundary_exception.md
    └── commit_plan.md
```

## 5. Cách chạy chương trình

Ví dụ:

```bash
python src/bai01_hinh_vuong.py
```

Hoặc chạy bộ kiểm thử:

```bash
python run_tests.py
```

## 6. Danh sách test case

| Bài | Test case |
|---|---|
| Bài 1 | [bai01_test_cases.md](test_cases/bai01_test_cases.md) |
| Bài 2 | [bai02_test_cases.md](test_cases/bai02_test_cases.md) |
| Bài 3 | [bai03_test_cases.md](test_cases/bai03_test_cases.md) |
| Bài 4 | [bai04_test_cases.md](test_cases/bai04_test_cases.md) |
| Bài 5 | [bai05_test_cases.md](test_cases/bai05_test_cases.md) |
| Bài 6 | [bai06_test_cases.md](test_cases/bai06_test_cases.md) |
| Bài 7 | [bai07_test_cases.md](test_cases/bai07_test_cases.md) |
| Bài 8 | [bai08_test_cases.md](test_cases/bai08_test_cases.md) |

## 7. Kết quả kiểm thử

Kết quả được lưu tại `results/test_results.md`.

## 8. GitHub Issues

- Issue 1: Thiết kế test case dữ liệu hợp lệ.
- Issue 2: Thiết kế test case dữ liệu không hợp lệ, giá trị biên và trường hợp đặc biệt.

Chi tiết nội dung Issue và kế hoạch commit nằm trong thư mục `issues/`.
