import sys

# 배열의 크기 N, M 회전시킨 결과 R
N, M, R = map(int, sys.stdin.readline().split())
# 배열 graph
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(R):
    for n in range(min(N, M)//2):
        # 이동의 시작 위치 좌표
        si, sj = n, n
        # 다음 위치에 저장하는 이전 위치 값 prev
        # tmp는 저장되는 위치의 값 tmp
        prev = graph[si][sj]

        for i in range(n+1, N-n):
            tmp = graph[i][sj]
            graph[i][sj] = prev
            prev = tmp
            si = i

        for j in range(n+1, M-n):
            tmp = graph[si][j]
            graph[si][j] = prev
            prev = tmp
            sj = j

        for ii in range(N-n-2, n-1, -1):
            tmp = graph[ii][sj]
            graph[ii][sj] = prev
            prev = tmp
            si = ii

        for jj in range(M-n-2, n-1, -1):
            tmp = graph[si][jj]
            graph[si][jj] = prev
            prev = tmp
            sj = jj

# 어진 배열을 R번 회전시킨 결과를 출력
for g in graph:
    print(*g)