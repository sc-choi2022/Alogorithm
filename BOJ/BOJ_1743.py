from collections import deque
import sys

def bfs(si, sj):
    global amount
    queue = deque([(si, sj)])
    trash[si][sj] = 0
    tmp = 1

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and trash[ni][nj]:
                queue.append((ni, nj))
                trash[ni][nj] = 0
                tmp += 1
    # 가장 큰 음식물의 크기 갱신
    amount = max(amount, tmp)

# 통로의 세로 길이 N, 가로 길이 M, 음식물 쓰레기의 개수 K
N, M, K = map(int, sys.stdin.readline().split())
# 통로의 쓰레기 크기를 저장할 배열 trash
trash = [[0]*M for _ in range(N)]
# 가장 큰 음식물의 크기 amount
amount = 0

for _ in range(K):
    # 좌표 r, c
    r, c = map(int, sys.stdin.readline().split())
    # 음식물의 위치를 배열 trash에 반영
    trash[r-1][c-1] = 1

for i in range(N):
    for j in range(M):
        if trash[i][j]:
            bfs(i, j)

# 음식물 중 가장 큰 음식물의 크기를 출력
print(amount)