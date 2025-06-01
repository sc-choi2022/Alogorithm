import sys

# 낚시왕이 낚시
def fish(fj):
    global answer

    for fi in range(R):
        if board[fi][fj]:
            answer += board[fi][fj][2]
            board[fi][fj] = 0
            return

# 상어가 이동
def move():
    global board
    tmp = [[0]*C for _ in range(R)]

    for mi in range(R):
        for mj in range(C):
            if board[mi][mj]:
                # 상어의 속력 ms, 이동방향 md, 크기 mm
                ms, md, mm = board[mi][mj]
                ni, nj = mi, mj

                # 방향이 위, 아래인 경우
                if md == 0 or md == 1:
                    cnt = ms%(2*(R-1))
                    while cnt:
                        if ni == 0:
                            md = 1
                        elif ni == R-1:
                            md = 0
                        ni += direction[md][0]
                        cnt -= 1
                # 방향이 왼쪽, 오른쪽인 경우
                else:
                    cnt = ms%(2*(C-1))
                    while cnt:
                        if nj == 0:
                            md = 2
                        elif nj == C-1:
                            md = 3
                        nj += direction[md][1]
                        cnt -= 1
                # 상어 위치 지정
                # 빈칸이 아니거나 새로운 상어가 더 큰 경우
                if tmp[ni][nj] == 0 or tmp[ni][nj][2] < mm:
                    tmp[ni][nj] = (ms, md, mm)

    # 상어의 위치 정보 갱신
    board = tmp

# 격자판의 크기 R, C, 상어의 수 M
R, C, M = map(int, sys.stdin.readline().split())

# 격자판 board
board = [[0]*C for _ in range(R)]

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for _ in range(M):
    # 상어의 정보: 위치(r, c), 속력 s, 이동방향 d, 크기 z
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    board[r-1][c-1] = (s, d-1, z)

# 두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
# 낚시왕이 잡은 상어 크기의 합 answer 출력
answer = 0

for f in range(C):
    fish(f)
    move()

# 낚시왕이 잡은 상어 크기의 합을 출력
print(answer)