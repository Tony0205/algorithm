n, t = map(int, input().split())

d = list(map(int, input().split()))


def binary_search(data, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid + 1  # index가 아닌 위치로 반환해야됨.

    # Target이 중앙값보다 크다면, 왼쪽을 날린다.
    if data[mid] < target:
        start = mid + 1
        return binary_search(data, target, start, end)
        # Target이 중앙값보다 작거나 같다면, 오른쪽을 날린다.
    else:
        end = mid - 1
        return binary_search(data, target, start, end)


result = binary_search(d, t, 0, n - 1)

print(result)
