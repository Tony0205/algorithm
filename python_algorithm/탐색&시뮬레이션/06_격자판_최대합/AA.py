import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\06_격자판_최대합\in1.txt"
sys.stdin = open(open_dir, "rt")

n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# print(data)

result = []

for d in data:
    sum_res = 0
    # 행의 합
    for x in d:
        sum_res += x
    result.append(sum_res)

# 열의 합
for i in range(n):
    sum_res = 0
    for j in range(n):
        sum_res += data[j][i]
        result.append(sum_res)

# 대각선 합 - 1, 2
sum1, sum2 = 0, 0

for i in range(n):
    sum1 += data[i][i]
    sum2 += data[i][n-i-1]

result.append(sum1)
result.append(sum2)

# 대각선의 합 - 2 (틀림)
# sum_res = 0
# for i in range(n-1, -1, -1):
#     sum_res += data[i][i]
#     print(i)
# result.append(sum_res)

print(max(result))
