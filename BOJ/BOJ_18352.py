from collections import deque

# 도시의 수 N, 도로의 수 M, 최단거리의 기준 K, 시작 노드 X
N, M, K, X = map(int, input().split())

# 도시의 시작과 도착정보를 담을 리스트 city
city = [[] for _ in range(N + 1)]
# 도시의 방문까지의 거리를 담을 visited
visited = [-1]*(N + 1)
# 시작 도칙의 방문까지의 거리 0을 인덱스 X에 할당
visited[X] = 0
# deque를 활용하여 queue를 생성
queue = deque()
# 첫 위치를 queue에 추가
queue.append(X)

# M개의 방문정보를 city에 반영
for _ in range(M):
    start, end = map(int, input().split())
    city[start].append(end)

# quque에 값이 있을 때까지 반복
while queue:
    start = queue.popleft()
    # 시작위치의 값이 city[start]의 모든 값을 확인한다.
    for end in city[start]:
        # 미방문한 도시라면
        if visited[end] == -1:
            # 도시까지의 거리를 visited에 반영하고 queue에 그 도시를 추가한다.
            visited[end] = visited[start] + 1
            queue.append(end)

# visited의 값중 거리가 K인 경우 도시의 번호를 출력한다.
for i in range(1, N+1):
    if visited[i] == K:
        print(i)
# 위 for문에서 출력되지 않았다면 K가 없는 것이므로 -1 출력
if K not in visited:
    print(-1)