import sys

# 먹을 수 있는 최대 사탕개수를 구하는 함수 check
def check():
    cnt = 1
    for ci in range(N):
        # 연속된 열을 확인
        tmpCnt = 1
        for cj in range(1, N):
            if board[ci][cj] == board[ci][cj-1]:
                tmpCnt += 1
            else:
                tmpCnt = 1
            cnt = max(tmpCnt, cnt)
        # 연속된 행을 확인
        tmpCnt = 1
        for cj in range(1, N):
            if board[cj][ci] == board[cj-1][ci]:
                tmpCnt += 1
            else:
                tmpCnt = 1
            cnt = max(tmpCnt, cnt)
    return cnt

# 보드의 크기 N
N = int(sys.stdin.readline())
# 보드의 배열 board
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# 먹을 수 있는 최대 사탕 개수 answer
answer = 0
# 최대 개수에 도달했는지 여부
flag = False

for i in range(N):
    # 최대개수에 도달한 경우 break
    if flag:
        break
    for j in range(N-1):
        # 색이 다른 인접한 두칸인 경우
        if board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if answer == N:
            flag = True
            break
        if i == N-1:
            continue
        # 색이 다른 인접한 두칸인 경우
        if board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        # 최대 개수 여부를 확인하여 flag에 반영
        if answer == N:
            flag = True
            break
# 먹을 수 있는 사탕의 최대 개수를 출력
print(answer)