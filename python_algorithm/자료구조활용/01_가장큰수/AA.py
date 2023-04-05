# import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\01_가장큰수\in1.txt"
# sys.stdin = open(open_dir, "rt")

# a, m = map(int, input().split())

# # print(a, m)

# stack = []
# remove_cnt = 0

# for x in list(str(a)):
#     target = int(x)

#     if len(stack) == 0:
#         stack.append(target)
#         continue

#     if stack[-1] < target:
#         if remove_cnt < m:
#             stack.pop()
#             stack.append(target)
#             remove_cnt += 1
#         else:
#             stack.append(target)
#     else:
#         if remove_cnt < m:
#             remove_cnt += 1
#         else:
#             stack.append(target)


# for s in stack:
#     print(s, end="")
