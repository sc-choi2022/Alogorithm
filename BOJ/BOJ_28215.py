from itertools import combinations
import sys

# 집의 개수 N, 설치하는 대피소의 개수 K
N, K = map(int, sys.stdin.readline().split())

x, y = [0] * N, [0] * N
for i in range(N):
    x[i], y[i] = map(int, sys.stdin.readline().split())

INF = float('INF')

# 가장 가까운 대피소와 집 사이의 거리 중 가장 큰 값이 가장 작을 때의 거리 answer
answer = INF

for c in combinations(range(N), K):
    answer = min(answer, solve(c))

# answer 출력
print(answer)