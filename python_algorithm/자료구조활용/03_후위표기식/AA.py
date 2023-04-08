# import sys

# # open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\03_후위표기식\in1.txt"
# # sys.stdin = open(open_dir, "rt")

# exp = list(input())

# prec = {
#     "*": 3,
#     "/": 3,
#     "+": 2,
#     "-": 2,
#     "(": 1,
#     ")": 1,
# }
# postfix = ""
# stack = []
# for x in exp:
#     if x in prec:
#         if len(stack) == 0:
#             stack.append(x)
#             continue

#         if x == "(":
#             stack.append(x)
#             continue
#         if x == ")":
#             while stack:
#                 s = stack.pop()
#                 if s == "(":                    
#                     break
#                 else:
#                     postfix += s

#         if prec[stack[-1]] < prec[x]:
#             stack.append(x)
#         else:
#             postfix += stack.pop()            
#             stack.append(x)
#     else:
#         postfix += x


# while stack:
#     s = stack.pop()
#     if s != "(" and s != ")":
#         postfix += s

# print(postfix)
