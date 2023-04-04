import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\08_침몰하는_타이타닉(그리디)\in2.txt"
# sys.stdin = open(open_dir, "rt")

n, m = map(int, input().split())
people = list(map(int, input().split()))


# 다 탈출할 때 까지 loop
cnt = 0
while len(people) > 0:
    if len(people) == 1:
        cnt += 1
        break

    passenger = people.pop(0)
    remain_weight = m - passenger

    smallest = 9999
    smIndex = n + 999

    for i, x in enumerate(people):
        subtracted_val = remain_weight - x
        if subtracted_val >= 0 and smallest > subtracted_val:
            smallest = subtracted_val
            smIndex = i

    # 승객들 보트에 태우기
    if smIndex != n + 999:
        del people[smIndex]
    cnt += 1

print(cnt)
