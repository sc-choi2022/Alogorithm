from collections import deque

def solution(maps):
    answer = bfs(maps, len(maps), len(maps[0]))
    return answer

def bfs(zido, N, M):
    queue = deque([(0, 0)])
    # 방문한 칸의 개수를 저장하는 배열 visit, 첫 시작위치 (0, 0)를 표시
    visit = [[0] * M for _ in range(N)]
    visit[0][0] = 1
    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            # 움직일 수 있는 경우
            if 0 <= ni < N and 0 <= nj < M and zido[ni][nj] and not visit[ni][nj]:
                visit[ni][nj] = visit[ci][cj] + 1
                queue.append((ni, nj))
    # 지나가야하는 칸의 개수를 변수 cnt에 저장, 도착할 수 없을 경우 -1을 저장
    cnt = visit[N - 1][M - 1] if visit[N - 1][M - 1] else -1
    return cnt