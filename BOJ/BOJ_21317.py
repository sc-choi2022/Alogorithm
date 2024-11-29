from collections import deque
import sys

# 돌의 개수 N
N = int(sys.stdin.readline())
stones = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
dp = [0] * N

K = int(sys.stdin.readline())

queue = deque([(0, 0, 0)])

while queue:
    current, energy, flag = queue.popleft()

print(dp[N-1])