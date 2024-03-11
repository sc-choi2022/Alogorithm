from collections import deque
import sys

# 성의 크기 N, M, 제한시간 T
N, M, T = map(int, sys.stdin.readline().split())
# 성의 구조를 저장하는 배열 castle
castle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 방문여부를 저장하는 배열 visit
visit = [[10001]*M for _ in range(N)]

queue = deque([(0, 0)])
visit[0][0] = 0
# 그람의 위치 (gi, gj)
gi, gj = -1, -1

while queue:
    ci, cj = queue.popleft()

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 10001:
            if castle[ni][nj] == 1:
                continue
            elif castle[ni][nj] == 2:
                gi, gj = ni, nj
            queue.append((ni, nj))
            visit[ni][nj] = visit[ci][cj] + 1

# 그람을 찾지 못한 경우
if (gi, gj) == (-1, -1):
    answer = visit[N-1][M-1]
else:
    answer = min(visit[N-1][M-1], visit[gi][gj]+abs(N-1-gi)+abs(M-1-gj))
# T시간 이내에 공주에게 도달할 수 있는 최단 시간 출력
if answer <= T:
    print(answer)
# T시간 이내에 구출할 수 없는 경우 Fail 출력
else:
    print('Fail')