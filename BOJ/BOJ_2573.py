from collections import deque
import sys

def melt():
    queue = deque(iceberg)

    while queue:
        ci, cj = queue.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            if not ocean[ci][cj]:
                iceberg.remove((ci, cj))
                break
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not ocean[ni][ni]:
                ocean[ci][cj] -= 1
                if not ocean[ci][cj]:
                    iceberg.remove((ci, cj))
                    break

def seperate(si, sj):
    global flag
    tmp = [(si, sj)]

    queue = deque([(si, sj)])
    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not ocean[ni][ni] and (ni, nj) not in tmp:
                queue.append((ni, nj))
                tmp.append((ni, nj))

    if len(tmp) != len(iceberg):
        flag = True

# 행의 개수와 열의 개수 N, M
N, M = map(int, sys.stdin.readline().split())
# 바다의 정보를 담을 배열 ocean
ocean = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 빙하의 정보를 담을 배열 iceberg
iceberg = []
# 빙산이 분리되는 시간 time, 분리여부 flag
time, flag = 0, False

for i in range(N):
    for j in range(M):
        if ocean[i][j]:
            iceberg.append((i, j))


while True:
    print(len(iceberg), flag, time)
    for o in ocean:
        print(*o)

    if not iceberg and not flag:
        print(0)
        break

    if flag:
        print(time)
        break

    melt()
    time += 1
    si, sj = iceberg[0]
    seperate(si, sj)