# 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

print("n=", n, " m=", m, " K=", k)
print(data)

sum = 0
# m번 더한다
i = 1
while i <= m:
  # 연속해서 K+1 배수마다 그 다음으로 작은 수가 나옴 (연속 성립)
  if i % (k+1) == 0:
    sum += data[1]
  else:
    # 이 외에는 연속하는 수를 더해준다. (제일 큰 수)
    sum += data[0]
  i+= 1

print(sum)
  
  

