import sys

# 배열의 크기 NxM
N, M = map(int, sys.stdin.readline().split())
square = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(1,M):
        if square[i][j]:
            square[i][j] = square[i][j-1] + 1

for s in square:
    print(*s)
print('==================================')

dp[0] = square[0][::]
for ii in range(N):
    for jj in range(M):
        # if jj == 0 and
        #     dp[ii][jj] = square[ii][jj]
        if not square[ii-1][jj] and not square[ii][jj-1]:
            dp[ii][jj] = square[ii][jj]
        # if square[ii][jj] and dp[ii-1][jj] and dp[ii][jj-1]:
        #     dp[ii][jj] =
for d in dp:
    print(*d)