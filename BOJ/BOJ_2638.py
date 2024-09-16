from collections import deque
import sys

def bfs():
    queue = deque([(0, 0)])
    visit[0][0] = 1

    # 녹은 치즈의 개수 cnt
    cnt = 0
    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not cheeses[ni][nj] and not visit[ni][nj]:
                    visit[ni][nj] = 1
                    queue.append((ni, nj))
                elif cheeses[ni][nj] and visit[ni][nj] < 2:
                    visit[ni][nj] += 1
                    if visit[ni][nj] == 2:
                        cheeses[ni][nj] = 0
                        cnt += 1
    return cnt

# 모눈종이의 크기를 나타내는 두 개의 정수 N, M
N, M = map(int, sys.stdin.readline().split())
# 치즈의 위치를 저장하는 배열 cheeses
cheeses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간 time
time = -1
while True:
    time += 1
    visit = [[0] * M for _ in range(N)]

    if bfs() == 0:
        break

# time 출력
print(time)