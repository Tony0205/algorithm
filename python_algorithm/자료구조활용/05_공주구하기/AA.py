import sys
from collections import deque

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\05_공주구하기\in1.txt"
sys.stdin = open(open_dir, "rt")

n, k = map(int, input().split())

deq = deque()

for i in range(1, n+1):
    deq.append(i)

# print(deq)

i = 1
while len(deq) > 1:
    if i % k == 0:
        deq.popleft()
        i = 1
    else:
        pop_element = deq.popleft()
        deq.append(pop_element)
        i += 1

print(deq.popleft())
