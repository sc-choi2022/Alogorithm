from collections import deque
import sys

# 미로의 크기 N
N = int(sys.stdin.readline())
# 미로 maze
maze = list(map(int, sys.stdin.readline().split()))

# BFS
visit = [-1] * N
visit[0] = 0

queue = deque([0])
while queue:
    current = queue.popleft()
    if current == N-1:
        break
    for i in range(1, maze[current]+1):
        if current + i < N and visit[current + i] == -1:
            queue.append(current+i)
            visit[current+i] = visit[current] + 1
# 최소 몇 번 점프를 해야 가장 오른쪽 끝 칸으로 갈 수 있는지 출력
# 만약, 가장 오른쪽 끝으로 갈 수 없는 경우에는 -1을 출력
print(visit[N-1] if visit[N-1] != -1 else -1)

# DP
dp = [N+1] * N
dp[0] = 0

for i in range(N):
    for j in range(1, maze[i]+1):
        if i+j >= N:
            break
        dp[i+j] = min(dp[i+j], dp[i] + 1)
print(dp[N-1] if dp[N-1] != N+1 else -1)