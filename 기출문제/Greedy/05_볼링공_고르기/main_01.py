n, m = map(int, input().split())

ball = list(map(int, input().split()))


# 경우의 수
number_of_cases = 0
for i in range(n):
    for j in range(n):
        if i < j:
            if ball[i] != ball[j]:
                number_of_cases += 1

print("볼링공 고르는 경우의 수는?", number_of_cases)
