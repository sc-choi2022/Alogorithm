import sys

while True:
    # 일수 N
    N = int(sys.stdin.readline())
    if N == 0:
        break
    earn = [int(sys.stdin.readline()) for _ in range(N)]
    dp = [0] * N
    dp[0] = earn[0]

    for i in range(1, N):
        dp[i] = max(dp[i-1] + earn[i], earn[i])

    # 가장 많은 수익을 올린 구간의 수익을 출력
    print(max(dp))