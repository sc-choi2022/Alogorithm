import sys

def BF(start):
    dist[start] = 0

    for i in range(1, N+1):
        for edge in edges:
            current, next, cost = edge

            if dist[current] != float('INF') and dist[next] > dist[current] + cost:
                dist[next] = dist[current] + cost
                if i == N:
                    return True
    return False

# 도시의 개수 N, 버스 노선의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 도시의 이동시간을 저장하는 배열 edges
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
dist = [float('INF')] * (N+1)

if BF(1):
    print(-1)
else:
    for k in range(2, N+1):
        # 도달 불가능한 경우
        if dist[k] == float('INF'):
            print(-1)
        # 도달 가능한 경우
        else:
            print(dist[k])