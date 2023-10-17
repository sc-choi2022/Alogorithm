from collections import deque
import sys

def bfs(V, start):
    queue = deque([start])
    visited[start] = 1
    cnt = 2

    while queue:
        currrent = queue.popleft()

        for next in V[currrent]:
            if not visited[next]:
                visited[next] = cnt
                cnt += 1
                queue.append(next)
# 정점의 수 N, 간선의 수 M, 시작 정점 R
N, M, R = map(int, sys.stdin.readline().rstrip().split())
# 간선 정보를 저장하는 배열 graph
graph = [[] for _ in range(N+1)]
# 방문 순서를 저장하는 배열 visited
visited = [0] * (N + 1)

for _ in range(M):
    # 정점 u, v
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
# 간선 정보를 오름차순으로 정렬
for i in range(1, N+1):
    graph[i].sort()

bfs(graph, R)
# i번째 줄에는 정점 i의 방문 순서를 출력
for j in range(1, N+1):
    print(visited[j])