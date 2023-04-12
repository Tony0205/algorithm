import sys
from collections import deque

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\06_응급실\in1.txt"
# sys.stdin = open(open_dir, "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

deq = deque(a)

# print(deq)

i = 0

while i < n:
    p = deq.popleft()
    m -= 1

    for w in deq:
        if p < w:
            deq.append(p)
            if m == -1:
                m = len(deq) - 1
            break
    else:
        i += 1
        if m == -1:
            break


print(i)
