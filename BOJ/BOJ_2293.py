import sys

# 동전의 수 N, 목표 합 K
N, K = map(int, sys.stdin.readline().split())
# 동전의 가치를 담을 리스트 coins
coins = [int(sys.stdin.readline()) for _ in range(N)]
# 합이 index가 되는 경우의 수를 담는 dp
dp = [0]*(K+1)
# 이중 for문의 coin-i이 0일 때 1개를 추가하기 위해 1로 값 초기화
dp[0] = 1

# coins의 모든 coin에 대해
for coin in coins:
    # coin 1개로 만들 수 있는 값부터 K까지
    for i in range(coin, K+1):
        # i-coin>=0인 경우, i-coin을 만드는 경우의 수를 dp[i]에 더해주어
        # 현재 coin을 사용한 경우까지 dp[i]에 갱신
        if i-coin >= 0:
            dp[i] += dp[i-coin]
# K가 되는 경우의 수 출력
print(dp[K])