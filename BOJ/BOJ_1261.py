from collections import deque
import sys

# 가로 크기 M, 세로 크기 N
M, N = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# 위치까지 필요한 최소 벽을 깨는 횟수를 저장하는 배열 visit
visit = [[-1]*M for _ in range(N)]

queue = deque([(0, 0)])
visit[0][0] = 0

while queue:
    ci, cj = queue.popleft()

    for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < M:
            if visit[ni][nj] == -1:
                if maze[ni][nj] == '0':
                    visit[ni][nj] = visit[ci][cj]
                    queue.appendleft((ni, nj))
                else:
                    visit[ni][nj] = visit[ci][cj] + 1
                    queue.append((ni, nj))
# (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력
print(visit[N-1][M-1])