from collections import deque
import sys

# 체스판의 크기 N
N = int(sys.stdin.readline())
# 데스 나이트의 출발 위치 (R1, C1), 도착 위치 (R2, C2)
R1, C1, R2, C2 = map(int, sys.stdin.readline().split())

graph = [[-1]*(N+1) for _ in range(N+1)]
graph[R1][C1] = 0
queue = deque([(R1, C1)])

while queue:
    ci, cj = queue.popleft()

    for di, dj in (-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1):
        ni, nj = ci + di, cj + dj

        if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] == -1:
            graph[ni][nj] = graph[ci][cj] + 1
            queue.append((ni, nj))

    if graph[R2][C2] != -1:
        break
# 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력
# 이동할 수 없는 경우에는 -1을 출력
print(graph[R2][C2])