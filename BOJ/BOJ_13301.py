import sys

# 타일의 개수 N
N = int(sys.stdin.readline())
# 타일의 개수에 따른 직사각형의 둘레를 저장하는 배열 dp
dp = [4, 6] + [0] * 79

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

# N 개의 타일이 구성하는 타일 장식물 직사각형의 둘레를 출력
print(dp[N-1])