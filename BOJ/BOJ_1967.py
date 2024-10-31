# dfs

import sys
sys.setrecursionlimit(10**5)

def dfs(node, dist):
    for next, d in graph[node]:
        if visit[next] == -1:
            visit[next] = dist + d
            dfs(next, dist + d)

# 노드의 개수 N
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visit = [-1] * (N+1)

for _ in range(N-1):
    # 부모 노드 번호 A, 자식 노드 번호 B, 간선의 가중치 M
    A, B, M = map(int, sys.stdin.readline().split())
    graph[A].append((B, M))
    graph[B].append((A, M))

# 루트노드 1에서 도달하는 가중치를 구한다
visit[1] = 0
dfs(1, 0)

# 트리의 지름이 되는 노드 goal
goal = visit.index(max(visit))

# goal에서 함수 dfs 실행
visit = [-1] * (N+1)
visit[goal] = 0
dfs(goal, 0)

# 트리의 지름을 출력
print(max(visit))