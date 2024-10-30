import sys
from collections import deque

def bfs():
    while queue:
        si, sj = queue.popleft()
        # 네 방향에 대한 di, dj
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = si + di, sj + dj
            # ni,nj가 범위 안에 있고 area[ni][nj]가 바이러스에 감염되지 않았다면
            if 0 <= ni < N and 0 <= nj < N and not area[ni][nj]:
                # 다음 queue에 위치값을 추가 후 area에 감염정보를 반영한다.
                next_queue.append((ni,nj))
                area[ni][nj] = area[si][sj]
                # 만약 찾는 위치에 바이러스가 있다면 bfs를 마친다.
                if (ni, nj) == (X-1, Y-1):
                    return

# NxN의 N, 바이러스의 종류 수 K
N, K = map(int, sys.stdin.readline().split())
# 바이러스의 초기 정보를 담은 리스트 area
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# S초에 대한 정보 S, 위치좌표 X, Y
S, X, Y = map(int, sys.stdin.readline().split())

# 각 단계 별 queue를 구분하기 위해 queue, next_queue 두개의 deque를 생성
queue = deque()
next_queue = deque()
# 시간을 세기위한 변수 cnt를 0으로 초기화
cnt = 0
# K개의 종류의 바이러스의 초기 위치를 바이러스 번호 순서로 queue에 담아 준다.
for k in range(1, K+1):
    for i in range(N):
        for j in range(N):
            if area[i][j] == k:
                queue.append((i,j))
# S 시간이 될때까지 while문을 진행한다.
while cnt < S:
    # queue에 담긴 위치를 가지고 bfs를 진행
    bfs()
    # cnt 1증가
    cnt += 1
    # bfs에서 만들어진 next_queue를 queue에 할당 후 next_queue를 초기화
    queue = next_queue
    next_queue = deque()
    
# X, Y 위치의 S초 후의 바이러스 정보를 출력한다.
print(area[X-1][Y-1])