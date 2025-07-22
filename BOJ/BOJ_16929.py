import sys

def start(ii):
    global sj

    for jj in range(M):
        sj = jj

        for dd in range(4):
            ddi, ddj = D[dd]
            nni, nnj = si+ddi, sj+ddj
            if 0 <= nni < N and 0 <= nnj < M and dots[si][sj] == dots[nni][nnj]:
                if cycle(nni, nnj):
                    return True
    return False

def cycle(ci, cj):
    if (ci, cj) == (si, sj):
        return True

    for dd in range(4):
        di, dj = D[dd]
        ni, nj = ci+di, cj+dj
        if 0 <= ni < N and 0 <= nj < M and not visit[ni][nj] and dots[ni][nj] == dots[ci][cj]:
            visit[ni][nj] = 1
            cycle(ni, nj)
            visit[ni][nj] = 0
    return False

# 게임판의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 게이판의 점의 색을 저장하는 배열 dots
dots = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

# 방향을 저장하는 딕셔너리 D
D = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
si, sj = 0, 0
for i in range(N-1):
    si = i

    if start(si):
        print('Yes')
        break
else:
    print('No')