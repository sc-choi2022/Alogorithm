import sys

# 종이의 크기 NxM
N, M = map(int, sys.stdin.readline().split())
# 위치에 정육면체수를 저장할 배열 grid
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 겉넓이 area
area = 2 * N * M

for i in range(N):
    for j in range(M):
        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            # (i, j) 위치의 옆칸이 존재가능한 위치 ni, nj
            ni, nj = i + di, j + dj
            # 옆칸이 존재하는 경우
            if 0 <= ni < N and 0 <= nj < M:
                # 옆칸보다 현재칸의 정육면체 개수가 많은 경우
                if grid[i][j] > grid[ni][nj]:
                    area += (grid[i][j] - grid[ni][nj])
            # 끝칸에 존재하는 경우
            else:
                area += grid[i][j]
# 도형의 겉넓이를 출력
print(area)