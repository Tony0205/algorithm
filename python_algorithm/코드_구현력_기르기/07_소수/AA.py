import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\코드_구현력_기르기\07_소수\in2.txt"
sys.stdin = open(open_dir, "rt")

n = int(input())

ch = [0] * (n+1)

cnt = 0
for i in range(2, n + 1):
    # i 번째 수가, 0이면
    if ch[i] == 0:
        # cnt + 1을 해주고,
        cnt += 1
        for j in range(i, n + 1, i):            
            ch[j] = 1            

print(cnt)

