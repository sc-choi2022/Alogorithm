import sys
from collections import deque

def findbady():
    global si, sj
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                si, sj = i, j
                return
# bfs를 활용해서
def feedshark(i, j, shark_size):
    # bfs로 사용할 queue, 시작 위치를 queue에 추가
    queue = deque()
    queue.append((i,j))
    # 방문 여부를 표시할 행렬 visited, 시작 위치 i, j에 방문 표시 1을 한다.
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    # 시작 위치에서 각 위치까지 가는 데 걸리는 거리를 담을 행렬 distance
    distance = [[0]*N for _ in range(N)]
    # 시작 위치 i, j에서 출발해서 갈 수 있는 모든 경우를 담을 리스트 output
    output = []
    while queue:
        # 현재 위치 ci, cj
        ci, cj = queue.popleft()
        # 상하좌우로 움직이는 경우 이동한 위치 ni,nj
        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = ci + di, cj + dj
            # ni,nj가 범위안에 있고 물고기의 크기가 아기상어와 같거나 작은 경우(지나갈 수 있는 경우)
            if 0 <= ni < N and 0<= nj < N and visited[ni][nj] == 0 and sea[ni][nj] <= shark_size:
                # queue의 ni,nj 추가 visited[ni][nj]에 방문 표시와 distance[ni][nj]에 거리정보 입력
                queue.append((ni, nj))
                visited[ni][nj] = 1
                distance[ni][nj] = distance[ci][cj] + 1
                # 지나갈 수 있는 경우 중 아기상어가 먹을 수 있는 경우 output에 ni,nj와 distance 정보를 담아 준다.
                if sea[ni][nj] < shark_size and sea[ni][nj] != 0:
                    output.append((ni, nj, distance[ni][nj]))
    # output의 값을 거리, i좌표, j좌표 순으로 정렬을 해서 return
    return sorted(output, key=lambda x: (-x[2], -x[0], -x[1]))


# 아기상어와 물고기 정보를 알려주는 공간 sea와 공간의 크기 NxN의 N
N = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 아기상어의 초기 정보를 담을 si, sj, mass
si, sj, mass = 0, 0, 2
# 함수 findbaby를 통해 아기상어의 초기 위치를 잦는다.
findbady()

# 물고기를 잡아먹을 수 있는 시간 ans
ans = 0
# 자신의 크기만큼 먹었는 지 확인하기 위해 먹은 물고기의 개수를 세는 cnt
cnt = 0

while True:
    # 상어가 현재 위치에가 갈 수 있는 위치와 거리 정보가 정렬된 리스트로 변수 shark에 할당된다.
    shark = feedshark(si, sj, mass)
    # 더 갈 수 있는 위치가 없다면 break
    if len(shark) == 0:
        break
    # shark의 값 중 가장 합당한 값을 ni, nj, distance 변수에 할당
    ni, nj, distance = shark.pop()
    # 움직인 거리 만큼 ans에 더한다.
    ans += distance
    # sea의 출발점 si, sj와 도착점 ni,nj의 물고기 정보를 0으로 변경
    sea[si][sj] = 0
    sea[ni][nj] = 0
    # 아기 상어의 위치를 변경
    si, sj = ni, nj
    # 먹은 물고기 수 1 증가
    cnt += 1
    # 먹은 물고기 수가 아기상어의 크기와 같다면 아기상어 크기 1 증가
    if cnt == mass:
        mass += 1
        # 먹은 물고기 수 초기화
        cnt = 0
# ans 출력
print(ans)