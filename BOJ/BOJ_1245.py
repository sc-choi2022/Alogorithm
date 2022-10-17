import sys

def dfs(a, b):
    global check

    visited[a][b] = True

    for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1):
        x, y = a + di, b + dj

        if -1 < x < N and -1 < y < M:
            if farm[a][b] < farm[x][y]:
                check = False
            if not visited[x][y] and farm[x][y] == farm[a][b]:
                dfs(x, y)

N, M = map(int, input().split())
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if farm[i][j] > 0 and not visited[i][j]:
            check = True
            dfs(i, j)

            if check:
                cnt += 1
print(cnt)