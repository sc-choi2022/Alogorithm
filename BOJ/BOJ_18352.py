from collections import deque

# 도시의 수 N, 도로의 수 M, 최단거리의 기준 K, 시작 노드 X
N, M, K, X = map(int, input().split())

city = [[] for _ in range(N + 1)]
visited = [-1]*(N + 1)
visited[X] = 0
queue = deque()
queue.append(X)

for _ in range(M):
    start, end = map(int, input().split())
    city[start].append(end)

while queue:
    start = queue.popleft()
    for end in city[start]:
        if visited[end] == -1:
            visited[end] = visited[start] + 1
            queue.append(end)

for i in range(N+1):
    if visited[i] == K:
        print(i)

if K not in visited:
    print(-1)