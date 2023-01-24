import sys

def bfs(mid):


# 섬의 개수 N, 다리의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 중량제한의 정보를 저장할 island
island = [[0] * (N + 1) for _ in range(N + 1)]
start, end = 0, 0

for _ in range(M):
    land1, land2, weight = map(int, sys.stdin.readline().split())
    island[land1][land2] = weight
    island[land2][land1] = weight
    end = max(end, weight)

# 공장의 위치 L1, L2
L1, L2 = map(int, sys.stdin.readline().split())