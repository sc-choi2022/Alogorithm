from collections import deque
import sys
sys.stdin = open('sample_input.txt')

# 테스트케이스의 개수
T = int(input())
for case in range(1, T+1):
    # NxN행렬의 한 변의 길이 N
    N = int(input())
    # NxN의 행렬을 담은 리스트 maze
    maze = [list(map(int, input())) for _ in range(N)]

    # 방향의 정보를 담은 리스트 di, dj
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 시작위치 start와 종료위치 end를 구하는 for문
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)

    # start위치를 2로 찾은 후 정답을 구하기 위해 시작 위치의 값을 0으로 할당
    maze[start[0]][start[1]] = 0
    # queue와 visited를 생성하고 시작 점의 위치를 추가
    queue = deque()
    queue.append(start)
    visited = [start]

    # 정답 ans 초기화
    ans = 0
    # BFS를 진행
    while queue:
        # queue의 가장 앞 값을 변수 tmp에 할당
        tmp = queue.popleft()
        i = tmp[0]
        j = tmp[1]

        # tmp의 위치에서 모든 방향으로 움직인다.
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            # 만약 범위안에 있고 방문한 적이 없다면
            if 0<= ni < N and 0<= nj <N and (ni, nj) not in visited:
                # 이동한 위치의 값이 0이라면 queue와 visited에 추가하고 그 위치의 값을 이전 위치값의 +1 한 값으로 재 설정
                if maze[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited.append((ni, nj))
                    maze[ni][nj] = maze[i][j] + 1
                # 이동한 위치의 값이 0이라면 queue와 visited에 추가하고 ans에 이전 위치의 값을 할당
                elif maze[ni][nj] == 3:
                    queue.append((ni, nj))
                    visited.append((ni, nj))
                    ans = maze[i][j]
        # end위치에 방문했다면 이미 ans의 값을 알고 있으므로 while문 탈출
        if end in visited:
            break
    # 테스트케이스 번호와 ans 출력
    print(f'#{case} {ans}')
