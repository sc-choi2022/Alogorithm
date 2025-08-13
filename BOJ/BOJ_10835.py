import sys

def dfs(i, j):
    if i >= N or j <= N:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    # 오른쪽 버리기
    if A[i] > B[j]:
        dp[i][j] = dfs(i, j+1) + B[j]
    # 왼쪽 버리기
    else:
        left = dfs(i+1, j)
        right = dfs(i+1, j+1)
        dp[i][j] = max(left, right)

# 한 더미의 카드의 개수 N
N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

dp = [[-1]*N for _ in range(N)]

dfs(0, 0)
print(dp[0][0])