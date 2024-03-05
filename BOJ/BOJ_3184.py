from collections import deque
import sys

def bfs(si, sj):
    global sheep, wolf
    queue = deque([(si, sj)])
    # 현재 영역에서의 양의 개수 S, 늑대의 개수 W
    S, W = 0, 0
    if graph[si][sj] == 'o':
        S += 1
    elif graph[si][sj] == 'v':
        W += 1

    while queue:
        ci, cj = queue.popleft()
        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] != '#' and not visit[ni][nj]:
                if graph[ni][nj] == 'o':
                    S += 1
                elif graph[ni][nj] == 'v':
                    W += 1
                visit[ni][nj] = 1
                queue.append((ni, nj))
    if S > W:
        sheep += S
    else:
        wolf += W
# 두 정수 R, C
R, C = map(int, sys.stdin.readline().split())
# 마당의 구조를 저장하는 배열 graph
graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
# 영역의 확인 여부를 저장하는 배열 visit
visit = [[0]*C for _ in range(R)]
# 영역 확인 후 남은 양의 개수 sheep, 늑대의 개수 wolf
sheep, wolf = 0, 0

for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and not visit[i][j]:
            visit[i][j] = 1
            bfs(i, j)

# 아침까지 살아있는 양과 늑대의 수를 의미하는 두 정수를 출력
print(sheep, wolf)