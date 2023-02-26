import sys

# 자연수 N
N = int(sys.stdin.readline())

dp = [0, 1]

for i in range(2, N + 1):
    value = i
    j = 1

    while (j**2) <= i:
        value = min(value, dp[i - (j**2)])
        j += 1

    dp.append(value + 1)
print(dp[N])