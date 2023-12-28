import sys

# 숫자의 개수 N
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [[0]*21 for _ in range(N-1)]
dp[0][numbers[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if 0 <= j - numbers[i]:
            dp[i][j-numbers[i]] += dp[i-1][j]
        if j + numbers[i] <= 20:
            dp[i][j+numbers[i]] += dp[i-1][j]

print(dp[-1][numbers[-1]])