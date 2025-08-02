import sys

# 한 더미의 카드의 개수 N
N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

dp = [0] * N

for i in range(N):
    for j in range(N):
        if A[i] < B[j]:
            dp[i][j] += B[j]
        else:
            