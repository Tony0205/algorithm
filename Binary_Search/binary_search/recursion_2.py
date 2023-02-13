n, t = map(int, input().split())

arr = list(map(int, input().split()))

print(n, t, arr)

# 정렬하기
arr.sort()


def binary_search(array, target, start, end):
    mid = (start + end) // 2

    # Base Case 입력
    if start > end:
        return None

    if array[mid] == target:
        return mid + 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


result = binary_search(arr, t, 0, n - 1)

print(result)
