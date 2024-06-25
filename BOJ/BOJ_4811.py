import sys

dp = [[0]*31 for _ in range(31)]

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break
    print(dp[N][0])