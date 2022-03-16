from collections import deque
import sys
sys.stdin = open('input.txt')

# DFS
for case in range(10):
    # 테스트 케이스 번호
    T = int(input())
    # 미로의 정보를 담은 리스트 maze
    maze = [list(map(int, input())) for _ in range(16)]
    # 방향에 대한 값 di, dj
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 첫 위치 값 s 초기화
    s = [0, 0]
    # 첫 위치를 찾아 s를 재 설정
    for x in range(16):
        for y in range(16):
            if maze[x][y] == 2:
                s = [x, y]
    # 스택과 visited에 첫 위치를 추가
    stack = [s]
    visited = [s]

    # 답 ans 초기화
    ans = 0
    # stack에 무언가 있고 ans값이 0일 때 계속
    while stack and ans == 0:
        # top은 stack의 top을 의미
        top = stack[-1]
        # top의 위치 값을 각각 i, j에 할당
        i = top[0]
        j = top[1]
        # 4개의 방향에 대해
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            # 범위안에 있고 maze[ni][nj]값이 0이고 visited에 없다면 stack과 visited에 [ni, nj]추가
            if 0<= ni < 16 and 0<= nj < 16 and maze[ni][nj] == 0 and [ni, nj] not in visited:
                stack.append([ni, nj])
                visited.append([ni, nj])
                break
            # 범위안에 있고 maze[ni][nj]값이 3이고 visited에 없다면 도착 했으므로 ans에 1 할당
            elif 0<= ni < 16 and 0<= nj < 16 and maze[ni][nj] == 3 and [ni, nj] not in visited:
                ans = 1
                break
        # break문을 만나지 못했다면 stack.pop
        else:
            stack.pop()
    # 테스트 케이스 번호와 답 출력
    print(f'#{T} {ans}')

# BFS
for case in range(10):
    # 테스트 케이스 번호
    T = int(input())
    # 미로의 정보를 담은 리스트 maze
    maze = [list(map(int, input())) for _ in range(16)]
    # 방향에 대한 값 di, dj
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 첫 위치 값 s 초기화
    s = [0, 0]
    # 첫 위치를 찾아 s를 재 설정
    for x in range(16):
        for y in range(16):
            if maze[x][y] == 2:
                s = [x, y]

    # queue과 visited에 첫 위치를 추가
    queue = deque()
    visited = []
    queue.append((s[0], s[1]))
    visited.append((s[0], s[1]))
    # 답 ans 초기화
    ans = 0
    # stack에 무언가 있고 ans값이 0일 때 계속
    while queue and ans == 0:
        # temp는 queue의 첫 값
        temp = queue.popleft()
        # temp의 위치 값을 각각 i, j에 할당
        i = temp[0]
        j = temp[1]
        # 4개의 방향에 대해
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            # 범위안에 있고 maze[ni][nj]값이 0 이고 방문한 적이 없는 위치라면 queue와 visited에 추가
            if 0<= ni < 16 and 0<= nj < 16 and maze[ni][nj] == 0 and (ni, nj) not in visited:
                queue.append((ni, nj))
                visited.append((ni, nj))
            # 범위안에 있고 maze[ni][nj]값이 3 이고 방문한 적이 없는 위치라면 ans에 1 할당
            elif 0<= ni < 16 and 0<= nj < 16 and maze[ni][nj] == 3 and (ni, nj) not in visited:
                ans = 1
    # 테스트 케이스 번호와 답 출력
    print(f'#{T} {ans}')