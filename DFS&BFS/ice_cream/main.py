# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
print(n, m)

graph_data = []
for i in range(n):
  graph_data.append(list(map(int, input())))

print("graph_data", graph_data)

def dfs(x, y):
  # 그래프의 범위를 벗어나면 즉시 종료
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  
  # 현재 그래프를 방문하지 않았다면,
  if graph_data[x][y] == 0:
    # 방문처리
    graph_data[x][y] = 1

    # 상, 하, 좌, 우 확인 및 방문처리
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  # 방문한 곳은 자연스레 False로 처리
  return False


result = 0

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print("만들수있는 음료수의 개수는?", result)



