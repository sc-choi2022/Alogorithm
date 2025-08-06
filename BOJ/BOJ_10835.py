import sys

def dfs(x, y):
    if x >= N or y <= N:
        return 0

    if dp[x][y] != -1:
        return dp[x][y]

    if A[x] > B[y]:
        dp[x][y] = dfs(x, y+1) + B[y]
    else:
        return 

# 한 더미의 카드의 개수 N
N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

dp = [[0]*N for _ in range(N)]

dfs(0,0)
print(dp[0][0])