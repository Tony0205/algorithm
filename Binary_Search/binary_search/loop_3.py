n, t = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()


def b_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid + 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


result = b_search(arr, t, 0, n - 1)

print(result)
