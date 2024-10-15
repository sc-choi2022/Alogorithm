import sys

# 산책하는 시간 D분
D = int(sys.stdin.readline())
# 배열 dp
dp = [0] * 8
dp[0] = 1
# 나머지 출력을 위한 정수 N
N = 1000000007

for _ in range(D):
    tmp = [0] * 8
    tmp[0] = (dp[1] + dp[2]) % N
    tmp[1] = (dp[0] + dp[2] + dp[3]) % N
    tmp[2] = (dp[0] + dp[1] + dp[3] + dp[4]) % N
    tmp[3] = (dp[1] + dp[2] + dp[4] + dp[5]) % N
    tmp[4] = (dp[2] + dp[3] + dp[5] + dp[6]) % N
    tmp[5] = (dp[3] + dp[4] + dp[7]) % N
    tmp[6] = (dp[4] + dp[7]) % N
    tmp[7] = (dp[5] + dp[6]) % N

    dp = tmp
    
# 가능한 경로의 수 출력
print(dp[0])