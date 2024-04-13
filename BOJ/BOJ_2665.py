from collections import deque
import sys

# 한 줄에 들어가는 방의 수 N
N = int(sys.stdin.readline())
# 방의 종류를 저장하는 배열 rooms
rooms = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
# 방문 시 흰 방으로 바꿔야하는 수를 저장하는 배열 visit
visit = [[-1]*N for _ in range(N)]
visit[0][0] = 0

queue = deque([(0, 0)])

while queue:
    ci, cj = queue.popleft()

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N:
            if visit[ni][nj] == -1:
                if rooms[ni][nj]:
                    queue.appendleft((ni, nj))
                    visit[ni][nj] = visit[ci][cj]
                else:
                    queue.append((ni, nj))
                    visit[ni][nj] = visit[ci][cj] + 1
    # 바꾸어야할 최소 방의 수가 구해진 경우 break
    if visit[N-1][N-1] != -1:
        break
# 흰 방으로 바꾸어야 할 최소의 검은 방의 수를 출력
print(visit[N-1][N-1])