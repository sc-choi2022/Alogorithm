import sys

# 행의 수 N, 열의 수 M, O표시가 된 수 K
N, M, K = map(int, sys.stdin.readline().split())
# 확인을 위한 배열 dp
dp = [[0]*M for _ in range(N)]
# 출력하는 결과 answer
answer = 1
# K가 존재할 경우
if K:
    ci, cj = (K-1)//M, (K-1)%M
    for i in range(ci+1):
        for j in range(cj+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    answer *= dp[ci][cj]
    for ii in range(ci, N):
        for jj in range(cj, M):
            if ii==ci or jj==cj:
                dp[ii][jj] = 1
            else:
                dp[ii][jj] = dp[ii][jj-1] + dp[ii-1][jj]
# K가 존재하지 않을 경우
else:
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
# 서로 다른 경로의 수를 계산하여 출력
print(answer*dp[N-1][M-1])