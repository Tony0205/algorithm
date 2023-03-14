import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\08_곶감(모래시계)\in3.txt"
sys.stdin = open(open_dir, "rt")

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

b = [list(map(int, input().split())) for _ in range(m)]


# print(a)
# print(b)


for x in b:
    row, direction, cnt = x
    # 행 선택
    selected_row = a[row-1]

    # 왼쪽
    temp = [0] * n
    if direction == 0:
        # 원하는 만큼 회전...
        for i in range(n):
            x = selected_row[i]
            temp[i-cnt] = x
    else:
        # 오른쪽 회전
        for i in range(n):
            x = selected_row[i]

            rotate = i+cnt
            # 인덱스를 벗어나면...
            if rotate > n - 1:
                rotate = rotate - n
                temp[rotate] = x
            else:
                temp[rotate] = x

    a[row-1] = temp


# 모래시계 모양의 영역에 감 몇 개가 있는지
s = 0
e = n
sum1 = 0
for i in range(n):
    for j in range(s, e):
        sum1 += a[i][j]

    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sum1)
