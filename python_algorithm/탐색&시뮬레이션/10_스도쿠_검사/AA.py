import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\10_스도쿠_검사\in1.txt"
# sys.stdin = open(open_dir, "rt")

a = [list(map(int, input().split())) for _ in range(9)]

answer = "YES"

# 행 검사
for i in range(9):
    num = list(range(1, 10))
    for j in range(9):
        if a[i][j] in num:
            num.remove(a[i][j])
        else:
            answer = "NO"
            break

# 열 검사
for i in range(9):
    num = list(range(1, 10))
    for j in range(9):
        if a[j][i] in num:
            num.remove(a[j][i])
        else:
            answer = "NO"
            break

# 3*3 보드 검사
num = list(range(1, 10))
for i in range(3):
    for j in range(3):
        if a[i][j] in num:
            num.remove(a[i][j])
        else:
            answer = "NO"
            break

# 3*3 보드 검사
num = list(range(1, 10))
for i in range(3, 6):
    for j in range(3, 6):
        if a[i][j] in num:
            num.remove(a[i][j])
        else:
            answer = "NO"
            break

# 3*3 보드 검사
num = list(range(1, 10))
for i in range(6, 9):
    for j in range(6, 9):
        if a[i][j] in num:
            num.remove(a[i][j])
        else:
            answer = "NO"
            break


print(answer)
