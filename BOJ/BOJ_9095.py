# 테스트케이스 T
T = int(input())
dp = [0]*11
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(T):
    # 정수 N
    N = int(input())
    print(dp[N])