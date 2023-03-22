import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\11_격자판_회문수\in1.txt"
# sys.stdin = open(open_dir, "rt")

board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(3):
    for j in range(7):
        # 행 회문 검사
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1

        # 열 회문 검사
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1

print(cnt)
