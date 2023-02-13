import sys

# 미로의 크기 NxM
N, M = map(int, sys.stdin.readline().split())

# 미로의 내용을 담을 배열 maze
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 각 위치까지 사탕의 최대개수를 저장할 배열 dp
dp = [[0] * (M + 1)] * (N + 1)

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + maze[i - 1][j - 1]
# (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수를 출력
print(dp[N][M])