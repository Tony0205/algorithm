n = int(input())

array = set(map(int, input().split()))

print("set?", array)

m = int(input())

x = list(map(int, input().split()))

for t in x:
    if t in array:
        print('YES', end=' ')
    else:
        print('NO', end=' ')
