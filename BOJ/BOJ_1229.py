import sys

# 정수 N
N = int(sys.stdin.readline())
dp = [0] * (N+1)

for i in range(2, 7072):
    dp[i] = dp[i-1] + 6*(i-1) - (2*(i-2)+1)

print(dp[N])