import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\09_봉우리\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0] * n)
a.append([0] * n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):        
        target = a[i][j]

        left = a[i][j-1]
        right = a[i][j+1]
        top = a[i-1][j]
        bottom = a[i+1][j]

        if target > left and target > right and target > top and target > bottom:            
            cnt += 1


print(cnt)
