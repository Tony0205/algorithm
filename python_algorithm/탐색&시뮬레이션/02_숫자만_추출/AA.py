import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\02_숫자만_추출\in1.txt"
# sys.stdin = open(open_dir, "rt")

data = list(str(input()))

num = ''
for d in data:
    if not d.isalpha():
        num += d

# 앞의 0 숫자 제거
num = int(num)

res = []
for i in range(1, num + 1):
    if num % i == 0:
        res.append(i)

print(num)
print(len(res))