import sys

# 자연수 N
N = int(sys.stdin.readline())
# 활용할 배열 dp
dp = [0] * (N+1)
dp[1] = 1

for i in range(2, N+1):
    cnt = 1e9
    j = 1
    while j**2 <= i:
        cnt = min(cnt, dp[i-(j**2)])
        j += 1
    dp[i] = cnt + 1

# 합이 n과 같게 되는 제곱수들의 최소 개수 출력
print(dp[N])