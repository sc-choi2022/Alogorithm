import sys

# 3XN 크기의 벽의 가로 길이 N
N = int(sys.stdin.readline())
# 경우수의 수를 저장하는 배열 dp
dp = [0, 0, 3] + [0] * (N-2)
# dp[2]값을 3으로 초기화
dp[2] = 3

# 점화식에 따른 for문
# 점화식 dp[N] = dp[N-2]*3 + 2*sum(dp[:N-4]) + 2
for i in range(4,N+1, 2):
    dp[i] += 3*dp[i-2] + 2*sum(dp[:i-4+1]) + 2
# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 출력
print(dp[N])