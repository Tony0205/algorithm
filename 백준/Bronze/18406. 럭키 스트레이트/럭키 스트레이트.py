n = input()

half = len(n) // 2
# print(half)
left_number_list = list(n[:half])
right_number_list = list(n[half:])
# print(left_number, right_number)
left_sum = sum(map(int, left_number_list))
right_sum = sum(map(int, right_number_list))

# print(left_sum, right_sum)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
