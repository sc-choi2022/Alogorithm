import sys

# 판의 크기 N
N = int(sys.stdin.readline())
# NxN의 게임판 game
game = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break

        if i + game[i][j] < N:
            dp[i + game[i][j]][j] += dp[i][j]
        if j + game[i][j] < N:
            dp[i][j + game[i][j]] += dp[i][j]
