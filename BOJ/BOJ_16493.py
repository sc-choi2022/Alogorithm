import sys

# 남은 기간 N과 챕터의 수 M
N, M = map(int, sys.stdin.readline().split())
# 책의 챕터당 읽는데 소요되는 일 수와 페이지 수를 저장하는 배열 chapters

chapters = [(0, 0)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
chapters.sort()
dp = [[0]*(N+1) for _ in range(M+1)]

for i in range(1, M+1):
    day, page = chapters[i]
    for j in range(1, N+1):
        if j >= day:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day]+page)
        else:
            dp[i][j] = dp[i-1][j]

# 읽을 수 있는 최대 페이지 수를 출력
print(dp[M][N])