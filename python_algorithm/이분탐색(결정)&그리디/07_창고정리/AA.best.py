import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\07_창고정리\in1.txt"
sys.stdin = open(open_dir, "rt")

n = int(input())
boxes = list(map(int, input().split()))
m = int(input())

boxes.sort()

# print(boxes)

# m회의 높이 조정
for _ in range(m):
    boxes[0] += 1
    boxes[n-1] -= 1
    boxes.sort()


print(boxes[n-1] - boxes[0])