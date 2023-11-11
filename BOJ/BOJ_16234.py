from collections import deque
import sys

def bfs(si, sj):
    queue = deque([(si, sj)])
    # 이동가능한 위치를 저장하는 배열 tmp, 위치들의 인구수를 저장하는 변수 add
    tmp, add = [], 0

    while queue:
        ci, cj = queue.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and L <= abs(nation[ni][nj] - nation[ci][cj]) <= R and not visit[ni][nj]:
                visit[ni][nj] = 1
                queue.append((ni, nj))
                tmp.append((ni, nj))
                add += nation[ni][nj]
    return [tmp, add]

# N×N 크기의 땅, L명 이상, R명 이하
N, L, R = map(int, sys.stdin.readline().split())
# 각 나라의 인구수를 담을 배열 nation
nation = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 인구 이동이 일어나는 일수 day
day = 0

while True:
    visit = [[0]*N for _ in range(N)]
    flag = False

    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                visit[i][j] = 1
                # 이동하는 위치를 담은 배열 moves return
                moves, number = bfs(i, j)
                if len(moves):
                    flag = True
                    moves.append((i, j))
                    number += nation[i][j]
                    num = number // len(moves)
                    for mi, mj in moves:
                        nation[mi][mj] = num
    if not flag:
        break
    day += 1
# 인구 이동이 일어나는 일수 출력
print(day)