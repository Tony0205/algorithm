import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\01_가장큰수\in1.txt"
sys.stdin = open(open_dir, "rt")

num, m = map(int, input().split())

num = list(map(int, str(num)))

stack = []

for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]


res = ''.join(map(str, stack))
print(res)