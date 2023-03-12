import sys

def dfs(ci, cj, cnt):
    global answer
    answer = max(answer, cnt)
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < R and 0 <= nj < C and visit[ni][nj] == 0:
            visit[ni][nj] = 1
            dfs(ni, nj, cnt + 1)
            visit[ni][nj] = 0

R, C = map(int, sys.stdin.readline().split())
alphabet = [list(map(lambda x: ord(x)-65, sys.stdin.readline().rstrip())) for _ in range(R)]
visit = [[0] * C for _ in range(R)]

answer = 0
dfs(0, 0, 1)
print(answer)