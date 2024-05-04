import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    global cnt
    visit[start] = cnt
    for node in graph[start]:
        if not visit[node]:
            cnt += 1
            dfs(node)

# 정점의 수 N, 간선의 수 M, 시작 정점 R
N, M, R = map(int, sys.stdin.readline().split())
# 간선의 정보를 저장하는 배열 graph
graph = [[] for _ in range(N+1)]
# idx번 간선의 방문순서를 저장하는 배열 visit
visit = [0] * (N+1)
# 방문순서 cnt
cnt = 1

for _ in range(M):
    # 연결된 간선정보 u, v를 graph에저장
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for s in range(1, N+1):
    # 인접 정점은 오름차순으로 방문된다.
    graph[s].sort()

# 시작 정점에서 dfs을 시작한다.
dfs(R)

# i번째 줄에는 정점 i의 방문 순서를 출력
for v in visit[1:]:
    print(v)