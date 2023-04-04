import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\09_증가수열만들기\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n - 1
last = 0
res = ""

tmp = []
while lt <= rt:
    if last > a[lt] and last > a[rt]:
        break

    tmp.append((a[lt], "L"))
    tmp.append((a[rt], "R"))
    tmp.sort()

    if tmp[0][0] < last and tmp[1][0] > last:
        res += tmp[1][1]
        last = tmp[1][0]

        if tmp[1][1] == "R":
            rt -= 1
        else:
            lt += 1

    else:
        res += tmp[0][1]
        last = tmp[0][0]

        if tmp[0][1] == "R":
            rt -= 1
        else:
            lt += 1

    # print(text)

    tmp = []


print(len(res))
print(res)
