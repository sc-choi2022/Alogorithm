import sys

# 행의 수 N, 열의 수 M, O표시가 된 수 K
N, M, K = map(int, sys.stdin.readline().split())
# 확인을 위한 배열 dp
dp = [[0]*M for _ in range(N)]

if K:
    ci, cj = K//M, K%M-1
    dp[0] = [1] * M
    for i in range(1, ci+1):
        for j in range(cj+1):
            if j == 0:
                dp[i][j] = 1
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    for ii in range(ci, N):
        for jj in range(cj, M):
            if (ii, jj) == (ci, cj):
                continue
            elif ii == ci:
                dp[ii][jj] = dp[ci][cj]
            elif jj == cj:
                dp[ii][jj] = dp[ci][cj]
            else:
                dp[ii][jj] = dp[ii-1][jj] + dp[ii][jj-1]
else:
    dp[0] = [1] * M
    for i in range(1, N):
        for j in range(M):
            if j == 0:
                dp[i][j] = 1
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[N-1][M-1])