import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\09_봉우리\in1.txt"
sys.stdin = open(open_dir, "rt")

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0] * n)
a.append([0] * n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0

# 중요!!
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n+1):
    for j in range(1, n+1):
        # 중요!! 4방향 모두 검사
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
