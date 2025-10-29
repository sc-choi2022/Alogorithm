from itertools import combinations
import sys

# 집의 개수 N, 설치하는 대피소의 개수 K
N, K = map(int, sys.stdin.readline().split())

x, y = [0] * N, [0] * N
for i in range(N):
    x[i], y[i] = map(int, sys.stdin.readline().split())

INF = float('INF')

for c in combinations(range(N), K):
    continue