from collections import deque
import sys

def dfs(si, sj):
    global check
    visit[si][sj] = 1
    for di, dj in (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1):
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < M:
            if farm[ni][nj] > farm[si][sj]:
                check = 0
            if farm[ni][nj] == farm[si][sj] and not visit[ni][nj]:
                dfs(ni, nj)

# 농장의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 농장의 높이를 저장하는 배열 farm
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
# 봉우리의 개수 answer
answer = 0

# 봉우리 가능한 위치 찾기
# dfs로 주변이 다 작은지 확인

# 봉우리를 저장하는 배열 peaks
peaks = []
for i in range(N):
    for j in range(M):
        if farm[i][j] and not visit[i][j]:
            check = 1
            dfs(i, j)
            answer += check

# 산봉우리의 개수를 출력
print(answer)