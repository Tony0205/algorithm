n, k = map(int, input().split())


aArray = list(map(int, input().split()))
bArray = list(map(int, input().split()))

print(aArray, bArray)

aArray.sort()
bArray.sort(reverse=True)

print("Sort?", aArray, bArray)

# Swap Element
for i in range(k):
  # [P]: A의 원소가 B의 원소보다 작은 경우에만 교체한다.
  if aArray[i] < bArray[i]:
    aArray[i], bArray[i] = bArray[i], aArray[i]
  else: # A의 원소가 B보다 크거나 같다면 더이상 B에는 A보다 큰 원소가 없을것이다. (B는 내림차순 정렬이 되어있기 때문에)
    break
  

print("Swap?", aArray, bArray)

print(sum(aArray))