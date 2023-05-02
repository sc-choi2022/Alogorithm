from collections import deque
from copy import deepcopy
import sys

def virus(cnt):
    if cnt == M:
        bfs()
        return

    for i in range(N):
        for j in range(N):
            if not zido[i][j]:
                zido[i][j] = 2
                virus(cnt+1)
                zido[i][j] = 0

def bfs():
    global answer
    tmp = deepcopy(zido)
    queue = deque([])
    for ii in range(N):
        for jj in range(N):
            if zido[ii][jj] == 2:
                queue.append((ii, jj))

    while queue:
        ci, cj = queue.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not tmp[ni][nj]:
                tmp[ni][nj] = tmp[ci][cj] + 1
                queue.append((ni, nj))
    check(tmp)

def check(lst):
    global answer
    maxTime = 0
    for iii in range(N):
        for jjj in range(N):
            if not lst[iii][jjj]:
                return
            maxTime = max(maxTime, lst[iii][jjj])
    answer = min(answer, maxTime)

# 연구소의 크기 N, 놓을 수 있는 바이러스 개수 M
N, M = map(int, sys.stdin.readline().split())

zido = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 1e9
virus(0)
print(answer)