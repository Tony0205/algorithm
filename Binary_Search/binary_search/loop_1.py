n, target = map(int, input().split())

arr = list(map(int, input().split()))


def bn_search_using_loop():
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


result = bn_search_using_loop()

print(result)
