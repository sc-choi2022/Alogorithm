# 동전의 수 N, 목표 합 K
N, K = map(int, input().split())
# 동전의 가치를 담을 리스트 coins
coins = [int(input()) for _ in range(N)]
# 합이 index가 되는 경우의 수를 담는 dp
dp = [100001]*(K+1)
# 1가 되는 경우의 수를 위해 index 0에 1 저장
dp[0] = 0

for coin in coins:
    for j in range(coin, K+1):
        if j-coin >= 0:
            dp[j] = min(dp[j-coin]+1, dp[j])
if dp[K] != 100001:
    print(dp[K])
else:
    print(-1)