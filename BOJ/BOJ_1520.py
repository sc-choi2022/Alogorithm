import sys
sys.setrecursionlimit(10**9)

def dfs(si, sj):
    # 목적지점에 도달한 경우
    if si == M-1 and sj == N-1:
        return 1

    if dp[si][sj] == -1:
        dp[si][sj] = 0
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = si + di, sj + dj
            # 내리막 길인 경우
            if 0 <= ni < M and 0 <= nj < N and zido[si][sj] > zido[ni][nj]:
                dp[si][sj] += dfs(ni, nj)
    return dp[si][sj]

# 세로의 크기 M, 가로의 크기 N
M, N = map(int, sys.stdin.readline().split())
# 지도의 높이를 저장하는 배열 zido
zido = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
# (i, j)위치에서 목표지점까지는 가는 경로의 수
dp = [[-1] * N for _ in range(M)]

# 이동 가능한 경로의 수 출력
print(dfs(0, 0))