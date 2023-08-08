import sys

# N번째 피보나치 수 N
N = int(sys.stdin.readline())
# 피보나치 수열을 저장하는 배열 dp
dp = [0, 1] + [0]*(N-1)

for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1]
# N번째 피보나치 수를 출력
print(dp[N])