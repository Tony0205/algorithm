from collections import deque

# n, m 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

print("graph:", graph)

# 이동할 방향 정의하기 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  # Deque 사용
  queue = deque()
  queue.append((x, y))

  while queue:
    # 1. x = 0, y = 0
    x, y = queue.popleft()
    print("x, y:", x, y)
     
    # 현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      print("nx, ny:", nx, ny)

      # 미로 찾기 공간 벗어나면 무시, n=5 / m=6
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      # 벽인 경우 무시 (괴물)
      if graph[nx][ny] == 0:
        continue

      # 지나온 미로 공간은 1이 아니기 때문에 지나치게 된다.
      print("graph[nx][ny]", graph[nx][ny])
      
      # 해당 노드를 처음 방문하는 경우에는 1로 적용되어 있으므로, 이때 최단 거리를 기록한다.
      if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          queue.append((nx, ny))
          print("queue.append((nx, ny))", nx, ny)
      
    print("graph", graph)
  print("==============================")
  # 가장 오른쪽 아래까지의 최단거리 반환
  return graph[n-1][m-1]

print("bfs:", bfs(0, 0))
