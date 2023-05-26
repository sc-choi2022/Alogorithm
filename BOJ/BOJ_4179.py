from collections import deque
import sys

def location():
    global si, sj
    for li in range(R):
        for lj in range(C):
            if zido[li][lj] == 'J':
                si, sj = li, lj
                visit[li][lj] = 0
            elif zido[li][lj] == 'F':
                fire.append((li, lj))
                visit[li][lj] = -2

def bfs():
    fire.append((si, sj))
    queue = deque(fire)

    while queue:
        ci, cj = queue.popleft()
        mark = visit[ci][cj]

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < R and 0 <= nj < C:
                if visit[ni][nj] == -1 and zido[ni][nj] in ('.', 'J'):
                    # 불이 번지는 경우
                    if mark == -2:
                        visit[ni][nj] = -2
                    else:
                        visit[ni][nj] = visit[ci][cj] + 1
                    queue.append((ni, nj))
            else:
                if mark != -2:
                    return visit[ci][cj] + 1

    return 'IMPOSSIBLE'

# 빌딩 지도의 너비 W와 높이 H
R, C = map(int, sys.stdin.readline().split())
# 빌딩 지도의 정보를 담은 배열 zido
zido = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
# queue에 중복값을 저장하지 않도록 하기 위한 배열 visit
visit = [[-1]*C for _ in range(R)]
# 지훈이의 시작 위치 si, sj
si, sj = 0, 0
# 불의 위치를 저장하는 배열 fire
fire = []
# 시작 위치와 불의 위치를 저장하는 함수 location
location()
# 시간에 따른 이동을 확인하고 탈출여부 확인하는 함수 bfs
print(bfs())