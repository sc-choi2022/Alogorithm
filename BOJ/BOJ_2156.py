# 포도잔의 개수 N
N = int(input())
# 포도주 양을 담을 리스트 wine
wine = [int(input()) for _ in range(N)]

# 포도잔이 하나인 경우
if N == 1:
    print(wine[0])
# 포도잔이 두잔이상인 경우
else:
    # 최대 포도주양을 담을 리스트 dp
    dp = [0] * N
    # dp[0], dp[1] 값을 저장
    dp[0], dp[1] = wine[0], wine[0] + wine[1]
    # 3잔부터의 최대양을 연속 3잔이 아닌 경우 중 가장 큰 값을 저장한다.
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])
    # dp[N-1]을 출력
    print(dp[N-1])