import sys

# 금액 N
N = int(sys.stdin.readline())
# 합법적으로 낼 수 있는 동전의 개수를 저장하는 배열 dp
dp = [d for d in range(N+1)]

for i in range(2, N+1):
    for j in (2, 5, 7):
        if i-j >= 0:
            dp[i] = min(dp[i], dp[i-j]+1)
            
# 합법적으로 낼 수 있는 동전의 개수를 출력
print(dp[N])