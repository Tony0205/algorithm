n = int(input())

part_list = list(map(int, input().split()))

m = int(input())

target_parts = list(map(int, input().split()))

part_list.sort()

def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        start = mid + 1
        return binary_search(arr, target, start, end)
    else:
        end = mid - 1
        return binary_search(arr, target, start, end)


for t_part in target_parts:
    result = binary_search(part_list, t_part, 0, n-1)
    if result != None:
        print('Yes', end=' ')
    else:
        print('No', end=' ')
