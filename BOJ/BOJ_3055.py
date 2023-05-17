from collections import deque
import sys

def bfs():
    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if not 0 <= ni < R and not 0 <= nj < C:
                continue
            elif visit[ni][nj] != -1:
                continue
            elif zido[ni][nj] == '*' or zido[ni][nj] == 'X':
                continue
            elif zido[ni][nj] == 'D' and zido[ci][cj] == '*':
                continue
            elif zido[ni][nj] == 'D' and zido[ci][cj] == 'S':
                return visit[ci][cj] + 1

            queue.append((ni, nj))
            visit[ni][nj] = visit[ci][cj] + 1
            zido[ni][nj] = zido[ci][cj]

    return 'KAKTUS'

# R행 C열
R, C = map(int, sys.stdin.readline().split())
# 티떱숲의 지도 배열 zido
zido = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visit = [[-1]*C for _ in range(R)]
queue = deque([])

for fi in range(R):
    for fj in range(C):
        if zido[fi][fj] == 'S':
            queue.append((fi, fj))
            visit[fi][fj] = 0
        elif zido[fi][fj] == '*':
            queue.appendleft((fi, fj))
            visit[fi][fj] = 0
print(bfs())