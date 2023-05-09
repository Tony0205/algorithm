import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\완전탐색_DFS\02_부분집합(DFS)\in1.txt"
sys.stdin = open(open_dir, "rt")

result = ""


def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=" ")
        print()
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n+1)
    DFS(1)
