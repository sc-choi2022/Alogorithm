import sys

# 수열 A의 크기 N
N = int(sys.stdin.readline())

# 수열 A
A = list(map(int, sys.stdin.readline().split()))
# 다이나믹프로그래밍을 활용할 배열 dp
dp = [0] * N
dp = A[::]

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j] + A[i]:
            dp[i] = dp[j] + A[i]
print(max(dp))