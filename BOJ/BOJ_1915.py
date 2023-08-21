import sys

# 배열의 크기 NxM
N, M = map(int, sys.stdin.readline().split())
square = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for i in range(1, N):
    for j in range(1, M):
        if square[i][j]:
            square[i][j] = square[i][j-1] + 1

