from collections import deque
import sys

# 게임 구역의 크기 N
N = int(sys.stdin.readline())
# 게임판의 구역 맵 zido
zido = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 방문여부를 저장하는 배열 visit
visit = [[0]*N for _ in range(N)]
visit[0][0] = 1

queue = deque([(0, 0)])

while queue:
    ci, cj = queue.popleft()
    num = zido[ci][cj]

    for di, dj in (0, 1), (1, 0):
        # 이동가능한 위치 ni, nj
        ni, nj = ci + num * di, cj + num * dj
        if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj]:
            visit[ni][nj] = 1
            queue.append((ni, nj))
# ‘쩰리’가 끝 점에 도달할 수 있으면 HaruHaru,
# 도달할 수 없으면 Hing 출력
print('HaruHaru' if visit[N-1][N-1] else 'Hing')