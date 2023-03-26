import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\04_마구간정하기(결정)\in1.txt"
# sys.stdin = open(open_dir, "rt")


def Count(len):
    cnt = 1
    ep = Line[0]

    for i in range(1, n):
        if Line[i]-ep >= len:
            cnt += 1
            ep = Line[i]
    return cnt


n, c = map(int, input().split())
Line = []


for _ in range(n):
    Line.append(int(input()))

Line.sort()

lt = 1
rt = Line[n-1]

res = 0
while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)
