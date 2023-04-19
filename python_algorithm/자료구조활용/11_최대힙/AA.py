import sys
from heapq import heappop, heappush

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\10_최소힙\in1.txt"
# sys.stdin = open(open_dir, "rt")

heap = []
while True:
    a = int(input())

    if a == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(heappop(heap)[1])
        continue

    if a == -1:
        break

    heappush(heap, (-a, a))
