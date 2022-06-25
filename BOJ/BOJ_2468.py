from collections import deque
import sys

def bfs(i, j, height):
    queue = deque()
    queue.append((i, j))

    while queue:
        ci, cj = queue.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and area[ni][nj] > height and status[ni][nj] == 0:
                queue.append((ni, nj))
                status[ni][nj] = 1
    return
# 2차원 배열의 행과 열의 수 N
N = int(sys.stdin.readline())
# 높이의 정보를 담을 리스트 area
area = [0] * N
# 가장 높은 높이를 담을 변수 maximum의 값을 0으로 초기화
maximum = 0

for n in range(N):
    # N개의 줄로 주어지는 정보를 변수 line에 담는다.
    line = list(map(int, sys.stdin.readline().split()))
    # 각 행의 최대값을 maximum값과 비교하여 큰 값을 maximum에 할당
    maximum = max(maximum, max(line))
    # line을 area의 n번째에 할당
    area[n] = line

# 안전영역의 개수를 담을 변수 ans의 값을 0으로 초기화
ans = 0
# maximum 높이까지 비가 왔을 때를 가정하기 위한 for문
for height in range(maximum + 1):
    # 각 height에 따라 상황을 표시할 행렬 status
    status = [[0]*N for _ in range(N)]
    # 영역을 시작한 위치를 담아 안전영역의 수를 구하는데 활용할 행렬 left
    left = []
    # area의 모든 위치를 확인하기 위한 이중 for문
    for i in range(N):
        for j in range(N):
            # area[i][j]가 height보다 큰 값으로 물에 잠기지 않고 status[i][j]가 0으로 안전영역으로 이미 확인한 곳이 아니라면
            if area[i][j] > height and status[i][j] == 0:
                # 위치정보 (i, j)와 높이 정보 height를 매개변수로 bfs를 실행
                bfs(i, j, height)
                # left에 위치정보(i,j)를 추가한다.
                left.append((i, j))
    # 출력할 답 ans에 ans와 left의 길이 중 큰 값을 할당한다.
    ans = max(ans, len(left))
# ans를 출력한다.
print(ans)