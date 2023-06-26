from collections import deque
import sys

def bfs(si, sj):
    global W, B
    queue = deque([(si, sj)])
    color = army[si][sj]
    # 인접한 같은 나라 병사 수 cnt
    cnt = 1

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < M and 0 <= nj < N and not visit[ni][nj] and army[ni][nj] == color:
                queue.append((ni, nj))
                visit[ni][nj] = 1
                cnt += 1
    if color == 'W':
        W += cnt**2
    else:
        B += cnt**2
# 전쟁터의 가로 크기 N, 세로 크기 M
N, M = map(int, sys.stdin.readline().split())
# 병사의 상태를 담을 배열 army
army = [list(sys.stdin.readline().rstrip()) for _ in range(M)]
# 아군의 병사의 위력 W, 적군 병사의 위력 B
W, B = 0, 0
# 확인여부를 저장하는 배열 visit
visit = [[0]*N for _ in range(M)]

for i in range(M):
    for j in range(N):
        if not visit[i][j]:
            visit[i][j] = 1
            bfs(i, j)
# 나라의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력
print(W, B)