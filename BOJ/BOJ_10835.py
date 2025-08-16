import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    return 

# 한 더미의 카드의 개수 N
N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

dp = [[-1]*N for _ in range(N)]

dfs(0, 0)
print(dp[0][0])