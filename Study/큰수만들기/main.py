num, k = input().split()
print(num, k)

k = int(k)
stack = []

for n in num:
    while k > 0 and len(stack) > 0 and stack[-1] < n:
        stack.pop()
        k -= 1
    stack.append(n)
    # print(stack)


sli = len(num) - k

# print(stack[:sli])
print("".join(stack))
