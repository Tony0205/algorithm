import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\코드_구현력_기르기\08_뒤집은소수\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())

data = list(map(int, input().split()))


def reverse(x):
    res = 0    
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    
    return res


def isPrime(x):
    if x == 1:
        return False
    
    for n in range(2, (x // 2) + 1):
        if x % n == 0:
            return False
    else:
        return True        

for d in data:
    temp = reverse(d)
    
    if isPrime(temp):  
        print(temp, end=" ")
