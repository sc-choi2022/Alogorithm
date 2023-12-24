import sys

def dfs(ci, cj, d, add):
    global answer

    if ci == N-1:
        answer = min(answer, add)
        return

    if add > answer:
        return

    for l in range(3):
        di, dj = direct[l]
        ni, nj = ci + di, cj + dj
        if l == d:
            continue
        if 0 <= ni < N and 0 <= nj < M:
            dfs(ni, nj, l, add+place[ni][nj])

# 행렬의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
place = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = float('INF')
direct = {0:(1, -1), 1:(1, 0), 2:(1, 1)}

for i in range(1):
    for j in range(M):
        for k in range(3):
            di, dj = direct[k]
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                dfs(ni, nj, k, place[i][j]+place[ni][nj])
print(answer)