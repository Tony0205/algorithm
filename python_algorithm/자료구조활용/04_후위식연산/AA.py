import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\04_후위식연산\in1.txt"
# sys.stdin = open(open_dir, "rt")

a = input()
stack = []

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        # 연산자를 만나면... 계산을 한다
        c = stack.pop()
        b = stack.pop()

        if x == "+":
            res = b + c
        elif x == "-":
            res = b - c
        elif x == "*":
            res = b * c
        elif x == "/":
            res = b / c

        # 계산 결과를 다시 스택에 넣어줌 (추후에 사용할 수 있기 때문) 
        stack.append(res)


print(stack.pop())
