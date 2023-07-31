from collections import deque
import sys

def bfs(start):
    global cnt
    visit[start] = 1
    queue = deque([start])
    cnt += 1
    while queue:
        current = queue.popleft()
        graph[current].sort(reverse=True)

        for next in graph[current]:
            if not visit[next]:
                visit[next] = cnt
                queue.append(next)
                cnt += 1

# 정점의 개수 N, 간선의 개수 M의 무방향 그래프, 시작 정점 R
N, M, R = map(int, sys.stdin.readline().split())
# 간선의 정보를 저장하는 배열 graph
graph = [[] for _ in range(N+1)]
# 방문순서를 저장하는 배열
visit = [0]*(N+1)
# 방문 순서 cnt
cnt = 1

for _ in range(M):
    # 정점 u, 정점 v, 가중치 1인 양방향 간선
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
# 시작 정점 R부터 bfs 시작
bfs(R)

# i번째 줄에는 정점 i의 방문 순서를 출력
for i in range(1, N+1):
    print(visit[i])