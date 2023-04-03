from collections import deque
import sys

def bfs(si, sj):
    global answer
    queue = deque([(si, sj)])
    visit = [[-1] * M for _ in range(N)]
    visit[si][sj] = 0

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and zido[ni][nj] == 'L' and visit[ni][nj] == -1:
                queue.append((ni, nj))
                visit[ni][nj] = visit[ci][cj] + 1
                answer = max(answer, visit[ni][nj])

# 보물 지도의 세로의 크기와 가로의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 지도 배열 zido
zido = [[] for _ in range(N)]
# 육지의 위치를 저장하는 배열 land
land = []

for i in range(N):
    zido[i] = list(sys.stdin.readline().rstrip())
    for j in range(M):
        if zido[i][j] == 'L':
            land.append((i, j))
# 최단 시간을 저장할 변수 answer
answer = 0

# bfs함수에 모든 육지를 확인
for si, sj in land:
    bfs(si, sj)

# 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력
print(answer)