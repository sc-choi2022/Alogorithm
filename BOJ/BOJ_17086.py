import sys, copy
from collections import deque
# bfs로 현재 상어 위치에서 다음 상어를 만날 때까지 거리를 구한다.
def bfs():
    # 상어의 위치를 모두 확인할 때까지
    while location:
        ci, cj = location.popleft()
        # 상어의 움직임인 8방향 움직임으로 다음 위치 ni,nj을 구한다.
        for di, dj in (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1):
            ni, nj = ci + di, cj + dj
            # ni,nj가 범위안에 있다면
            if 0 <= ni < N and 0 <= nj < M:
                # 상어가 없고 방문한 적 없는 곳이라면
                if visited[ni][nj] == 0:
                    # location에 값을 추가하고, 상어의 방문을 표시한다.
                    location.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1

N, M = map(int, sys.stdin.readline().split())
# 공간의 위치 정보를 담을 리스트 shark
shark = [0] * N
# 상어의 위치 정보를 담을 queue 변수 location
location = deque()
# N개의 줄에서
for i in range(N):
    # 각 줄을 받고 shark에 추가 하고 상어가 있는 줄이라면 상어의 위치를 location에 추가
    tmp = list(map(int, sys.stdin.readline().split()))
    shark[i] = tmp
    for j in range(M):
        if tmp[j] == 1:
            location.append((i, j))
# 상어의 이동방문과 이동거리 정보를 입력할 리스트 visited
visited = copy.deepcopy(shark)
# 상어의 안전거리 최댓값 변수 ans 값 초기화
ans = 0
# 함수 bfs 실행
bfs()
# 상어의 이동정보를 담을 visited에서 max값을 찾아 ans에 저장
for visit in visited:
    ans = max(ans, max(visit))

# ans의 max값은 출발위치의 값이 1이었으므로 -1을 하여 거리의 최댓값을 출력
print(ans-1)