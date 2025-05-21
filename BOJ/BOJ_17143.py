import sys

# 격자판의 크기 R, C, 상어의 수 M
R, C, M = map(int, sys.stdin.readline().split())
board = [[0]*C for _ in range(R)]

direction = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]

for _ in range(M):
    # 상어의 정보: 위치(r, c), 속력 s, 이동방향 d, 크기 z
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    r, c = r - 1, c - 1
    board[r][c] = (s, d, z)

# 두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
# 낚시왕이 잡은 상어 크기의 합 answer 출력
answer = 0

for j in range(C):
    for i in range(R):
        if board[i][j]:
            answer += board[i][j][2]
            board[i][j] = 0
            break
    move = [[0]*C for _ in range(R)]
    for ii in range(R):
        for jj in range(C):
            # 상어가 있는 경우
            if board[ii][jj]:
                ss, dd, zz = board[ii][jj]

                ni, nj = ii, jj
                # 상하로 움직이는 상어인 경우
                if dd == 0 or dd == 1:
                    cnt = ss%(2*(R-1))
                    while cnt:
                        if ni == 0:
                            dd = 1
                        if ni == R-1:
                            dd = 0
                        ni += direction[dd][0]
                        cnt -= 1
                # 좌우로 움직이는 상어인 경우
                else:
                    cnt = ss%(2*(C-1))
                    while cnt:
                        if nj == 0:
                            dd = 2
                        if nj == C-1:
                            dd = 3
                        nj += direction[dd][1]
                        cnt -= 1
                # 상어 위치 지정
                # 빈칸이 아니거나 새로운 상어가 더 큰 경우
                if move[ni][nj] == 0:
                    move[ni][nj] = (ss, dd, zz)
                elif move[ni][nj][2] < zz:
                    move[ni][nj] = (ss, dd, zz)
    board = move

print(answer)