from collections import deque
import sys

# 게임 구역의 크기 N
N = int(sys.stdin.readline())
# 게임파의 구역을 저장하는 배열 game
game = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 출력하는 문구 answer
answer = 'Hing'

queue = deque([(0, 0)])
visit = [[0]*N for _ in range(N)]
visit[0][0] = 1
while queue:
    ci, cj = queue.popleft()
    number = game[ci][cj]

    if (ci, cj) == (N-1, N-1):
        answer = 'HaruHaru'
        break

    for di, dj in (0, 1), (1, 0):
        ni, nj = ci+number*di, cj+number*dj

        if ni < N and nj < N and not visit[ni][nj] and game[ni][nj]:
            queue.append((ni, nj))
            visit[ni][nj] = 1
# answer 출력
print(answer)