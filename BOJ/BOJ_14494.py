import sys

# 도달해야하는 위 N, M
N, M = map(int, sys.stdin.readline().split())
# 해당 위치에 도달하는 경우의 수를 저장하는 배열 dp
dp = [[0]*M for _ in range(N)]

for i in range(N):
    dp[i][0] = 1
for j in range(1, M):
    dp[0][j] = 1

for ii in range(1, N):
    for jj in range(1, M):
        dp[ii][jj] = (dp[ii-1][jj-1] + dp[ii-1][jj] + dp[ii][jj-1])%1000000007
# 경우의 수를 1,000,000,007(=109+7)로 나눈 나머지를 출력
print(dp[N-1][M-1])