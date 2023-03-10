import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\04_두_리스트_합치기\in1.txt"
sys.stdin = open(open_dir, "rt")


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


p1 = p2 = 0
c = []


while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1


if p1 < n:
    c = c + a[p1:]

if p2 < m:
    c = c + b[p2:]


for x in c:
    print(x, end=" ")
