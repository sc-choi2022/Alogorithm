from collections import deque
from copy import deepcopy
from itertools import combinations
import sys

def bfs(lst):
    global time
    tmp = deepcopy(test)
    queue = deque(lst)
    # 바이러스의 위치를 배열 tmp에 반영
    for li, lj in lst:
        tmp[li][lj] = 0

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and tmp[ni][nj] == -1:
                tmp[ni][nj] = tmp[ci][cj] + 1
                queue.append((ni, nj))
    # 바이러스가 모두 퍼진 시점의 시간
    number = 0
    for ii in range(N):
        for jj in range(N):
            if tmp[ii][jj] == -1:
                return
            # 바이러스가 놓여있고 벽이 아닌 경우
            elif tmp[ii][jj] and lab[ii][jj] != 1:
                number = max(number, tmp[ii][jj])
    # 최소시간을 갱신
    time = min(time, number)

# 연구소의 크기 N, 바이러스의 개수
N, M = map(int, sys.stdin.readline().split())
# 연구소의 상태 lab
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 바이러스의 위치외에 동일한 부분을 저장할 배열 test
test = [[-1]*N for _ in range(N)]
# 최소시간 time
time = 100000
# 바이러스를 놓을 수 있는 위치 place
place = []
for pi in range(N):
    for pj in range(N):
        if lab[pi][pj] == 2:
            place.append((pi, pj))
        if lab[pi][pj] == 1:
            test[pi][pj] = 1
# 바이러스를 M개 놓을 수 있는 모든 경우의 수 virun
virus = list(combinations(place, M))
for v in virus:
    bfs(v)
# 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력
# 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력
print(-1 if time == 100000 else time)