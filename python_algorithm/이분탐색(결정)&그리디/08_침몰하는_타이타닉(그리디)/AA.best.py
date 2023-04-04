import sys
from collections import deque

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\08_침몰하는_타이타닉(그리디)\in2.txt"
sys.stdin = open(open_dir, "rt")

n, limit = map(int, input().split())
people = list(map(int, input().split()))

people.sort()

people = deque(people)
cnt = 0

while people:
    if len(people) == 1:
        cnt += 1
        break

    if people[0] + people[-1] > limit:
        people.pop()
        cnt += 1
    else:
        people.popleft()
        people.pop()
        cnt += 1


print(cnt)
