from collections import deque
import sys

# 미로의 크기 N
N = int(sys.stdin.readline())
# 미로 maze
maze = list(map(int, sys.stdin.readline().split()))
dp = [N+1] * N
dp[0] = 0

for i in range(N):
    for j in range(i, maze[i]+1):
        if i + j >= N:
            break
        dp[i+j] = min(dp[i+j], dp[i]+1)
print(dp[N-1] if dp[N-1] != N+1 else -1)