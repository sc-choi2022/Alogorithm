from collections import deque
import sys

def bfs(si, sj):
    queue = deque([(si, sj)])

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < M and 0 <= nj < N and banner[ni][nj]:
                queue.append((ni, nj))
                banner[ni][nj] = 0

# 현수막의 크기 M, N
M, N = map(int, sys.stdin.readline().split())
# 현수막의 내용을 저장하는 배령 banner
banner = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
# 글자의 개수 cnt
cnt = 0

for i in range(M):
    for j in range(N):
        if banner[i][j]:
            banner[i][j] = 0
            bfs(i, j)
            cnt += 1
# 현수막에서 글자의 개수 출력
print(cnt)