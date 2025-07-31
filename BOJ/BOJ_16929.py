import sys

def solve():
    global si, sj
    for i in range(N):
        for j in range(M):
            si, sj = i, j
            visit[i][j] = 1
            dfs(i, j, 0, 1)
            visit[i][j] = 0

            if answer == 'Yes':
                return

def dfs(ci, cj, dn, cnt):
    global answer

    for d in range(4):
        # 왔던 방향을 돌아가는 것을 제한
        if (dn-2)%4 == d:
            continue
        di, dj = D[d]
        ni, nj = ci+di, cj+dj
        if 0 <= ni < N and 0 <= nj < M and dots[ni][nj] == dots[ci][cj]:
            # 사이클은 찾은 경우
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

# 사이클을 확인하는 함수 solve
# 사이클을 찾은 경우 종료
solve()

print(answer)