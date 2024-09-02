import sys
from collections import deque

# 지도의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 지도를 저장하는 배열 zido
zido = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

queue = deque([(0, 0, 0, 1)])
while queue:
    ci, cj, flag, cnt = queue.popleft()

    if (ci, cj) == (N-1, M-1):
        print(cnt)
        break

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj

        if 0 <= ni < N and 0 <= nj < M:
            # 벽을 깨지 않고 도달한 경우
            if not flag:
                if zido[ni][nj] == 0 or zido[ni][nj] == 3:
                    zido[ni][nj] = 2
                    queue.append((ni, nj, flag, cnt+1))
                elif zido[ni][nj] == 1:
                    queue.append((ni, nj, 1, cnt+1))
            # 벽을 깨고 도달한 경우
            else:
                if zido[ni][nj] == 0:
                    zido[ni][nj] = 3
                    queue.append((ni, nj, flag, cnt+1))
else:
    print(-1)