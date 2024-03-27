import sys

# 테스트 케이스 T
T = 1

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    dp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dp[1][0] += dp[0][1]
    dp[1][1] += min(dp[1][0], dp[0][1], dp[0][1] + dp[0][2])
    dp[1][2] += min(dp[1][1], dp[0][1], dp[0][1] + dp[0][2])

    for i in range(2, N):
        dp[i][0] += min(dp[i-1][0], dp[i-1][1])
        dp[i][1] += min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0])
        dp[i][2] += min(dp[i-1][1], dp[i-1][2], dp[i][1])

    # 테스트 케이스 번호와 최소비용 출력
    print(f'{T}. {dp[N - 1][1]}')
    # 테스트 케이스 수 1 증가
    T += 1