import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 동전의 가지수 N
    N = int(sys.stdin.readline())
    # 동전의 각 금액 coins
    coins = list(map(int, sys.stdin.readline().split()))
    # N가지 동전으로 만들어야 할 금액 M
    M = int(sys.stdin.readline())

    # index 금액을 만들 수 있는 가지수의 수를 저장할 배열 dp
    dp = [0] * (M+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, M + 1):
            dp[i] += dp[i-coin]
    # N가지 동전으로 금액 M을 만드는 모든 방법의 수를 출력
    print(dp[M])