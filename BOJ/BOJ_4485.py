from heapq import heappush, heappop
import sys

def bfs():

    queue = []
    heappush(queue, (cave[0][0], 0, 0))
    visited[0][0] = 0

    while queue:
        c, ci, cj = heappop(queue)
        if (ci, cj) == (N-1, N-1):
            print(f'Problem {cnt}: {visited[ci][cj]}')
            break

        for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            else:
                if c + cave[ni][nj] < visited[ni][nj]:
                    visited[ni][nj] = c + cave[ni][nj]
                    heappush(queue, (c + cave[ni][nj], ni, nj))

cnt = 1
while True:
    # 동굴의 크기
    N = int(sys.stdin.readline())
    if N == 0:
        break

    cave = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[sys.maxsize]*N for _ in range(N)]
    bfs()
    cnt += 1