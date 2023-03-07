import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())

print(n, k)

# 약수
numbers = []

for num in range(1, n + 1):
    if n % num == 0:
        numbers.append(num)

if len(numbers) >= k:
    print(numbers[k-1])
else:
    print(-1)
