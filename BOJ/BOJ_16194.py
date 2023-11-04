import sys

# 민규가 구매하려는 카드의 개수 N
N = int(sys.stdin.readline())
# 카드팩의 가격 P
P = [0] + list(map(int, sys.stdin.readline().split()))
# i개의 카드를 구매했을 때 최솟값을 저장하는 배열 dp
dp = [10000001] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    for j in range(i+1):
        dp[i] = min(dp[i], dp[i-j] + P[j])
# 카드 N개를 갖기 위해 지불해야 하는 금액의 최솟값을 출력
print(dp[-1])