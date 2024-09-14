from collections import deque
import sys

def bfs():
    queue = deque([(0, 0)])
    visit[0][0] = 1
    cnt = 0

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not visit[ni][nj]:
                if not cheeses[ni][nj]:
                    visit[ni][nj] = 1
                    queue.append((ni, nj))
                else:
                    cheeses[ni][nj] = 0
                    visit[ni][nj] = 1
                    cnt += 1
    answer.append(cnt)
    return cnt

# 세로와 가로의 길이 N, M
N, M = map(int, sys.stdin.readline().split())
# 치즈의 위치가 담긴 배열 cheeses
cheeses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 각 시간에 치즈의 개수
answer = []

# 치즈가 모두 녹아 없어지는 데 걸리는 시간 time
time = -1
while True:
    time += 1
    visit = [[0]*M for _ in range(N)]
    cnt = bfs()

    if cnt == 0:
        break

# 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력
print(time)
# 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력
print(answer[-2])