import copy
from collections import deque
def bfs():
    tmp_arr = copy.deepcopy(arr)
    queue = deque()
    queue.append((0,0,0))
    visited[0][0] = 1
    while queue:
        ci, cj, yn = queue.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni = ci + di
            nj = cj + dj
            if 0<= ni < N and 0<= nj < M:
                if yn == 0:
                    if tmp_arr[ni][nj] == 0 and visited[ci][ci] + 1 < visited[ni][nj]:
                        visited[ni][nj] = visited[ci][ci] + 1
                        queue.append((ni,nj,yn))
                    elif tmp_arr[ni][nj] == 1:
                        queue.append((ni,nj,1))
                else:
                    if tmp_arr[ni][nj] == 0 and visited[ci][ci] + 1 < visited[ni][nj]:
                        visited[ni][nj] = visited[ci][ci] + 1
                        queue.append((ni,nj,yn))
    if visited[N-1][M-1] == 10000:
        return -1
    else:
        return visited[N-1][M-1]

N, M = map(int, input().split())
arr = [list(map(int, input())) for i in range(N)]
visited =[[1000]*M for _ in range(N)]
if (N, M) == (1, 1):
    print(1)
    exit()

print(bfs())