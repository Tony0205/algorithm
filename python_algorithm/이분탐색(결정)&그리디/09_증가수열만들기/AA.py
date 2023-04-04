import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\09_증가수열만들기\in1.txt"
sys.stdin = open(open_dir, "rt")

n = int(input())
a = list(map(int, input().split()))

print(n, a)

# 증가수열의 마지막 숫자
last_incremental_seq = 0
seq_cnt = 0
order_text = ""

while a:
    # 앞이 더 작을 때,
    if last_incremental_seq < a[0] and a[0] < a[-1]:
        last_incremental_seq = a.pop(0)
        seq_cnt += 1
        order_text += "L"
    # 뒤가 더 작을 때,
    elif last_incremental_seq < a[-1] and a[0] > a[-1]:
        last_incremental_seq = a.pop()
        seq_cnt += 1
        order_text += "R"
    else:
        break


print(seq_cnt)
print(order_text)
