import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\02_숫자만_추출\in1.txt"
sys.stdin = open(open_dir, "rt")

data = input()

res = 0
for x in data:
    if x.isdecimal():
        res = res * 10 + int(x)

print(res)

cnt = 0

for i in range(1, res+1):
    if res%i == 0:
        cnt += 1

print(cnt)