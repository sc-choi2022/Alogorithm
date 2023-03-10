import sys

def dfs(si, sj):
    if si == M-1 and sj == N-1:
        return 1
    if dp[si][sj] == -1:
        dp[si][sj] = 0
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = si + di, sj + dj
            if 0 <= ni < M and 0 <= nj < N and zido[si][sj] > zido[ni][nj]:
                dp[si][sj] += dfs(ni, nj)
    return dp[si][sj]

# 지도의 세로의 크기 M과 가로의 크기 N
M, N = map(int, sys.stdin.readline().split())
# 지도의 숫자를 담을 배열 zido
zido = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
# 각 위치에서 가능한 경로의 수를 담을 배열 dp
dp = [[-1]*N for _ in range(M)]

print(dfs(0, 0))