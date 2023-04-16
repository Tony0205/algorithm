import sys
from collections import deque

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\09_아나그램\in1.txt"
# sys.stdin = open(open_dir, "rt")

A = list(input())
B = list(input())

# print(A, B)

word_dict = {}
for x in A:
    if x in word_dict:
        word_dict[x] += 1
    else:
        word_dict[x] = 1

for y in B:
    if y in word_dict:
        word_dict[y] -= 1
    else:
        word_dict[y] = 1


# print(word_dict)

if any(x > 0 for x in word_dict.values()):
    print("NO")
else:
    print("YES")
