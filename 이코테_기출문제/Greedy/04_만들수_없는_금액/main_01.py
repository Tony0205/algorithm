n = int(input())

coins = list(map(int, input().split()))

# INF = int(1e9)

coins.sort()

# print(coins)

result = 1

sli = -1
sumCoinVal = 0
while sli < len(coins):
    sli += 1
    for coin in coins[sli:]:
        # print("coin, sumCoin", coin, sumCoinVal)
        sumCoinVal += coin
        if result == sumCoinVal:
            result += 1
            # print("result", result)
            sli = -1
            break

    sumCoinVal = 0
    # print("sli", sli)

print("만들 수 없는 양의 정수?", result)
