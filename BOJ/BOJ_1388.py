from collections import deque

def bfs(a, b):
    queue = deque([(a, b)])
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == '-':
            graph[x][y] = '1'
            if y + 1 < M and graph[x][y + 1] == '-':
                queue.append((x, y + 1))
        elif graph[x][y] == '|':
            graph[x][y] = '1'
            if x + 1 < N and graph[x + 1][y] == '|':
                queue.append((x + 1, y))
N, M = map(int, input().split())
cnt = 0
graph = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] != '1':
            bfs(i, j)
            cnt += 1
print(cnt)