from collections import deque
import sys

# queue를 활용한 bfs
def bfs():
    # deque를 활용하여 queue를 선언
    queue = deque()
    # queue에는 위치 ci, cj, 사용할 수 있는 말의 움직임 수 K, 움직인 수 ans를 담는다.
    queue.append((0, 0, K, 0))
    # visited는 list로 선언하면 시간초과가 발생한다.
    visited = set()
    visited.add((0, 0, K))

    while queue:
        # queue.popleft()를 통해 ci, cj, cnt, answer값 각 변수에 담아 준다.
        ci, cj, cnt, answer = queue.popleft()
        # 만약 도착위치에 도착했다면 answer를 return
        if (ci, cj) == (H - 1, W - 1):
            return answer
        # 원숭이의 움직임으로 갈 수 있는 위치를 위한 for문
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            # 현재 위치 ci, cj, 다음 위치 ni, nj
            ni, nj = ci + di, cj + dj
            # ni, nj가 범위 안에 존재하고 (ni,nj, cnt)가 visited에 있어 방문한 정보가 아니며 (ni,nj) 위치에 벽이 없다면
            if 0 <= ni < H and 0 <= nj < W and (ni, nj, cnt) not in visited and location[ni][nj] != 1:
                # 다음 위치와 사용할 수 있는 말을 움직임, 움직인 수 1 증가하여 queue에 추가한다.
                queue.append((ni, nj, cnt, answer + 1))
                # visited에 (ni, nj, cnt)를 추가
                visited.add((ni, nj, cnt))
        # 말의 움직임을 할 수 있는 상황이라면
        if cnt != 0:
            # 말의 움직임으로 갈 수 있는 위치를 위한 for문
            for di, dj in (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1):
                # 현재 위치 ci, cj, 다음 위치 ni, nj
                ni, nj = ci + di, cj + dj
                # ni, nj가 범위 안에 존재하고 (ni,nj, cnt -1)가 visited에 있어 방문한 정보가 아니며 (ni,nj) 위치에 벽이 없다면
                # visited를 확인할 때에 말의 움직임이기 때문에 -1을 해주고 존재 여부를 확인해주어야한다.
                if 0 <= ni < H and 0 <= nj < W and (ni, nj, cnt - 1) not in visited and location[ni][nj] != 1:
                    # 다음 위치와 사용할 수 있는 말을 움직임 1 감소, 움직인 수로 queue에 추가한다.
                    queue.append((ni, nj, cnt - 1, answer + 1))
                    # visited에 (ni, nj, cnt - 1)를 추가
                    visited.add((ni, nj, cnt - 1))
    # 만약 도착할 수 없다면 return -1
    return -1

# 원숭이가 따라할 수 있는 횟수 K
K = int(sys.stdin.readline())

# 가로 W, 세로 H
W, H = map(int, sys.stdin.readline().split())
# 격자판의 정보를 담을 리스트 location
location = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
# bfs를 실행하고 return 값을 출력
print(bfs())