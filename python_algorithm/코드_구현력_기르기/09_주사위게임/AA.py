import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\코드_구현력_기르기\09_주사위게임\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())

prices = []

for x in range(n):
    a = list(map(int, input().split()))

    # 1~6까지의 주사위
    dice = [0] * 7

    for d in a:
        dice[d] += 1

    for idx, num in enumerate(dice):
        # 같은 눈 3개
        if num == 3:
            tot = 10000 + idx * 1000
            prices.append(tot)
            break
        # 같은 눈 2개
        elif num == 2:
            tot = 1000 + idx * 100
            prices.append(tot)
            break
    else:
        # 같은 눈 없을 때
        tot = max(a) * 100
        prices.append(tot)

print(max(prices))