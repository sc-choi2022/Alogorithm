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

# bfs
from collections import deque
import sys

def bfs(start):
    global answer
    # 배열 visit 초기화
    visit = [-1] * (N+1)
    visit[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for next, d in graph[current]:
            if visit[next] == -1:
                visit[next] = visit[current] + d
                queue.append(next)
    # 시작 노드에서 최대길이를 갱신
    answer = max(answer, max(visit))

    return visit.index(answer)

# 노드의 개수 N
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visit = [-1] * (N+1)

for _ in range(N-1):
    # 부모 노드 번호 A, 자식 노드 번호 B, 간선의 가중치 M
    A, B, M = map(int, sys.stdin.readline().split())
    graph[A].append((B, M))
    graph[B].append((A, M))

# 트리의 지름 answer
answer = 0
# 루트노드에서의 최대 길이인 노드를 구하고 그 노드를 시작으로 트리의 지름을 구한다.
bfs(bfs(1))
# answer 출력
print(answer)