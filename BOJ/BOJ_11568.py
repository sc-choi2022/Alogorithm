import sys

# 카드의 개수 N
N = int(sys.stdin.readline())
# 카드의 정보를 저장하는 배열 cards
cards = list(map(int, sys.stdin.readline().split()))
# 각 카드까지 만들 수 있는 가장 긴 순증가의 길이
dp = [0] * N
dp[0] = 1

for i in range(1, N):
    tmp = 0
    for j in range(i):
        if cards[j] < cards[i]:
            tmp = max(tmp, dp[j])
    dp[i] = tmp + 1

# 제시할 수 있는 수열의 원소의 최대 개수를 출력
print(max(dp))