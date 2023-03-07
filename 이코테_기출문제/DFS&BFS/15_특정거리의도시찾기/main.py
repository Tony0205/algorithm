from collections import deque

# n: 도시의 개수 / m: 도로의 개수 / k: 최단 거리 정보 / x: 출발 도시번호
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 각 노드에서 어디를 갈 수 있는지 저장
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # print(graph)

# 초기값 세팅
distance = [-1] * (n + 1)  # 각 도시까지 거리 세팅
distance[x] = 0

q = deque([x])

# 최단거리 계산 BFS
while q:
    now = q.popleft()
    # 현재 시작점에서, 각 노드까지의 거리 계산
    for next_node in graph[now]:
        # 방문하지 않은 노드일 경우
        if distance[next_node] == -1:
            # 다음 노드까지의 거리 = 현재 거리 + 1
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            # print(distance)

# 최단거리가 K인 도시 번호가 있을 때, True
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
