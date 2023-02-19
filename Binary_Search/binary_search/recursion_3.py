n, t = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

def b_search(arr, t, start, end):
    mid = (start + end) // 2

    # Base Case
    if start > end:
        return None

    if arr[mid] == t:
        return mid + 1  # 위치 반환
    elif arr[mid] > t:
        end = mid - 1
        return b_search(arr, t, start, end)
    else:
        start = mid + 1
        return b_search(arr, t, start, end)


result = b_search(arr=array, t=t, start=0, end=n - 1)

print(result)
