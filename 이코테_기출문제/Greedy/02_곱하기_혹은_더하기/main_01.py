num = list(map(int, input()))

print(num)

result = 0
for n in num:
    if n == 0 or n == 1 or result == 0:
        result += n
    else:
        result *= n


print(result)
