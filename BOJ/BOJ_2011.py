import sys

# 암호 숫자 N
N = list(map(int, sys.stdin.readline().rstrip()))
L = len(N)
dp = [0] * (L + 1)

if N[0] == 0:
    print('0')
else:
    N = [0] + N
    dp[0], dp[1] = 1, 1
    for i in range(2, L + 1):
        if N[i]:
            dp[i] += dp[i-1]
        tmp = 10 * N[i-1] + N[i]
        if tmp >= 10 and tmp <= 26:
            dp[i] += dp[i-2]
    print(dp[L] % 1000000)