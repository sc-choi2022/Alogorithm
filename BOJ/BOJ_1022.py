import sys

def func():
    si, sj = L, L
    graph[si][sj] = 1
    cnt = 1
    while cnt < len(graph):
        if cnt%2:
            for di, dj in (0, 1), (-1, 0):
                for _ in range(cnt):
                    ni, nj = si + di, sj + dj
                    graph[ni][nj] = graph[si][sj] + 1
                    si, sj = ni, nj
        else:
            for di, dj in (0, -1), (1, 0):
                for _ in range(cnt):
                    ni, nj = si + di, sj + dj
                    graph[ni][nj] = graph[si][sj] + 1
                    si, sj = ni, nj
        cnt += 1
    if cnt%2:
        for _ in range(cnt-1):
            nj = sj + 1
            graph[ni][nj] = graph[si][sj] + 1
            sj = nj
    else:
        for _ in range(cnt-1):
            nj = sj - 1
            graph[ni][nj] = graph[si][sj] + 1
            sj = nj


# R1, C1, R2, C2
R1, C1, R2, C2 = map(int, sys.stdin.readline().split())

L = max(abs(R1), abs(R2), abs(C1), abs(C2))
graph = [[0]*(2*L+1) for _ in range(2*L+1)]
func()

length = len(str(max(graph[R1+L][C1+L], graph[R1+L][C2+L], graph[R2+L][C1+L], graph[R2+L][C2+L])))

for i in range(R1+L, R2+L+1):
    for j in range(C1+L, C2+L+1):
        N = length - len(str(graph[i][j]))
        print(' '*N + str(graph[i][j]), end=' ')
    print()