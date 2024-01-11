import sys

# 사람의 수 N
N = int(sys.stdin.readline())
# 필요한 체력을 저장하는 배열 L
L = [0] + list(map(int, sys.stdin.readline().split()))
# 얻는 기쁨의 크기를 저장하는 배열 J
J = [0] + list(map(int, sys.stdin.readline().split()))
# 행은 i번째 손님
# 열은 체력이 j일 때 가능한 최대 기쁨을 저장하는 배열 dp
dp = [[0]*101 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 101):
        if L[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
        else:
            dp[i][j] = dp[i-1][j]
# 얻을 수 있는 최대 기쁨을 출력
print(dp[N][99])