al = list(input())

al.sort()
# print(al)

only_number = list(map(lambda x: int(x) if x.isnumeric() else 0, al))
only_string = list(map(lambda x: x if x.isnumeric() == False else '', al))

sum_number = sum(only_number)
sum_string = "".join(only_string)

if sum_number != 0:
    print(sum_string + str(sum_number))
else:
    print(sum_string)
