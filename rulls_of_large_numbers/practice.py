# 배열의 개수? n, 몇번 더하는지? m, 연속해서 k번 나올수 있는지? 입력받기
n, m, k = map(int, input().split())
# data 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True)

print(data)

# 가장 큰 수가 연속적으로 곱해지는 반복횟수
# (m / (k+1)) : 수열의 반복 횟수
# 위에 * k번 하면 큰수가 몇번곱해지는지 나온다.
count = (m // (k + 1)) * k  # 몫만 계산
count += (m % (k + 1))  # 나머지 계산

# 첫번째로 큰수 계산하고
sum = count * data[0]

# 나머지 그 다음 작은수는 몇번?
sum += (m - count) * data[1]

print(sum)
