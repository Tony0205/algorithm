import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\코드_구현력_기르기\06_자릿수의_합\in1.txt"
# sys.stdin = open(open_dir, "rt")


n = map(int, input().split())
data = list(map(str, input().split()))


def digit_sum(x):
    sum = 0
    for y in x:        
        sum += int(y)
    return sum

max = -1
res = -1
for str_num in data:
    # 최대값보다, 더 큰 수가 나온다면
    d_sum = digit_sum(str_num)
    if max < d_sum:
        max = d_sum
        res = str_num

print(res)


    
    


            
    