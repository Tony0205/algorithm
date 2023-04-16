import sys
from collections import deque

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\09_아나그램\in1.txt"
sys.stdin = open(open_dir, "rt")


a = input()
b = input()

str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x, 0) + 1

for x in b:
    str2[x] = str2.get(x, 0) + 1


for key in str1.keys():
    if key in str2.keys():
        if str1[key] != str2[key]:  # value값이 같지 않으면
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
