from heapq import heappush, heappop
import sys

def dijkstra(start):
    # 최단길이를 저장하는 배열 distance
    distance = [INF] * N
    distance[start] = 0
    heappush(queue, (0, start))

    while queue:
        c_weight, c_node = heappop(queue)

        if distance[c_node] < c_weight:
            continue

        for n_node, weight in route[c_node]:
            n_weight = distance[c_node] + weight

            if distance[n_node] > n_weight:
                distance[n_node] = n_weight
                heappush(queue, (n_weight, n_node))
    return distance

# 정점의 개수 N과 간선의 개수 E
N, E = map(int, sys.stdin.readline().split())
# 정점의 정보를 담을 배열 route
route = [[] for _ in range(N)]
queue = []
INF = float('inf')

for _ in range(E):
    # a번 정점에서 b번 정점까지 거리가 c
    a, b, c = map(int, sys.stdin.readline().split())

    route[a-1].append((b-1, c))
    route[b-1].append((a-1, c))
# 반드시 거쳐야하는 두개의 서로 다른 정점
v1, v2 = map(int, sys.stdin.readline().split())
# 1, v1, v2 노드에서 출발할 때 최단 경로 d0, d1, d2
d0 = dijkstra(0)
d1 = dijkstra(v1-1)
d2 = dijkstra(v2-1)
# v1, v2를 지나 N에 도달하는 최단 경로의 방번 두가지 way1, way2
way1 = d0[v1-1] + d1[v2-1] + d2[N-1]
way2 = d0[v2-1] + d2[v1-1] + d1[N-1]
# way1와 way2 중 짧은 경로를 변수 answer에 저장
answer = min(way1, way2)
# 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력
print(answer if answer < INF else -1)