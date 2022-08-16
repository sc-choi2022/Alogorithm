# 카드의 개수 N
N = int(input())
# 카드 담을 리스트 p
p = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], p[j]+dp[i-j])
# 금액의 최댓값을 출력
print(dp[N])