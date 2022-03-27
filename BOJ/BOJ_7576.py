import sys
from collections import deque

# 가로 M, 세로 N, 높이 H
M, N, H = map(int, sys.stdin.readline().split())

# 토마토를 담을 상자 리스트 box
box = []
# 토마토의 정보를 box에 담는다.
for _ in range(H):
    box.append([list(map(int, input().split())) for _ in range(N)])

# BFS에 사용할 queue 생성
queue = deque()
# 일수를 담을 상자와 같은 사이즈의 리스트 days
days = [[[0]*M for _ in range(N)] for _ in range(H)]
# 모든 익은 토마토를 box 리스트에 반영
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append((i,j,k))
                box[i][j][k] = -1
# BFS에 사용하는 queue가 빌때까지
while queue:
    # si, sj, sk는 queue에 담긴 좌표의 시작 값
    temp = queue.popleft()
    si = temp[0]
    sj = temp[1]
    sk = temp[2]
    # 주어진 6 방향으로 움직였을 때
    for di, dj, dk in ((1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)):
        ni = si + di
        nj = sj + dj
        nk = sk + dk
        # 범위 안이고 익지 않은 토마토라면
        if 0<= ni < H and 0<= nj < N and 0<= nk < M and box[ni][nj][nk] == 0:
            # 익은 토마토로 바꾸고
            box[ni][nj][nk] = 1
            # queue에 좌표를 추가하고
            queue.append((ni, nj, nk))
            # days에 일수를 출발 일수 +1 하여 동일 좌표에 추가
            days[ni][nj][nk] = days[si][sj][sk] + 1

# 만약 익지 않은 토마토 0이 남아있다면
def check(box):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    # -1를 return
                    return -1
    # 토마토가 다 익었다면 0을 return
    return 0

# 만약 check의 return 값이 -1 이라면 -1 출력
if check(box) == -1:
    print(-1)
# 아닌 경우 days의 최대 값을 찾아 ans에 할당 후 ans 출력
else:
    ans = 0
    for i in range(H):
        for j in range(N):
            if max(days[i][j]) > ans:
                ans = max(days[i][j])
    print(ans)