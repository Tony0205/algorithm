import sys
from collections import deque

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\06_응급실\in1.txt"
# sys.stdin = open(open_dir, "rt")

n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]

deq = deque(Q)
cnt = 0
# print(deq)

while True:
    cur = deq.popleft()
    
    if any(cur[1] < x[1] for x in deq):
        deq.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break

