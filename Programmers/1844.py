from collections import deque

def solution(maps):
    answer = bfs(maps, len(maps), len(maps[0]))
    return answer

def bfs(zido, N, M):
    queue = deque([(0, 0)])

    visit = [[0] * M for _ in range(N)]
    visit[0][0] = 1
    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and zido[ni][nj] and not visit[ni][nj]:
                visit[ni][nj] = visit[ci][cj] + 1
                queue.append((ni, nj))

    cnt = visit[N - 1][M - 1] if visit[N - 1][M - 1] else -1
    return cnt