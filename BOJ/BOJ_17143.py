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
    global board
    tmp = [[0]*C for _ in range(R)]

    for mi in range(R):
        for mj in range(C):
            if board[mi][mj]:
                ni, nj, nd = next(mi, mj, tmp[mi][mj][0], tmp[mi][mj][1])
                if tmp[ni][nj]:
                    return
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

answer = 0

for f in range(C):
    answer += fish(f)
    move()

print(answer)