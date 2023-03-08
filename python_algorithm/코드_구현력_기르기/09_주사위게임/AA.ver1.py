import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\코드_구현력_기르기\09_주사위게임\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())

max_res = -1
for x in range(n):
    a, b, c = map(int, input().split())

    # 세 눈이 같을 때
    if a == b and b == c:
        price = 10000 + a * 1000
    elif a == b or a == c:
        price = 1000 + a * 100
    elif b == c:
        price = 1000 + a * 100
    else:
        price = max(a, b, c) * 100

    if max_res < price:
        max_res = price

print(max_res)
