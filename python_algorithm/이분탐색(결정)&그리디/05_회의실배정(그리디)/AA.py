import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\05_회의실배정(그리디)\in1.txt"
sys.stdin = open(open_dir, "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort(key=lambda x: (x[1], x[0]))

ep = 0
cnt = 0
for x in a:
    if x[0] >= ep:
        ep = x[1]
        cnt += 1

print(cnt)