import sys

# 자연수 N
N = int(sys.stdin.readline())
dp = [x for x in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, i):
        if j**2 > i:
            break
        if dp[i] > dp[i - j**2] + 1:
            dp[i] = dp[i - j**2] + 1
# 제곱수 항의 최소 개수를 출력
print(dp[N])