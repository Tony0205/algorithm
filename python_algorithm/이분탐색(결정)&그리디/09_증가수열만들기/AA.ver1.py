import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\이분탐색(결정)&그리디\09_증가수열만들기\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())
a = list(map(int, input().split()))

# print(n, a)

incremented_seq = []
seq_text = ""
for i in range(1, n + 1):
    if a[0] == i:
        incremented_seq.append(a.pop(0))
        seq_text += "L"

    if a[-1] == i:
        incremented_seq.append(a.pop())
        seq_text += "R"


print(len(incremented_seq))
print(seq_text)
