import sys

# 세로길이 N, 가로길이 M
N, M = map(int, sys.stdin.readline().split())
# 자원의 정보를 저장하는 배열 resources
resources = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dp[0][0] = resources[0][0]

for i in range(N):
    for j in range(M):
        if (i, j) == (0, 0):
            continue
        elif i and j == 0:
            dp[i][j] = dp[i-1][j] + resources[i][j]
        elif i == 0 and j:
            dp[i][j] = dp[i][j-1] + resources[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + resources[i][j]

# WOOK이 수집할 수 있는 최대 광석의 개수를 출력
print(dp[N-1][M-1])