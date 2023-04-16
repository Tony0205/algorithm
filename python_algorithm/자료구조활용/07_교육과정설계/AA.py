import sys
from collections import deque

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\07_교육과정설계\in1.txt"
# sys.stdin = open(open_dir, "rt")

required = list(input())
n = int(input())


for i in range(n):
    reqQ1 = deque(required)
    classes = list(input())

    req = reqQ1[0]

    for cls in classes:
        if req == cls:
            req = reqQ1.popleft()
            if reqQ1:
                req = reqQ1[0]
            else:
                break

        # 현재 class가 reqQ1에 있다면,
        # 현재 검색하는 값이 더 나중의 과목이기 때문에 선수과목 법칙을 위배하게 된다.
        if cls in reqQ1:
            break

    if len(reqQ1) == 0:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")
