import sys, heapq

# 정점의 개수 V, 간선의 개수 E
V, E = map(int, sys.stdin.readline().split())
# 시작 정점의 번호 K
K = int(sys.stdin.readline())

route = [[] for _ in range(V + 1)]

INF = float('inf')
# 비용을 미리 무한대로 초기화
answer = [INF] * (V + 1)
queue = []

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    route[u].append([v, w])

def dijkstra(start):
    answer[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        current_w, current_node = heapq.heappop(queue)

        if answer[current_node] < current_w:
            continue

        for next_node, weight in route[current_node]:
            next_w = current_w + weight

            if next_w < answer[next_node]:
                answer[next_node] = next_w
                heapq.heappush(queue, [next_w, next_node])

dijkstra(K)

for j in answer[1:]:
    print(j if j != INF else 'INF')