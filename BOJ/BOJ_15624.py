import sys

# N번째 피보나치 수
N = int(sys.stdin.readline())
dp = [0, 1] + [0] * (N-1)

for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%1000000007
# N번째 피보나치 수 출력
print(dp[N])