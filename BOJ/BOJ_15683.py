import sys

def dfs(idx):
    global answer
    # 방향을 정한 cctv가 K개인 경우
    if idx == K:
        answer = min(answer, space-monitor())
        return
    # idx번째 cctv의 위치
    ci, cj = cctv[idx]
    # cctv의 종류에 따른 감시방향이 저장된 배열 ways
    ways = number[room[ci][cj]]

    for way in ways:
        choose[ci][cj] = way
        dfs(idx+1)

def monitor():
    # 현재 cctv의 위치에서 감시 가능한 칸의 개수 cnt
    cnt = 0
    # visit 배열 초기화
    visit = [[0]*M for _ in range(N)]

    for c in cctv:
        si, sj = c
        for d in choose[si][sj]:
            di, dj = direction[d]
            ni, nj = si+di, sj+dj
            while 0 <= ni < N and 0 <= nj < M:
                # 벽의 위치에 도달한 경우
                if room[ni][nj] == 6:
                    break
                # 이전에 감시하지 않은 칸인 경우
                elif not room[ni][nj] and not visit[ni][nj]:
                    cnt += 1
                    visit[ni][nj] = 1
                ni, nj = ni+di, nj+dj
    return cnt

# 사무실의 세로 크기 N, 가로 크기 M
N, M = map(int, sys.stdin.readline().split())
# 사무실의 정보 room
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# cctv의 위치를 저장하는 배열 cctv
cctv = []
# 감시할 수 있는 영역의 개수 space
space = 0

for i in range(N):
    for j in range(M):
        # CCTV인 경우
        if 0 < room[i][j] < 6:
            cctv.append((i, j))
        elif room[i][j] == 0:
            space += 1

# cctv의 개수 K
K = len(cctv)
# cctv 번호에 따른 감시가능 방향을 저장하는 배열 number
number = {1: [[0], [1], [2], [3]], 2: [[0, 2], [1, 3]], 3: [[0, 1], [1, 2], [2, 3], [3, 0]],
          4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], 5: [[0, 1, 2, 3]]}
# cctv의 감시방향을 저장하는 딕셔너리 direction
direction = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

# 사각 지대의 최소 크기 answer
answer = N*M
# cctv의 방향설정을 저장하는 배열 choose
choose = [[[] for _ in range(M)] for _ in range(N)]
# 감시 여부를 저장하는 배열 visit
visit = [[0]*M for _ in range(N)]

dfs(0)

# 사각 지대의 최소 크기를 출력
print(answer)