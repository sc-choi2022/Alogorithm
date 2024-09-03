import sys

# 합 N, 정수의 개수 K
N, K = map(int, sys.stdin.readline().split())
# dp[i][j] i를 만드는데 j개의 정수를 사용하는 경우의 수를 저장하는 배열 dp
dp = [[0]*(K+1) for _ in range(N+1)]
dp[0] = [1]*(K+1)

for i in range(1, N+1):
    for j in range(1, K+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000

# 답을 1,000,000,000으로 나눈 나머지를 출력
print(dp[N][K])