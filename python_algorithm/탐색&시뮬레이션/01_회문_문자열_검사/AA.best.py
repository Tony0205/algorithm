import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\01_회문_문자열_검사\in1.txt"
sys.stdin = open(open_dir, "rt")

n = int(input())

for i in range(n):
    s = input().lower()

    size = len(s)

    # 절반까지만 값이 같은지 확인하면 됨 (그려서 확인하기)
    for i in range(size//2):
        if s[i] != s[-1-i]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
    


   