import sys

# 보드의 크기 N, M 체스판의 크기 K
N, M, K = map(int, sys.stdin.readline().split())
# 보드의 상태를 저장하는 배열 board
board = [sys.stdin.readline().rstrip() for _ in range(N)]

B = [[0]*(M+1) for _ in range(N+1)]
W = [[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if (i+j)%2:
            if board[i][j] == 'B':
                B[i][j] = 1 + B[i-1][j] + B[i][j-1] - B[i-1][j-1]
                W[i][j] = 0 + W[i-1][j] + W[i][j-1] - W[i-1][j-1]
            else:
                B[i][j] = 0 + B[i-1][j] + B[i][j-1] - B[i-1][j-1]
                W[i][j] = 1 + W[i-1][j] + W[i][j-1] - W[i-1][j-1]
        else:
            if board[i][j] == 'B':
                B[i][j] = 0 + B[i-1][j] + B[i][j-1] - B[i-1][j-1]
                W[i][j] = 1 + W[i-1][j] + W[i][j-1] - W[i-1][j-1]
            else:
                B[i][j] = 1 + B[i-1][j] + B[i][j-1] - B[i-1][j-1]
                W[i][j] = 0 + W[i-1][j] + W[i][j-1] - W[i-1][j-1]

# 체스판으로 만들기 위해 다시 칠해야하는 정사각형 개수의 최솟값 answer
answer = 1e7

for ii in range(N-K+1):
    for jj in range(M-K+1):
        BB = B[ii+K-1][jj+K-1] - B[ii-1][jj+K-1] - B[ii+K-1][jj-1] + B[ii-1][jj-1]
        WW = W[ii+K-1][jj+K-1] - W[ii-1][jj+K-1] - W[ii+K-1][jj-1] + W[ii-1][jj-1]
        answer = min(answer, BB, WW)

# answer 출력
print(answer)