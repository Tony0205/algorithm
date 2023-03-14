import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\08_곶감(모래시계)\in3.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())

    # 왼쪽으로 회전
    if t == 0:
        for _ in range(k):
            # 행 선택
            a[h-1].append(a[h-1].pop(0))
    else:
        # 오른쪽으로 회전
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())


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
