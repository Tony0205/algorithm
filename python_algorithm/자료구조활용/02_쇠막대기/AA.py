import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\02_쇠막대기\in1.txt"
sys.stdin = open(open_dir, "rt")

a = list(input())

stack = []
sum = 0
for i in range(len(a)):
    if a[i] == "(":
        stack.append(a[i])
    else:
        # 닫는 괄호일 때,
        stack.pop()
        if a[i-1] == ")":
            # stack.pop()
            sum += 1
        else:
            # stack.pop()
            sum += len(stack)

print(sum)
