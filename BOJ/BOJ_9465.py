import sys

# 테스트 케이스 개수
T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    dp = [[0]+list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    for j in range(2, n+1):
        dp[0][j] += max(dp[1][j-1], dp[1][j-2])
        dp[1][j] += max(dp[0][j-1], dp[0][j-2])
    print(max(dp[0][n], dp[1][n]))