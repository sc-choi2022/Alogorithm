import sys

dp = [[0]*31 for _ in range(31)]

for j in range(31):
    dp[0][j] = 1

for di in range(1, 31):
    for dj in range(i, 31):
        continue

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break
    print(dp[N][0])