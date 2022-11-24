from copy import deepcopy
import sys

def dfs(i, j, color, greed):
    stack = [(i, j)]

    while stack:
        ci, cj = stack.pop()

        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and greed[ni][nj] == color:
                stack.append((ni, nj))
                greed[ni][nj] = 0

# 그리드의 한 길이 N
N = int(sys.stdin.readline())

grd = [list(sys.stdin.readline().strip()) for _ in range(N)]

clcblind = deepcopy(grd)

ans1 = 0
for i in range(N):
    for j in range(N):
        now = grd[i][j]
        if now != 0:
            grd[i][j] = 0
            dfs(i, j, now, grd)
            ans1 += 1

ans2 = 0
for ii in range(N):
    for jj in range(N):
        if clcblind[ii][jj] == 'G':
            clcblind[ii][jj] = 'R'

for iii in range(N):
    for jjj in range(N):
        now1 = clcblind[iii][jjj]
        if now1 != 0:
            clcblind[iii][jjj] = 0
            dfs(iii, jjj, now1, clcblind)
            ans2 += 1

print(ans1, ans2)