import sys

# 범위의 정수 N, 개수의 정수 K
N, K = map(int, sys.stdin.readline().split())
dp = [[0] * (N + 1) for _ in range(K + 1)]
dp[1] = [1] * (N + 1)

for i in range(2, K + 1):
    dp[i][0] = 1
    for j in range(1, N + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

# 0부터 N까지의 정수 K개를 더해 합이 N이 되는 경우의 수를 출력
print(dp[K][N])