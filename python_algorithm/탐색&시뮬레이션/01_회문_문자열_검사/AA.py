import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\탐색&시뮬레이션\01_회문_문자열_검사\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())

for i in range(n):
    data = input().lower()

    reversed_data = reversed(data)
    reversed_data = ''.join(reversed_data)    
    
    if data == reversed_data:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")
