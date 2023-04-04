import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\10_역수열(그리디)\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())
a = list(map(int, input().split()))


seq = [0] * n
for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:
            a[i] -= 1

for x in seq:
    print(x, end=" ")
