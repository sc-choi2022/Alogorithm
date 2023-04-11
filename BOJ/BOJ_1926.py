from collections import deque
import sys

def bfs(si, sj):
    tmp = 1
    queue = deque([(si, sj)])

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and paper[ni][nj]:
                queue.append((ni, nj))
                paper[ni][nj] = 0
                tmp += 1
    return tmp

# 도화지의 세로 크기 N, 가로 크기 M
N, M = map(int, sys.stdin.readline().split())
# 도화지 배열 paper
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 그림의 개수 cnt, 가장 넓은 그림 넓이 area
cnt, area = 0, 0

for i in range(N):
    for j in range(M):
        if paper[i][j]:
            cnt += 1
            paper[i][j] = 0
            area = max(area, bfs(i, j))

# 그림의 개수 출력
print(cnt)
# 가장 넓은 그림 넓이 출력
print(area)