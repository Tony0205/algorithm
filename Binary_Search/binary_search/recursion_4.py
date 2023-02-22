n, t = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()


def binary_search(arr, target, start, end):
    mid = (start + end) // 2

    if start > end:
        return None

    if target == arr[mid]:
        return mid + 1
    elif target > arr[mid]:
        start = mid + 1
        return binary_search(arr, target, start, end)
    else:
        end = mid - 1
        return binary_search(arr, target, start, end)


result = binary_search(arr, t, 0, n - 1)

print(result)
