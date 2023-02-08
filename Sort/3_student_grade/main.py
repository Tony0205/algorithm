n = int(input())


students = []
for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))

#  Key를 이용하여 점수를 기준으로 정렬한다.
students.sort(key=lambda x: x[1])

print(students)

for item in students:
    print(item[0], end=' ')