import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\완전탐색_DFS\01_재귀함수_이진수_출력\in1.txt"
sys.stdin = open(open_dir, "rt")

result = ""


def DFS(x):
    global result

    if x == 0:
        return
    else:
        r1 = x // 2
        r2 = x % 2

        result = str(r2) + result
        DFS(r1)


if __name__ == "__main__":
    n = int(input())

    DFS(n)

    print(result)
