from collections import deque
import sys

# 땅의 위치 si, sj를 매개변수로 시작하는 bfs
def bfs(si, sj):
    # queue 생성 후 (si, sj) 추가
    queue = deque()
    queue.append((si, sj))

    while queue:
        ci, cj = queue.popleft()

        # 섬의 기준이 되는 8방향을 확인
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1):
            # 다음 위치 ni, nj
            ni, nj = ci + di, cj + dj
            # 지도의 크기를 벗어나지 않고 땅인 경우
            if 0 <= ni < h and 0 <= nj < w and island[ni][nj]:
                # queue에 (ni, nj) 추가
                queue.append((ni, nj))
                # 지도의 (ni, nj)위치를 0으로 변경
                island[ni][nj] = 0

while True:
    # 너비 w, 높이 h
    w, h = map(int, sys.stdin.readline().split())
    # w = 0, h = 0인 경우 break
    if (w, h) == (0, 0):
        break
    # 지도의 정보를 담을 리스트 island
    island = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    # 출력할 섬의 개수 ans
    ans = 0

    for i in range(h):
        for j in range(w):
            # island[i][j]가 땅인 경우 bfs(i, j) 실행
            if island[i][j]:
                bfs(i, j)
                ans += 1
    # ans 출력
    print(ans)