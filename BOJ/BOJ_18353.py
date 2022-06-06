# 병사의 수 N
N = int(input())
# N명의 전투력을 담은 리스트 power
power = list(map(int, input().split()))

# DP 테이블 초기화
dp = [1] * N

# 다이나믹 프로그래밍 진행
for i in range(N):
    for j in range(i):
        if power[i] < power[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

# 열외해야 하는 병사의 수 출력
print(N - max(dp))