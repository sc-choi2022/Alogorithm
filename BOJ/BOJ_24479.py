import sys

def dfs(start):

    for j in range(1, N+1):
        if graph[start][j] and not visit[j]:
            visit[j] = 1
            return j
    return 0

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)