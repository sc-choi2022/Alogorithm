from collections import deque
from copy import deepcopy
import sys

def location():
    global si, sj
    for li in range(H):
        for lj in range(W):
            if zido[li][lj] == '@':
                si, sj = li, lj
                burn[li][lj] = '.'
            elif zido[li][lj] == '*':
                fire.append((li, lj))
                burn[li][lj] = 0

def flame():
    q = deque(fire)

    while q:
        ci, cj = q.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < H and 0 <= nj < W and burn[ni][nj] == '.':
                q.append((ni, nj))
                burn[ni][nj] = burn[ci][cj] + 1

def bfs(si, sj):
    queue = deque([(si, sj)])
    zido[si][sj] = 0

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < H and 0 <= nj < W and zido[ni][nj] == '.' and zido[ci][cj] + 1 < burn[ni][nj]:
                queue.append((ni, nj))
                zido[ni][nj] = zido[ci][cj] + 1
                if ni == 0 or ni == H-1 or nj == 0 or nj == W-1:
                    return zido[ni][nj] + 1
    return 'IMPOSSIBLE'

# 테스트케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 빌딩 지도의 너비 W와 높이 H
    W, H = map(int, sys.stdin.readline().split())

    zido = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
    burn = deepcopy(zido)

    si, sj = 0, 0
    fire = []
    location()
    flame()
    print(bfs(si, sj))