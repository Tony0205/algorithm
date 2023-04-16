import sys
from collections import deque

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\07_교육과정설계\in1.txt"
sys.stdin = open(open_dir, "rt")

need = input()
n = int(input())


for i in range(n):
    plan = input()
    dq = deque(need)

    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" % (i+1))
        else:
            print("#%d NO" % (i+1))
