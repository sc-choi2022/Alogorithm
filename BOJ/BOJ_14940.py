from collections import deque
import sys

# 지도의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 정보를 저장하는 배열 zido
zido = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 출발점을 기준으로 최단거리를 저장하는 배열 visit
visit = [[-1]*M for _ in range(N)]
# 출발점 si, sj
si, sj = 0, 0

for i in range(N):
    for j in range(M):
        # 방문할 수 없는 경우
        if not zido[i][j]:
            visit[i][j] = 0
        # 출발위치인 경우
        elif zido[i][j] == 2:
            si, sj = i, j
            visit[i][j] = 0

queue = deque([(si, sj)])

while queue:
    ci, cj = queue.popleft()

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj

        if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == -1:
            # 갈 수 있는 땅 1
            if zido[ni][nj] == 1:
                visit[ni][nj] = visit[ci][cj] + 1
                queue.append((ni, nj))

# 각 지점에서 목표지점까지의 거리를 출력
for v in visit:
    print(*v)