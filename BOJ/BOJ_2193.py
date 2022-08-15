# 이친수의 자리수 N
N = int(input())

# 이친수를 담을 리스트 dp
dp = [0] * (N+1)
# N이 1인 경우
if N == 1:
    dp[1] = 1
# N이 1 이상인 경우
else:
    # dp[1], dp[2]을 1로 저장
    dp[1], dp[2] = 1, 1
    # 3부터는 규칙에 따라 dp[i]에 계산 후 저장
    for i in range(3, N+1):
        dp[i] = dp[i-2] + dp[i-1]
# N자리 이친수의 개수를 출력
print(dp[N])