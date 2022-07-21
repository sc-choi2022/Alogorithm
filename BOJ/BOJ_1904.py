import sys

# 2진 수열의 개수를 15746로 나눈 나머지를 dp 리스트에 담고 bi[N]을 return하는 함수 bi
def bi(N):
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2])%15746
    return dp[N]

# 자연수 N
N = int(sys.stdin.readline())
# 2진 수열의 개수를 15746로 나눈 나머지을 담는 리스트 dp
dp = [0] * 1000001
# 인덱스 1, 2에 1, 2을 할당
dp[1], dp[2] = 1, 2
# bi(N) 출력
print(bi(N))