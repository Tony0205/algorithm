import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\10_스도쿠_검사\in1.txt"
sys.stdin = open(open_dir, "rt")

def check(a):
    # 행과 열을 검사
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1

        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    # 그룹을 검사
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False

    return True


a = [list(map(int, input().split())) for _ in range(9)]

if check(a):
    print("YES")
else:
    print("NO")
