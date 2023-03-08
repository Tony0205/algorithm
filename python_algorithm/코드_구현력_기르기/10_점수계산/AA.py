import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\코드_구현력_기르기\10_점수계산\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())
a = list(map(int, input().split()))

t_point = 0
acc = 0
for x in a:       
    if x == 1:
        acc += 1
        t_point += acc
    else:        
        acc = 0    

print(t_point)
