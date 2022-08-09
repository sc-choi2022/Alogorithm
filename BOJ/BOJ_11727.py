import sys
# 주어지는 자연수 N
N = int(sys.stdin.readline())
# N에 따른 직사각형을 채우는 방법 수를 담는 리스트 dp
dp = [0]*1001
# dp[1], dp[2] 값을 1, 3로 저장한다.
dp[1], dp[2] = 1, 3
# 점화식에 따라 계산 후 dp[i]에 저장
for i in range(3, N+1):
    dp[i] = 2*dp[i-2] + dp[i-1]
# 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력
print(dp[N]%10007)