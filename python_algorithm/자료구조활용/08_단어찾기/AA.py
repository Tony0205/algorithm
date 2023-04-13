import sys
from collections import deque

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\08_단어찾기\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())

wordDict = {}

for _ in range(n):
    word = input()
    wordDict[word] = 1


for _ in range(n-1):
    word2 = input()

    if word2 in wordDict:
        del wordDict[word2]

print(list(wordDict.keys())[0])
