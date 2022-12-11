import sys

# 수의 길이 N
N = int(sys.stdin.readline())

dp = [1] * 10

for i in range(1, N):
    for j in range(1, 10):
        dp[j] += dp[j-1]

# 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력
print(sum(dp)%10007)