# 포도잔의 개수 N
N = int(input())
wine = [int(input()) for _ in range(N)]
dp = [0]

if N > 1:
    dp.append(wine[1]+wine[2])

for i in range(3, N+1):
    dp.append(max(dp[i-1], dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i]))

print(dp[N])