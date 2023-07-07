import sys
sys.setrecursionlimit(10**8)

def dfs(V):
    global cnt
    visit[V] = cnt
    graph[V].sort(reverse=True)
    for x in graph[V]:
        if not visit[x]:
            cnt += 1
            dfs(x)

# 정점의 수 N, 간선의 수 M, 시작 정점 R
N, M, R = map(int, sys.stdin.readline().split())
# 방문 순서를 담은 변수 cnt
cnt = 1
# 간선 정보를 저장할 배열 graph
graph = [[] for _ in range(N+1)]
# 방문 여부와 방문 순서를 저장하는 배열 visit
visit = [0]*(N+1)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
# dfs 실행
dfs(R)
# i번째 줄에는 정점 i의 방문 순서를 출력
for v in visit[1:]:
    print(v)