import sys

# NxM의 배열의 길이 N, M
N, M = map(int, sys.stdin.readline().split())
# NxM의 배열 graph
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
# 정사각형의 최대 모서리 길이를 저장하는 배열 dp
dp = [[0]*M for _ in range(N)]

# 가장 큰 정사각형의 한변의 길이 answer
answer = 0
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            dp[i][j] = graph[i][j]
        elif not graph[i][j]:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        answer = max(answer, dp[i][j])
# 가장 큰 정사각형의 넓이를 출력
print(answer*answer)