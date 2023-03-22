import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\11_격자판_회문수\in1.txt"
sys.stdin = open(open_dir, "rt")

a = [list(map(int, input().split())) for _ in range(7)]

print(a)


def circleNumberCheck(x):
    for i in range(5//2):
        if x[i] != x[5-i-1]:
            return False
    return True


cnt = 0
# 행 검사
for i in range(7):
    for j in range(7):
        if j+5 <= 7:
            x = a[i][j:j+5]

            if circleNumberCheck(x):
                cnt += 1

# 열 검사
s = 0
for i in range(s, 7):
    x = []
    for j in range(7):
        if s < 3:
            x.append(a[j][i])
            if len(x) == 5:
                if circleNumberCheck(x):
                    cnt += 1
                    s += 1
                else:
                    s += 1


print(cnt)
