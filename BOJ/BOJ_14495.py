import sys

# 자연수 N
N = int(sys.stdin.readline())
dp = [0, 1, 1, 1] + [0]*(N-3)

for i in range(4, N+1):
    dp[i] = dp[i-1] + dp[i-3]
# N번째 피보나치 비스무리한 수를 출력
print(dp[N])