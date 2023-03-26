import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\06_씨름선수(그리디)\in1.txt"
sys.stdin = open(open_dir, "rt")

n = int(input())

applier = []

for i in range(n):
    h, w = input().split()
    applier.append((h, w))


applier.sort(key=lambda x: (x[0], x[1]), reverse=True)

print(applier)

dropoutList = []

for i in range(n):
    human1 = applier[i]
    for j in range(i+1, n):
        human2 = applier[j]

        # 몸무게도 더 작고, 키도 더 작으면 탈락한다
        if human1[1] > human2[1]:
            if applier[j] not in dropoutList:
                dropoutList.append(applier[j])


# print(dropoutList)

result = len(applier) - len(dropoutList)

print(result)
