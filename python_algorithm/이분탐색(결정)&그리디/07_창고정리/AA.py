import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\07_창고정리\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())
boxes = list(map(int, input().split()))
m = int(input())


# m회의 높이 조정
for _ in range(m):

    largest = 0
    largestIdx = 0

    smallestIdx = 0
    smallest = 9999
    # n개의 박스를 돌면서
    for i in range(n):
        # 최대값, 최소값 찾기
        if boxes[i] > largest:
            largestIdx = i
            largest = boxes[i]

        if boxes[i] < smallest:
            smallestIdx = i
            smallest = boxes[i]

    # print(smallest, largest)

    # 가장 높은 곳의 상자를 -> 낮은곳으로 이동한다.
    boxes[largestIdx] -= 1
    boxes[smallestIdx] += 1

highest = max(boxes)
lowest = min(boxes)
# 높은 박스와 낮은 박스의 차이 출력
print(highest - lowest)
