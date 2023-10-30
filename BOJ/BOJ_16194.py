import sys

# 카드의 개수 N
N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))
dp = [1000001] * (N+1)
dp[0] = 0

for i in range(N+1):
    for j in range(i+1):
        dp[i] = min(dp[i], dp[i-j] + p[j])

print(dp[-1])