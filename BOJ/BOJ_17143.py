import sys
sys.setrecursionlimit(10**8)

def fish(fj):
    for fi in range(R):
        if board[fi][fj]:
            x = board[fi][fj][2]
            board[fi][fj] = 0
            return x
    return 0

def move():
    return

def next():
    return 

# 격자판의 크기 R, C, 상어의 수 M
R, C, M = map(int, sys.stdin.readline().split())
board = [[0]*C for _ in range(R)]

for _ in range(M):
    # 상어의 정보: 위치(r, c), 속력 s, 이동방향 d, 크기 z
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    r, c = r-1, c-1
    board[r][c] = (s, d, z)