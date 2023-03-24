import sys

# 도시의 개수 N
N = int(sys.stdin.readline())
# 버스의 개수 M
M = int(sys.stdin.readline())
INF = int(1e9)
# 도시 사이의 정보를 담을 배열 graph
graph = [[INF]*N for _ in range(N)]

for _ in range(M):
    # 버스의 시작 도시 A, 도착도시 B, 한 번 타는데 필요한 비용 C
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A-1][B-1] = min(graph[A-1][B-1], C)

# 플로이드 워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                graph[i][j] == 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# ii번째 줄에 출력하는 jj번째 숫자는 도시 ii에서 jj로 가는데 필요한 최소 비용을 출력
for ii in range(N):
    for jj in range(N):
        if graph[ii][jj] == INF:
            print(0, end=' ')
        else:
            print(graph[ii][jj], end=' ')
    print()