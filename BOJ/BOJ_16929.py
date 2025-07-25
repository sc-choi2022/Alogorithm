import sys

def solve():
    global si, sj, answer
    for si in range(N):
        for sj in range(M):
            visit[si][sj] = 1
            dfs(si, sj, 0, 1)
            visit[si][sj] = 0

            if answer == 'Yes':
                return

def dfs(ci, cj, dn, cnt):
    global answer

    for d in range(4):
        if (dn-2)%4 == d:
            continue
        di, dj = D[d]
        ni, nj = ci+di, cj+dj
        if 0 <= ni < N and 0 <= nj < M and dots[ni][nj] == dots[ci][cj]:
            if (ni, nj) == (si, sj) and cnt > 3:
                answer = 'Yes'
                return
            if not visit[ni][nj]:
                visit[ni][nj] = 1
                dfs(ni, nj, d, cnt+1)
                visit[ni][nj] = 0


# 게임판의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 게이판의 점의 색을 저장하는 배열 dots
dots = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

# 방향을 저장하는 딕셔너리 D
D = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
si, sj = 0, 0
answer = 'No'

solve()

print(answer)