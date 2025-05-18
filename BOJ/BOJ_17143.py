import sys

# 격자판의 크기 R, C, 상어의 수 M
R, C, M = map(int, sys.stdin.readline().split())
board = [[0]*C for _ in range(R)]

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for _ in range(M):
    # 상어의 정보: 위치(r, c), 속력 s, 이동방향 d, 크기 z
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    r, c = r - 1, c - 1
    board[r][c] = (s, d, z)

# 두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
# 낚시왕이 잡은 상어 크기의 합 answer 출력
answer = 0

for i in range(C):
    for j in range(R):
        if board[j][i]:
            answer += board[j][i][2]
            board[j][i] = 0
            break