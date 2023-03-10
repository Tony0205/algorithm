import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\04_두_리스트_합치기\in1.txt"
sys.stdin = open(open_dir, "rt")


n = input()
d1 = list(map(int, input().split()))
m = input()
d2 = list(map(int, input().split()))


p1 = 0
i = 0
p2 = 0
j = 0
res = []
while True:
    # d1이 끝까지 도달했다면,
    if i > len(d1)-1:
        # d2를 이어 붙여준다
        res = res + d2[j:]
        break

    # d2가 끝까지 도달했다면
    if j > len(d2)-1:
        res = res + d1[i:]
        break

    p1 = d1[i]
    p2 = d2[j]

    if p1 <= p2:
        res.append(p1)
        i += 1
    else:
        res.append(p2)
        j += 1


for r in res:
    print(r, end=" ")
