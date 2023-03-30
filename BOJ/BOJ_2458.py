import sys

# 학생들의 수 N, 두 학생 키를 비교한 횟수 M
N, M = map(int, sys.stdin.readline().split())
# 학생의 키 정보를 담을 배열 graph
graph = [[0]*N for _ in range(N)]
# 자신이 키가 몇 번째인지 알 수 있는 학생의 수 answer
answer = 0

for _ in range(M):
    # 번호가 a인 학생이 키가 큰 번호 b인 학생
    a, b = map(int, sys.stdin.readline().split())
    # graph에 정보를 저장
    graph[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            # i의 j의 키의 비교가 가능한 경우
            if graph[i][j] or (graph[i][k] and graph[k][j]):
                graph[i][j] = 1

for ii in range(N):
    cnt = 0
    for jj in range(N):
        # ii보다 jj가 큰 학생 수 + jj보다 ii가 큰 학생 수
        cnt += graph[ii][jj] + graph[jj][ii]
    # ii와 비교가능한 학생 수가 N-1명인 경우 answer 1 증가
    if cnt == N-1:
        answer += 1

# 자신이 키가 몇 번째인지 알 수 있는 학생이 모두 몇 명인지를 출력
print(answer)