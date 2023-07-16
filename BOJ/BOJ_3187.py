from collections import deque
import sys

def bfs(si, sj):
    global wolf, sheep
    queue = deque([(si, sj)])
    visit[si][sj] = 1

    tmp_wolf, tmp_sheep = 0, 0

    if area[si][sj] == 'v':
        tmp_wolf += 1
    elif area[si][sj] == 'k':
        tmp_sheep += 1

    while queue:
        ci, cj = queue.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < R and 0 <= nj < C and area[ni][nj] != '#' and not visit[ni][nj]:
                visit[ni][nj] = 0
                if area[ni][nj] == 'v':
                    tmp_wolf += 1
                elif area[ni][nj] == 'k':
                    queue.append((ni, nj))

    if tmp_sheep > tmp_wolf:
        sheep += tmp_sheep
    else:
        wolf += tmp_wolf

# 영역의 세로의 길이 R, 세로의 길이 C
R, C = map(int, sys.stdin.readline().split())
# 울타리, 늑대, 양이 있는 공간의 정보를 저장하는 배열 area
area = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
# 살아남은 늑대의 수 wolf, 양의 수 sheep
wolf, sheep = 0, 0
visit = [[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if area[i][j] != '#' and not visit[i][j]:
            bfs(i, j)
# 살아남게 되는 양과 늑대의 수를 각각 순서대로 출력
print(wolf, sheep)