import sys

def dfs(cnt, board1):
    global answer
    if cnt == 5:
        for b1 in board1:
            answer = max(answer, max(b1))
        return
    for d in range(4):
        dfs(cnt+1, move(d, board1))

def move(d, board2):
    tmp = [[0]*N for _ in range(N)]
    # 0: 위 1: 오른쪽 2: 아래 3: 왼쪽
    # 0: 위
    if d == 0:
        for j in range(N):
            idx, number = 0, -1
            for i in range(N):
                if board2[i][j]:
                    # 새로운 수를 받을 수 있는 경우
                    if number == -1:
                        number = board2[i][j]
                    # 두 수를 더할 수 있는 경우
                    elif number == board2[i][j]:
                        tmp[idx][j] = 2*number
                        number = -1
                        idx += 1
                    # 두 수가 다른 경우
                    else:
                        tmp[idx][j] = number
                        number = board2[i][j]
                        idx += 1
            if number != -1:
                tmp[idx][j] = number
    # 1: 오른쪽
    elif d == 1:
        for i in range(N):
            idx, number = N-1, -1
            for j in range(N-1, -1, -1):
                if board2[i][j]:
                    # 새로운 수를 받을 수 있는 경우
                    if number == -1:
                        number = board2[i][j]
                    # 두 수를 더할 수 있는 경우
                    elif number == board2[i][j]:
                        tmp[i][idx] = 2*number
                        number = -1
                        idx -= 1
                    # 두 수가 다른 경우
                    else:
                        tmp[i][idx] = number
                        number = board2[i][j]
                        idx -= 1
            if number != -1:
                tmp[i][idx] = number
    # 2: 아래
    elif d == 2:
        for j in range(N):
            idx, number = N-1, -1
            for i in range(N-1, -1, -1):
                if board2[i][j]:
                    # 새로운 수를 받을 수 있는 경우
                    if number == -1:
                        number = board2[i][j]
                    # 두 수를 더할 수 있는 경우
                    elif number == board2[i][j]:
                        tmp[idx][j] = 2*number
                        number = -1
                        idx -= 1
                    # 두 수가 다른 경우
                    else:
                        tmp[idx][j] = number
                        number = board2[i][j]
                        idx -= 1
            if number != -1:
                tmp[idx][j] = number
    # 3: 왼쪽
    else:
        for i in range(N):
            idx, number = 0, -1
            for j in range(N):
                if board2[i][j]:
                    # 새로운 수를 받을 수 있는 경우
                    if number == -1:
                        number = board2[i][j]
                    # 두 수를 더할 수 있는 경우
                    elif number == board2[i][j]:
                        tmp[i][idx] = 2*number
                        number = -1
                        idx += 1
                    # 두 수가 다른 경우
                    else:
                        tmp[i][idx] = number
                        number = board2[i][j]
                        idx += 1
            if number != -1:
                tmp[i][idx] = number
    return tmp

# 보드의 크기 N
N = int(sys.stdin.readline())
# 블럭의 초기상태를 저장하는 배열 board
boards = [[] for _ in range(N)]
# 이동시켜서 얻을 수 있는 가장 큰 블록 answer
answer = 0
for b in range(N):
    boards[b] = list(map(int, sys.stdin.readline().split()))
    answer = max(answer, max(boards[b]))
dfs(0, boards)
print(answer)