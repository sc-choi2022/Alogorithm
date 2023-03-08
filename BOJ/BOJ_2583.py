from pprint import pprint
from collections import deque
import sys

def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == 0:
                queue.append((ni, nj))
                grid[ni][nj] == -1

# M×N 모눈종이, 직사각형의 개수 K
M, N, K = map(int, sys.stdin.readline().split())

# 모눈종이 grid
grid = [[0]*N for _ in range(M)]

# 영역의 개수 ans
ans = 0

for _ in range(K):
    i2, j1, i1, j2 = map(int, sys.stdin.readline().split())
    i2, i1 = M - i2 - 1, M -i1 - 1
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            grid[i][j] += 1
print(grid)

for ii in range(M):
    for jj in range(N):
        if grid[ii][jj] == 0:
            grid[ii][jj] = -1
            bfs(ii, jj)
            ans += 1

print(ans)