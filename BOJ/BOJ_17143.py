import sys

# 낚시왕이 낚시
def fish(fj):
    for fi in range(R):
        if board[fi][fj]:
            mass = board[fi][fj][2]
            board[fi][fj] = []
            return mass
    return 0

# 상어가 이동
def move():
    global board
    tmp = [[[] for _ in range(C)] for _ in range(R)]

    for mi in range(R):
        for mj in range(C):
            if board[mi][mj]:
                # 상어의 속력 ms, 이동방향 md, 크기 mm
                ms, md, mm = board[mi][mj]
                # 상어의 시작 위치 (si, sj), 이동방향 (di, dj)
                si, sj = mi, mj
                di, dj = direction[md]
                # 상어의 움직임 횟수 cnt
                cnt = 0

                while cnt != ms:
                    ni, nj = si+di, sj+dj

                    if 0 <= ni < R and 0 <= nj < C:
                        cnt += 1
                        si, sj = ni, nj
                    else:
                        di *= -1
                        dj *= -1
                if tmp[si][sj] and mj < tmp[si][sj][2]:
                    continue
                else:
                    tmp[si][sj] = (ms, number[(di, dj)], mm)
    board = tmp

# 격자판의 크기 R, C, 상어의 수 M
R, C, M = map(int, sys.stdin.readline().split())

if M:
    # 격자판 board
    board = [[[] for _ in range(C)] for _ in range(R)]

    direction = {1:(-1, 0), 2:(1, 0), 3:(0, 1), 4:(0, -1)}
    number = {(-1, 0):1, (1, 0):2, (0, 1):3, (0, -1):4}

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
else:
    print(0)