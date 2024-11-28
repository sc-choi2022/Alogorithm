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

    for i in range(1, 4):
        if current + i < N:
            if not dp[current+i]:
                if i == 3 and not flag and energy+K < dp[current+i]:
                    dp[current+i] = energy+K
                    queue.append((current+i, energy+K, True))
                elif not dp[current+i] or energy+stones[current][i-1] < dp[current+i]:
                    dp[current + i] = energy + stones[current][i-1]
                    queue.append((current+i, energy+stones[current][i-1], flag))
print(dp[N-1])