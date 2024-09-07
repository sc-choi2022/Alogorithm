from collections import deque
import sys

# 테스트 케이스의 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 그리드의 높이 H, 너비 W
    H, W = map(int, sys.stdin.readline().split())
    # 양들을 저장하는 배열 gird
    grid = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
    visit = [[0] * W for _ in range(H)]
    # 양의 무리의 개수 answer
    answer = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visit[i][j]:
                answer += 1
                queue = deque([(i, j)])
                while queue:
                    ci, cj = queue.popleft()

                    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '#' and not visit[ni][nj]:
                            queue.append((ni, nj))
                            visit[ni][nj] = 1
    # 양 무리의 개수를 출력
    print(answer)