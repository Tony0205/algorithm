import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\07_사과나무(다이아몬드)\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

sum1 = 0
s = e = n//2

for i in range(n):
    for j in range(s, e + 1):        
        sum1 += data[i][j]

    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(sum1)
