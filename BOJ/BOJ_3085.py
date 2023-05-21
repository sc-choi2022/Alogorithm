import sys

def check():
    cnt = 1
    for ci in range(1, N):
        tmpCnt = 1
        for cj in range(1, N):
            if board[ci][cj] == board[ci][cj-1]:
                cnt += 1
            else:
                cnt = 1
            cnt = max(tmpCnt, cnt)
        tmpCnt = 1
        for cj in range(1, N):
            if board[cj][ci] == board[cj-1][ci]:
                cnt += 1
            else:
                cnt = 1
            cnt = max(tmpCnt, cnt)
    return cnt

# 보드의 크기 N
N = int(sys.stdin.readline())
# 보드의 배열 board
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            if board[i][j] != board[i][j+1]:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                answer = max(answer, check())
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        if i + 1 < N:
            if board[i][j] != board[i+1][j]:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                answer = max(answer, check())
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
print(answer)