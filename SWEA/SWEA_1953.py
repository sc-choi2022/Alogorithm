import collections
import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T + 1):
    # 지하터널크기 세로 N, 가로 M, 뚜껑의 위치 세로 R, 가로 C, 탈출 후 소요된 시간 L
    info = list(map(int, input().split()))
    N, M, R, C, L = info[0], info[1], info[2], info[3], info[4]
    # 지하 터널은 총 7 종류의 터널 구조물정보를 담은 리스트 maze
    maze = [list(map(int, input().split())) for _ in range(N)]
    # 방문가능한 터널을 표시할 리스트 visited
    visited = [[0] * M for _ in range(N)]
    # 터널의 종류의 번호에 맞춰 방향값을 담은 리스트 direct
    direct = [0, ((0, 1), (1, 0), (0, -1), (-1, 0)), ((1, 0), (-1, 0)), ((0, 1), (0, -1)), ((0, 1), (-1, 0)),
              ((0, 1), (1, 0)), ((1, 0), (0, -1)), ((0, -1), (-1, 0))]

    # 뚜껑의 위치 세로 R, 가로 C를 시작위치(i,j)로 지정
    i, j = R, C
    # queue를 이용하여 bfs진행
    queue = collections.deque()
    queue.append((i, j))
    # 방문한 첫 위치는 1시간 뒤이므로 1부터 visited에 할당
    visited[i][j] = 1

    while queue:
        si, sj = queue.popleft()

        # si, sj의 정보를 가지고 direct에서 가능한 방항을 di, dj를 통해 얻어낸다.
        for di, dj in direct[maze[si][sj]]:
            ni = si + di
            nj = sj + dj
            # ni, nj값이 범위 안에 있고 방문한 적이 없으며 현재 터널의 모양으로 다음 터널의 모양에 접근할 수 있는지 확인하고 현재 위치의 visited 값이 시간범위안에 있다면
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] != 0 and visited[ni][nj] == 0 and (di * -1, dj * -1) in \
                    direct[maze[ni][nj]] and visited[si][sj] < L:
                # queue에 값을 추가하고 visited에 (si,sj) 위치값에 1을 더한 값을 (ni,nj)에 할당한다.
                queue.append((ni, nj))
                visited[ni][nj] = visited[si][sj] + 1

    # visited의 방문을 의미하는 0이 아닌 숫자의 개수를 세기 위한 변수 ans
    ans = 0
    # visited의 각 행의 0의 값을 더해서 ans를 만든다.
    for visit in visited:
        ans += visit.count(0)
    # 테스트 케이스 번호와 전체 칸의 수에서 ans값을 뺀 값을 출력
    print(f'#{case} {N * M - ans}')