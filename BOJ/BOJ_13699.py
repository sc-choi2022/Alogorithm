import sys

# 수열의 매개변수 N
N = int(sys.stdin.readline())
# 수열 t(n)을 저장하는 배열 dp
dp = [1] + [0]*N

for i in range(1, N+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-j-1]
# t(n) 출력
print(dp[N])