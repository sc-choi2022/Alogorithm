import sys

# 학생들의 수 N, 두 학생 키를 비교한 횟수 M
N, M = map(int, sys.stdin.readline().split())
# 학생의 키 정보를 담을 배열 graph
graph = [[0]*N for _ in range(N)]
# 자신이 키가 몇 번째인지 알 수 있는 학생의 수 answer
answer = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] or (graph[i][k] and graph[k][j]):
                graph[i][j] = 1

for ii in range(N):
    height = 0
    for jj in range(N):
        height += graph[ii][jj] + graph[jj][ii]
    if height == N-1:
        answer += 1
print(answer)