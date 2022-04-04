# dfs를 활용하는 방법
def dfs(si, sj, n, Sum):
    global ans
    # 4개의 정사각형을 더했다면 ans와 Sum을 비교하여 큰 값을 ans에 저장
    if n == 3:
        ans = max(ans, Sum)
        return
    else:
        # 상하좌우방향으로 배치할 수 있는 di,dj
        for di, dj in ((0,1), (1,0), (0, -1), (-1, 0)):
            ni = si + di
            nj = sj + dj
            # ni, nj가 범위내에 있고 방문하지 않은 곳이라면
            if 0<= ni < N and 0<= nj < M and visited[ni][nj] == 0:
                # 방향키 모양을 하기 위해 두번 이동할때 새로 dfs를 시작하는 if문
                if n == 1:
                    # dfs이전에 방문표시를 하고 dfs를 나온 후 방문표시 취소
                    visited[ni][nj] = 1
                    dfs(si, sj, n + 1, Sum + arr[ni][nj])
                    visited[ni][nj] = 0
                # dfs이전에 방문표시를 하고 dfs를 나온 후 방문표시 취소
                visited[ni][nj] = 1
                dfs(ni, nj, n +1, Sum + arr[ni][nj])
                visited[ni][nj] = 0
# NxM 행렬의 길이 값 N, M
N, M = map(int, input().split())
# NxM 행렬의 값을 담은 리스트 arr
arr = [list(map(int, input().split())) for _ in range(N)]
# arr 리스트의 방문표시를 위해 만드는 리스트 visited
visited = [[0]*M for _ in range(N)]
# 정답 ans 값을 초기화
ans = 0
# prunning을 위해 max_val를 확인
max_val = max(max(*arr))

# 모든 위치를 시작위치로 함수 dfs를 실행
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = 0
# ans를 출력
print(ans)

# 5개의 모양에 대한 모든 경우의 수를 case를 나누어 방향값을 작성
case = [
    # case 1
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],

    # case 2
    [[0, 0], [0, 1], [1, 0], [1, 1]],

    # case 3
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [0, 1], [-1, 1], [-2, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],

    # case 4
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [-1, 1], [-1, 2]],
    [[0, 0], [0, 1], [-1, 1], [1, 0]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],

    # case 5
    [[0, 0], [0, 1], [-1, 1], [1, 1]],
    [[0, 0], [0, 1], [-1, 1], [0, 2]],
    [[0, 0], [1, 0], [1, 1], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 1]]
]
# case에 따라 4개의 정사각형을 값을 더하는 함수 tetro
def tetro(i, j):
    # ans값을 수정하기 위해 global ans
    global ans
    # 19개의 case에 대해
    for x in range(19):
        Sum = 0
        # 각 case의 4개의 위치를 확인
        for y in range(4):
            temp = case[x][y]
            ni = i + temp[0]
            nj = j + temp[1]
            # 위치가 범위안에 있다면 Sum에 더해주고
            if 0<= ni < N and 0<= nj < M:
                Sum += arr[ni][nj]
            # 범위를 벗어나면 다음 case를 확인한다.
            else:
                break
        # Sum이 완성될 때마다 ans와 Sum을 비교하여 큰 값을 ans에 저장한다.
        ans = max(ans, Sum)
    return

# NxM 행렬의 길이 값 N, M
N, M = map(int, input().split())
# NxM 행렬의 값을 담은 리스트 arr
arr = [list(map(int, input().split())) for _ in range(N)]
# ans값 초기화
ans = 0
# 모든 위치에서 함수 tetro를 실행
for i in range(N):
    for j in range(M):
        tetro(i, j)
# ans를 출력
print(ans)