from heapq import heappush, heappop
import sys

def dijkstra(start):
    answer[start] = 0
    heappush(queue, (0, start))
    while queue:
        c_weight, c_node = heappop(queue)

        # 현재노드까지의 가중치가 갱신되지 않아도 되는 경우
        if answer[c_node] < c_weight:
            continue

        for n_node, weight in route[c_node]:
            n_weight = answer[c_node] + weight
            if answer[n_node] > n_weight:
                answer[n_node] = n_weight
                heappush(queue, (n_weight, n_node))

# 정점의 개수 V와 간선의 개수 E
V, E = map(int, sys.stdin.readline().split())
# 시작 정점의 번호 K
K = int(sys.stdin.readline())
# 정점의 정보를 저장하는 배열 route
route = [[] for _ in range(V)]
# dijkstra함수에서 활용할 배열 queue
queue = []
# INF의 값을 변수 INF에 저장
INF = float('inf')
# 각 노드의 가중치를 저장할 배열 answer
answer = [INF] * V

for _ in range(E):
    # u에서 v로 가는 가중치 w
    u, v, w = map(int, sys.stdin.readline().split())
    route[u-1].append((v-1, w))

dijkstra(K-1)

# 최단 경로의 경로값을 출력한
for a in answer:
    print(a if a != INF else 'INF')