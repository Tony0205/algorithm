import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\01_이분검색\in1.txt"
# sys.stdin = open(open_dir, "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()


def bin_search(start, end, arr):
    mid = (start + end) // 2

    if start > end:
        return False

    if arr[mid] == m:
        return mid+1
    elif arr[mid] > m:
        return bin_search(start, mid-1, arr)
    else:
        # arr[mid] < m
        return bin_search(mid+1, end, arr)


result = bin_search(0, n-1, a)

print(result)
