import sys

# 표의 크기 N, 합을 구해야하는 횟수 M
N, M = map(int, sys.stdin.readline().split())
# NxN 표 chart
chart = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# (1,1)부터 (x1, y1)까지의 표에 채워져 있는 수의 합을 dp[x1][y1]에 담을 배열 dp
dp = [[0]*(N+1) for _ in range(N+1)]

# dp에 (1,1)부터 (x1, y1)까지의 표에 채워져 있는 수의 합을 dp[x1][y1]에 저장
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] -dp[i-1][j-1] + chart[i-1][j-1]

#
for _ in range(M):
    # 합을 구해 출력할 좌표 (x1, y1)와 (x2, y2)
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    # (x1, y1)부터 (x2, y2)까지 합을 출력
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])