import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\04_두_리스트_합치기\in1.txt"
# sys.stdin = open(open_dir, "rt")


n = input()
d1 = list(map(int, input().split()))
m = input()
d2 = list(map(int, input().split()))


l = sorted(d1 + d2)

for n in l:
    print(n, end=" ")
