import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\코드_구현력_기르기\05_정다면체\in1.txt"
# sys.stdin = open(open_dir, "rt")

n, m = map(int, input().split())

dice_cnt = [0 for _ in range(n + m + 1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        sum_of_dice = i+j
        dice_cnt[sum_of_dice] += 1

max_noon = -1

for x in dice_cnt:
    if x > max_noon:
        max_noon = x


for idx, x in enumerate(dice_cnt):
    if x == max_noon:
        print(idx, end=" ")
