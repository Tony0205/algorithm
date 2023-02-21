n = int(input())

data = list(map(int, input().split()))
data.sort()

result = 0  # 그룹 수

count = 0  # 모험가 수

for i in data:
    count += 1  # 모험가 수 증가시키기

    # 모험가 수가 모험가의 공포도 보다 크거나 같다면,
    if count >= i:
        result += 1  # 그룹 수 증가
        count = 0  # 모험가 수 초기화

print(result)
