import sys

# 출발노드를 기준으로 도착노드까지의 거리를 구하는 함수 dfs
def dfs(node, distance):
    # 목표노드에 도착했다면 distance를 출력
    if node == E:
        print(distance)
        return
    for j in range(1, N + 1):
        # node에서 j 사이의 거리가 존재하며 방문하지 않은 노드인 경우
        if dist[node][j] and j not in visited:
            # 방문 표시 후 j노드와 거리를 매개변수로 dfs 실행
            visited.append(j)
            dfs(j, distance + dist[node][j])
            # 방문 표시 제거
            visited.pop()

# 노드의 개수 N, 거리를 알고싶은 노드 쌍의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 노드의 거리정보를 담을 리스트 dist
dist = [[0]*(N + 1) for _ in range(N+1)]
# N-1개의 정보를 dist에 저장
for _ in range(N - 1):
    N1, N2, D = map(int, sys.stdin.readline().split())
    dist[N1][N2], dist[N2][N1] = D, D

# M개의 노드 정보의 거리를 dfs를 통해 출력
for i in range(M):
    visited = []
    S, E = map(int, sys.stdin.readline().split())
    visited.append(S)
    dfs(S, 0)