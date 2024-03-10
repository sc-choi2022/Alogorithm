from collections import deque
import sys

# 성의 크기 N, M, 제한시간 T
N, M, T = map(int, sys.stdin.readline().split())
# 성의 구조를 저장하는 배열 castle
castle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 방문여부를 저장하는 배열 visit
visit = [[10000]*M for _ in range(N)]
# 그람을 찾았는지 여부를 저장하는 변수 flag
flag = False

queue = deque([(0, 0)])
visit[0][0] = 0

while queue:
    ci, cj = queue.popleft()

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 10000:
            # 그람을 발견한 경우
            if castle[ni][nj] == 2:
                flag = True
                queue.append((ni, nj))
                visit[ni][nj] = visit[ci][cj] + 1
            # 빈 공간인 경우
            elif castle[ni][nj] == 0:
                queue.append((ni, nj))
                visit[ni][nj] = visit[ci][cj] + 1
            else:
                # 벽이지만 그람을 발견한 경우
                if flag:
                    queue.append((ni, nj))
                    visit[ni][nj] = visit[ci][cj] + 1

# T시간 이내에 공주에게 도달할 수 있는 최단 시간 출력
if visit[N-1][M-1] <= T:
    print(visit[N-1][M-1])
# T시간 이내에 구출할 수 없는 경우 Fail 출력
else:
    print('Fail')