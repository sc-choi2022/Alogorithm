import sys

def walk():
    for i in range(1, M+1):
        for j in range(1, N+1):
            if roads[i-1][j] == -1 and roads[i][j-1] == -1:
                return
            elif roads[i-1][j] == -1:
                roads[i][j] = roads[i][j-1]
            elif roads[i][j-1] == -1:
                roads[i][j] = roads[i-1][j]
            else:
                roads[i][j] = roads[i-1][j] + roads[i][j-1]

# 도로의 가로 크기 N, 세로 크기 M
N, M = map(int, sys.stdin.readline().split())
# 공사중인 도로의 개수 K
K = int(sys.stdin.readline())
# 도록
roads = [[0]*(N+1) for _ in range(M+1)]

for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    roads[a][b], roads[c][d] = -1, -1
roads[0][0], roads[M][N] = 0, 0

for ii in range(M+1):
    if roads[ii][0] == -1:
        break
    roads[ii][0] = 1
for jj in range(N+1):
    if roads[0][jj] == -1:
        break
    roads[0][jj] = 1
walk()

for road in roads:
    print(*road)
print(roads[M][N])