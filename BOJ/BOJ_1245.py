import sys
def dfs(a, b):
    global check
    # 방문을 표시
    visited[a][b] = True
    # 인접한 격자를 모두 확인
    for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1):
        # 방향에 따른 인접 격자의 위치 ni, nj
        ni, nj = a + di, b + dj
        # ni, nj가 범위안에 존재하는 경우
        if 0 <= ni < N and 0 <= nj < M:
            # 현재 위치가 인접 격자의 위치보다 낮을 경우 check에 False 저장
            if farm[a][b] < farm[ni][nj]:
                check = False
            # 확인하지 않은 위치이며 현재위치와 인접 격자 위치의 높이가 동일한 경우
            if not visited[ni][nj] and farm[a][b] == farm[ni][nj]:
                # 인접 위치로 dfs 실행
                dfs(ni, nj)

# 농장의 격자를 이루는 N, M
N, M = map(int, sys.stdin.readline().split())
# 농장의 높이를 담을 행렬 farm
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 하나의 격자가 인접한 경우를 확인하기 위한 행렬 visited
visited = [[0]*M for _ in range(N)]
# 출력할 산봉우리의 개수 cnt
cnt = 0

for i in range(N):
    for j in range(M):
        # 농장의 높이가 존재하고 확인하지 않은 곳인 경우
        if farm[i][j] and not visited[i][j]:
            # 변수 check를 True로 초기화
            check = True
            # 함수 dfs를 실행
            dfs(i, j)
            # dfs를 후 ckeck가 True로 봉우리가 맞는 경우
            if check:
                print(i, j)
                # 봉우리를 cnt
                cnt += 1
# 산봉우리의 개수 출력
print(cnt)