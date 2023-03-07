
import sys

sys.stdin = open(r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\코드_구현력_기르기\02_K번째수\in1.txt", "rt")

T = int(input())

for i in range(T):
    n, s, e, k = map(int, input().split())
    data = list(map(int, input().split()))    

    new_data = sorted(data[s-1:e])
    print(f'#{i+1} {new_data[k-1]}')



