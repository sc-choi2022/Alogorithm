import sys
sys.setrecursionlimit(10**8)

# 낚시왕이 낚시
def fish(fj):
    for fi in range(R):
        if board[fi][fj]:
            mass = board[fi][fj][2]
            board[fi][fj] = []
            return mass
# 상어가 이동
def move():
    tmp = [[[] for _ in range(C)] for _ in range(R)]

    for mi in range(R):
        for mj in range(C):
            if board[mi][mj]:
                ms, md, mz = board[mi][mj]
                si, sj = mi, mj
                di, dj = direction[md]
                while True:
                    # 배수 확인 필요
                    ni, nj = si+ms*di, sj+ms*dj
                    if 0 <= ni < R and 0 <= nj < C:
                        
    return

# 격자판의 크기 R, C, 상어의 수 M
R, C, M = map(int, sys.stdin.readline().split())
# 격자판 board
board = [[[] for _ in range(C)] for _ in range(R)]

direction = {1:(-1, 0), 2:(1, 0), 3:(0, 1), 4:(0, -1)}

for _ in range(M):
    # 상어의 정보: 위치(r, c), 속력 s, 이동방향 d, 크기 z
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    r, c = r-1, c-1
    board[r][c] = (s, d, z)

# 두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.

# 낚시왕이 잡은 상어 크기의 합 answer 출력
answer = 0

for f in range(C):
    answer += fish(f)
    move()

print(answer)