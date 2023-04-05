import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\01_가장큰수\in1.txt"
# sys.stdin = open(open_dir, "rt")

a, m = map(int, input().split())

# print(a, m)

stack = []

for x in list(str(a)):
    while stack:
        if stack[-1] < x and m != 0:
            stack.pop()
            m -= 1
        else:
            stack.append(x)
            break
    if len(stack) == 0:
        stack.append(x)
        continue

if m > 0:
    stack = stack[:-m]


for s in stack:
    print(s, end="")

# 통과