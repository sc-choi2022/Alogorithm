from collections import deque
import sys

def location():
    global si, sj
    for li in range(H):
        for lj in range(W):
            if zido[li][lj] == '@':
                si, sj = li, lj
                visit[li][lj] = 0
            elif zido[li][lj] == '*':
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
            if 0 <= ni < H and 0 <= nj < W:
                if visit[ni][nj] == -1 and zido[ni][nj] in ('.', '@'):
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

# 테스트케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 빌딩 지도의 너비 W와 높이 H
    W, H = map(int, sys.stdin.readline().split())
    # 빌딩 지도의 정보를 담은 배열 zido
    zido = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
    # queue에 중복값을 저장하지 않도록 하기 위한 배열 visit
    visit = [[-1]*W for _ in range(H)]
    # 상근이의 시작 위치 si, sj
    si, sj = 0, 0
    # 불의 위치를 저장하는 배열 fire
    fire = []
    # 상근이의 위치와 불의 위치를 저장하는 함수 location
    location()
    # 시간에 따른 이동을 확인하고 탈출여부 확인하는 함수 bfs
    print(bfs())