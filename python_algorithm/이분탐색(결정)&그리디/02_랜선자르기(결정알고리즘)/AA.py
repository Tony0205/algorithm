import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\02_랜선자르기(결정알고리즘)\in1.txt"
# sys.stdin = open(open_dir, "rt")

k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]


lt = 1
rt = max(a)

max_cable_length = rt

while lt <= rt:
    mid = (lt+rt) // 2

    res = 0
    for x in a:
        res += x // mid  # 각 원소에 따라 만들 수 있는 랜선 개수 모두 더하기

    # 랜선의 개수가 초과하거나 같으면
    if res >= n:
        max_cable_length = mid  # 값 저장
        lt = mid + 1
    else:
        # 랜선의 개수가 부족하면,
        rt = mid - 1


print(max_cable_length)
