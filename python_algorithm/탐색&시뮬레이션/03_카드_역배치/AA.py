import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\03_카드_역배치\in1.txt"
# sys.stdin = open(open_dir, "rt")

deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for _ in range(10):
    a, b = map(int, input().split())
    # print(a, b)

    split = list(reversed(deck[a:b+1]))

    deck = deck[:a] + split + deck[b+1:]


for i in range(1, len(deck)):
    print(deck[i], end=" ")