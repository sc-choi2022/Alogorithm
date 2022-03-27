from collections import deque

# 컴퓨터의 수 N
N = int(input())
# 연결되어 있는 컴퓨터 쌍의 개수
M = int(input())

# 컴퓨터의 연결 정보를 담을 리스트 arr
arr = [[0] * (N + 1) for _ in range(N + 1)]
# M개의 연결정보를 arr에 반영하기 위한 for문
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
# queue와 visited를 만들고 1번 컴퓨터의 정보를 추가한다.
queue = deque()
queue.append(1)
visited = [1]

# BFS
while queue:
    temp = queue.popleft()
    # temp 컴퓨터에 연결된 모든 정보에 대해 연결여부와 방문여부를 확인하고 queue에 추가
    for i in range(N + 1):
        if arr[temp][i] == 1 and i not in visited:
            queue.append(i)
            visited.append(i)
# 1번 컴퓨터를 제외하고 1번 컴퓨터와 연결되어 감염되는 모든 컴퓨터의 수를 출력한다.
print(len(visited) - 1)