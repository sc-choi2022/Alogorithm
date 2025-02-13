import sys

N = int(sys.stdin.readline())

dp = [0] * (N+1)

if N >= 2:
    for i in range(3, N+1):
        dp[i] = (dp[i-1]*3)%1000000009
print(dp[N])