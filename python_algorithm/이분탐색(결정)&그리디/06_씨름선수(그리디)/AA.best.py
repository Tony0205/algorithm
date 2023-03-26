import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\06_씨름선수(그리디)\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())

body = []

for i in range(n):
    h, w = map(int, input().split())
    body.append((h, w))

body.sort(reverse=True)

largest = 0
cnt = 0

for h, w in body:
    if w > largest:
        # 가장 큰 값으로 몸무게 갱신,
        # 그래야 다음사람입장에서 키도 지는데, 몸무게까지 지는지 알 수 있음
        largest = w
        cnt += 1

print(cnt)
