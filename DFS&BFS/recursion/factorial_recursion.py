def factorial_recursion(n):
  print(n)
  if n <= 1:
    return 1
  return n * factorial_recursion(n-1)


result = factorial_recursion(5)

print(result)