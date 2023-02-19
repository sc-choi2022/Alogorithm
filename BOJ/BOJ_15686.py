from itertools import combinations
import sys

# 도시의 크기 NxN, 치킨집의 최대 개수 M
N, M = map(int, sys.stdin.readline().split())

# 집과 치킨집의 위치를 담은 배열 zido
zido = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

house, chicken = [], []
ans = N*N*N
for i in range(N):
    for j in range(N):
        if zido[i][j] == 1:
            house.append((i, j))
        elif zido[i][j] == 2:
            chicken.append((i, j))

combination = list(combinations(chicken, M))

for combi in combination:
    cnt = [[N * N * N] * N for _ in range(N)]
    for c in combi:
        for h in house:
            cnt[h[0]][h[1]] = min(cnt[h[0]][h[1]], abs(h[0] - c[0]) + abs(h[1] - c[1]))
    tmp = 0
    for h in house:
        tmp += cnt[h[0]][h[1]]
    ans = min(ans, tmp)
print(ans)