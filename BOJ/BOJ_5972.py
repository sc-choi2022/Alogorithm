from heapq import heappush, heappop
import sys

def dijkstra(start):
    answer[start] = 0
    heappush(queue, [0, start])

    while queue:
        c_weight, c_node = heappop(queue)

        if answer[c_node] < c_weight:
            continue
        for n_node, weight in route[c_node]:
            n_weight = c_weight + weight
            if n_weight < answer[n_node]:
                answer[n_node] = n_weight
                heappush(queue, (n_weight, n_node))

# 헛간의 개수 N, 소들의 길 M
N, M = map(int, sys.stdin.readline().split())
route = [[] for _ in range(N)]
INF = float('inf')
answer = [INF] * N
queue = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    route[a-1].append((b-1, c))
    route[b-1].append((a-1, c))

dijkstra(0)
print(answer[N-1])