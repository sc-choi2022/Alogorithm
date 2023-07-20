import sys

# 수열의 매개변수 N
N = int(sys.stdin.readline())
dp = [0]*36
dp[0] = 1

for i in range(1, N+1):
    for j in range(i):
        dp[i] += dp[j]*dp[i-j-1]
# dp[N]을 출력
print(dp[N])