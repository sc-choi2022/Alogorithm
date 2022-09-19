import sys

# 동전의 수 N, 목표 합 K
N, K = map(int, sys.stdin.readline().split())
# 동전의 가치를 담을 리스트 coins
coins = [int(sys.stdin.readline()) for _ in range(N)]
# index가 되는 최소 동전의 개수를 담을 리스트 dp, 모든 값을 100001으로 초기화
dp = [100001]*(K+1)
# 이중 for문의 coin-i이 0인 경우를 위해 0로 값 초기화
dp[0] = 0

# coins의 모든 coin에 대해
for coin in coins:
    # coin 1개로 만들 수 있는 값부터 K까지
    for i in range(coin, K+1):
        # i-coin>=0인 경우, 
        # i-coin을 만드는 경우의 수인 dp[i-coin]+1과 기존 dp[i]값 중 작은 값을 dp[i]에 저장
        # dp[i-coin]+1은 coin한개와 나머지 i-coin을 만드는 최소 경우의 수를 더한 것을 의미
        if i-coin >= 0:
            dp[i] = min(dp[i-coin]+1, dp[i])
# dp[K]값이 갱신되지 않은 경우 -1 출력
if dp[K] == 100001:
    print(-1)
# dp[K]값이 갱신되었다면 dp[K]을 출력
else:
    print(dp[K])