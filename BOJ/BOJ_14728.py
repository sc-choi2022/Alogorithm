import sys

# 단원의 개수 N, 공부할 수 있는 총 시간 T
N, T = map(int, sys.stdin.readline().split())
# 예상 공부 시간 K, 문제의 배점 S을 저장하는 배열 study
study = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*T for _ in range(N)]

for i in range(N):
    for j in range(T):
        if j >= study[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-study[i][0]] + study[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N-1][T-1])