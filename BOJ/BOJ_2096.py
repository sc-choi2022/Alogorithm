from collections import deque
import sys
from pprint import pprint

def bfs(si, sj):
    queue = deque([(si, sj)])

    while queue:
        ci, cj = queue.popleft()
        maxNum, minNum = dp[ci][0], dp[ci][1]

        for di, dj in (1, 0), (1, -1), (1, 1):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < 3:
                num = lines[ni][nj]
                if maxNum + num > dp[ni][0]:
                    dp[ni][0] = maxNum + num
                    queue.append((ni, nj))
                elif minNum + num < dp[ni][1]:
                    dp[ni][1] = minNum + num
                    queue.append((ni, nj))

# 줄의 개수 N
N = int(sys.stdin.readline())

# 숫자를 담은 줄 lines
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 다이나믹프로그래밍을 활용할 배열 dp
# dp = [[[lines[0][0], lines[0][0]], [lines[0][1], lines[0][1]], [lines[0][2], lines[0][2]]]] + [[[0, int(1e9)]] * 3 for _ in range(N - 1)]
dp = [[max(lines[0]), min(lines[1])]] + [[0, int(1e9)]] * (N-1)

# for i in range(N):
for j in range(3):
    bfs(0, j)
pprint(dp)
# print(*dp[N-1][0])