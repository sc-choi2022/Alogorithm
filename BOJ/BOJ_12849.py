import sys

# 산책하는 시간 D분
D = int(sys.stdin.readline())
# 배열 dp
dp = [0] * 8
dp[0] = 1

for _ in range(D):
    tmp = [0] * 8
    tmp[0] = (dp[1] + dp[2])%1000000007
    tmp[1] = (dp[0] + dp[2] + dp[3])%1000000007
    tmp[2] = (dp[0] + dp[1] + dp[3] + dp[4])%1000000007
    tmp[3] = (dp[1] + dp[2] + dp[4] + dp[5])%1000000007