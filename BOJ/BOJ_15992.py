import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

dp = [[0]*1001 for _ in range(1001)]
dp[1][1], dp[2][1], dp[3][1] = 1, 1, 1

for i in range(2, 1001):
    for j in range(1, 1001):
        for k in range(1, 4):
            if j-k > 0:
                dp[j][i] += dp[j-k][i-1]
        dp[j][i] %= 1000000009

for _ in range(T):
    # 정수 N, M
    N, M = map(int, sys.stdin.readline().split())
    # N을 1, 2, 3의 합으로 나타내는 방법의 수를 1000000009로 나눈 나머지를 출력
    print(dp[N][M])