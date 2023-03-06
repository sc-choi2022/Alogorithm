import sys

# Greedy
# 거스름돈 액수 N
N = int(sys.stdin.readline())

five = N // 5
two = (N % 5) // 2

if (N % 5) % 2:
    five -= 1
    two += 3

print(-1 if five == -1 else five + two)

# DP
dp = [100000, 100000, 1, 100000, 2, 1] + [100000] * (N - 5)

for i in range(6, N + 1):
    # i의 거스름돈 동전의 최소 개수를 갱신
    dp[i] = min(dp[i-2], dp[i-5]) + 1

# dp[N]가 100000인 경우 -1 출력 아닌 경우 dp[N] 출력
print(-1 if dp[N] == 100000 else dp[N])