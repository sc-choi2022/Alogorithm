import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    if i == N or j == N:
        return 0

    if dp[i][j] >= 0:
        return dp[i][j]

    if A[i] > B[j]:
        dp[i][j] = dfs(i, j+1) + B[j]
    else:
        s1, s2 = dfs(i+1, j), dfs(i+1, j+1)
        if s1 >= s2:
            dp[i][j] = s1
        else:
            dp[i][j] = s2
    return dp[i][j]

# 한 더미의 카드의 개수 N
N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

dp = [[-1]*N for _ in range(N)]

print(dfs(0, 0))