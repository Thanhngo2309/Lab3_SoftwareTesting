# Kế hoạch commit và giải quyết Issue

## Commit 1 – Khởi tạo project

```bash
git add README.md src/
git commit -m "Initial project setup"
```

## Commit 2 – Giải quyết Issue 1

Mục tiêu: thêm test case cho dữ liệu hợp lệ.

```bash
git add test_cases/
git commit -m "Add valid input test cases"
```

Nếu muốn liên kết với Issue #1 trên GitHub:

```text
Add valid input test cases

Fixes #1
```

## Commit 3 – Giải quyết Issue 2

Mục tiêu: bổ sung dữ liệu không hợp lệ, giá trị biên và trường hợp đặc biệt.

```bash
git add test_cases/ src/ results/
git commit -m "Add invalid and boundary test cases"
```

Có thể liên kết với Issue #2:

```text
Add invalid and boundary test cases

Fixes #2
```

## Commit 4 – Hoàn thiện tài liệu và kết quả

```bash
git add README.md results/ issues/
git commit -m "Add test results and documentation"
```

## Push lên GitHub

```bash
git branch -M main
git remote add origin <URL_REPOSITORY>
git push -u origin main
```
