from collections import deque
import sys

def bfs(si, sj):
    cnt = 1
    queue = deque([(si, sj)])
    grid[si][sj] = 1

    while queue:
        ci, cj = queue.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not grid[ni][nj]:
                cnt += 1
                queue.append((ni, nj))
                grid[ni][nj] = 1
    # 현재 영역의 넓이를 area에 저장
    area.append(cnt)

# 모눈종이의 크기 M, N, 직사각형의 개수 K
M, N, K = map(int, sys.stdin.readline().split())
# 모눈종이 grid
grid = [[0]*M for _ in range(N)]
# 영역의 넓이를 저장하는 배열 area
area = []

for _ in range(K):
    i1, j1, i2, j2 = map(int, sys.stdin.readline().split())

    for i in range(i1, i2):
        for j in range(j1, j2):
            grid[i][j] = 1

for ii in range(N):
    for jj in range(M):
        if not grid[ii][jj]:
            bfs(ii, jj)

# 각 영역의 넓이를 오름차순으로 정렬
area.sort()
# 나누어지는 영역의 개수를 출력
print(len(area))
# 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력
print(*area)