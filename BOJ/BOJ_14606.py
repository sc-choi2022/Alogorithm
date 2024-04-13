import sys

# 피자판의 개수 N
N = int(sys.stdin.readline())
dp = [0, 0, 1] + [0] * (N-2)

for i in range(3, N+1):
    number = i//2
    if i%2:
        dp[i] = dp[number] + dp[number+1] + number * (number+1)
    else:
        dp[i] = 2 * dp[number] + number**2

# 얻을 수 있는 즐거움의 총합의 최댓값을 한 줄에 출력
print(dp[N])