import sys
from itertools import combinations

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\코드_구현력_기르기\03_K번째_큰_수\in2.txt"
# sys.stdin = open(open_dir, "rt")

n, k = map(int, input().split())

data = list(map(int, input().split()))

result = list(combinations(data, 3))

sum_list = set()

for res in result:
    sum_list.add(sum(res))

sorted_val = sorted(sum_list, reverse=True)

print(sorted_val[k-1])


