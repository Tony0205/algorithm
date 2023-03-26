import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\03_뮤직비디오(결정)\in1.txt"
sys.stdin = open(open_dir, "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

maxx = max(a)
lt = 1
rt = sum(a)

res = 0
while lt <= rt:
    mid = (lt + rt) // 2

    dvd_cnt = 1
    whole = 0
    for x in a:
        # 레코드가 최소 값을 넘지 않을때
        # print(whole)
        if whole + x <= mid:
            whole += x
        else:
            whole = x
            dvd_cnt += 1

    # print("dvd_cnt", dvd_cnt, mid)
    if mid >= maxx and dvd_cnt <= m:
        rt = mid - 1
        res = mid
        # print(res)
    else:
        lt = mid + 1

print(res)
