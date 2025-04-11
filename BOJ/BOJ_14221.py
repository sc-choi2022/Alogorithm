from heapq import heappush, heappop
import sys

def dijkstra(start):
    answer[start] = 0
    heappush(queue,[0, start])

    while queue:
        c_weight, c_node = heappop(queue)

        if answer[c_node] < c_weight:
            continue
        for n_node, weight in graph[c_node]:
            n_weight = c_weight + weight

            if n_weight < answer[n_node]:
                answer[n_node] = n_weight
                heappush(queue, [n_weight, n_node])

# 정점의 개수 N, 간선의 개수 M
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
INF = float('inf')
answer = [INF]*(N+1)
queue = []

for _ in range(M):
    # 정점 a, b, 간선의 거리 c
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

# 집의 후보지의 개수 P, 편의점의 개수 Q
P, Q = map(int, sys.stdin.readline().split())
# 집의 후보지 house
houses = list(map(int, sys.stdin.readline().split()))
# 편의점의 후보지 cvs
cvs = list(map(int, sys.stdin.readline().split()))

for i in range(P):
    dijkstra(i)
print(answer)