import collections
import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, T+1):
    # NxN행렬의 N
    N = int(input())
    # NxN의 방정보를 담은 리스트 room
    room = [list(map(int, input().split())) for _ in range(N)]
    # 이미 방문한 정보를 반영할 리스트 visited
    visited = [[0]*N for _ in range(N)]

    # 최대 방수를 가지는 시작방의 번호들을 담을 리스트 room_n
    room_n = []
    # 최대 방수값 초기화
    length = 0

    # 시작 위치 (i, j)
    for i in range(N):
        for j in range(N):
            # 시작 위치 (i, j)가 이미 방문한 곳이 아니라면
            if visited[i][j] == 0:
                # queue를 생성하고 시작위치를 추가
                queue = collections.deque()
                queue.append((i, j))
                # 방문가능한 방들의 번호를 담을 리스트 able에 방 번호 추가
                able = []
                able.append(room[i][j])
                # 방문한 방의 인덱스에 맞춰 visited에 1 할당
                visited[i][j] = 1
                # bfs를 진행한다.
                while queue:
                    # queue의 가장 앞쪽 값을 si, sj로 설정
                    si, sj = queue.popleft()
                    # 4방향을 움직여서
                    for di, dj in ((0, 1), (1,0), (0,-1),(-1,0)):
                        # si, sj의 위치를 ni, nj로 정한다.
                        ni = si + di
                        nj = sj + dj
                        # ni, nj가 범위 안에 있고 (si,sj) 위치와 (ni,nj)위치의 값의 차가 1이고 (ni,nj)위치를 방문하지 않았다면
                        if 0 <= ni < N and 0<= nj < N and abs(room[si][sj]-room[ni][nj]) == 1 and visited[ni][nj] == 0:
                            # able에 방 번호를 추가하고
                            able.append(room[ni][nj])
                            # visited에 방문을 표시한다.
                            visited[ni][nj] = 1
                            # queue에 (ni,nj)를 추가한다.
                            queue.append((ni, nj))
                # bfs가 끝나고 able의 길이가 기존 length보다 길다면
                if len(able) > length:
                    # length 값을 재설정하고 able의 방번호 중 가장 작은 값만을 room_n 리스트에 담는다.
                    length = len(able)
                    room_n = [min(able)]
                # able의 길이가 기존 값과 동일하다면 room_n 리스트에 able의 가장 작은 값을 추가한다.
                elif len(able) == length:
                    room_n.append(min(able))
    # 테스트케이스와 room_n 리스트의 min값 length값을 출력
    print(f'#{case} {min(room_n)} {length}')