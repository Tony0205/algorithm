import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\03_카드_역배치\in1.txt"
# sys.stdin = open(open_dir, "rt")

deck = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    
    for i in range((e-s+1)//2):        
        deck[s+i], deck[e-i] = deck[e-i], deck[s+i]
    


for i in range(1, len(deck)):
    print(deck[i], end=" ")