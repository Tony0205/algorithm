n, target = map(int, input().split())

arr = list(map(int, input().split()))


def b_search():
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid + 1
        elif arr[mid] > target:
            # 오른쪽을 날린다.
            end = mid - 1
        else:
            start = mid + 1

    return None


result = b_search()

print(result)
