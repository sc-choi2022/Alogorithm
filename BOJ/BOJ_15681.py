import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    visit[node] = 1
    for next in graph[node]:
        if not visit[next]:
            visit[node] += dfs(next)
    return visit[node]

# 정점의 수 N, 루트의 번호 R, 쿼리의 수 Q
N, R, Q = map(int, sys.stdin.readline().split())
# 간선의 정보를 저장하는 배열 graph, graph 정보를 바탕으로 tree를 저장하는 배열 tree
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    # 간선의 정보 u, v
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [0] * (N+1)
# 루트노드를 시작으로 트리를 구성
dfs(R)

for _ in range(Q):
    # 정점 U
    U = int(sys.stdin.readline())
    # 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력
    print(visit[U])