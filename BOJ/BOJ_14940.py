from collections import deque
import sys

def location():
    global si, sj

    for i in range(N):
        for j in range(M):
            if zido[i][j] == 2:
                si, sj = i, j
                return

# 지도의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
zido = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [[-1]*M for _ in range(N)]
si, sj = 0, 0

queue = deque([(si, sj)])
visit[si][sj] = 0

while queue:
    ci, cj = queue.popleft()

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj

        if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == -1:
            if zido[ni][nj] == 1:
                visit[ni][nj] = visit[ci][cj] + 1
                queue.append((ni, nj))
            elif zido[ni][nj] == 0:
                visit[ni][nj] = 0

for v in visit:
    print(*v)