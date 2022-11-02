import sys

# 목판의 크기 N
N = int(sys.stdin.readline())
# 로봇팔의 움직임 word
word = sys.stdin.readline().strip()

# 판화판 board
board = [['.'] * N for _ in range(N)]
# 시작위치 p1, p2 값을 각각 0, 0로 초기화
p1, p2 = 0, 0

# 로봇팔의 움직임에 따른 좌표값을 담은 딕셔너리 move
move = {'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)}

# word의 각 alphabet
for alphabet in word:
    # 다음 위치 n1, n2
    n1, n2 = p1 + move[alphabet][0], p2 + move[alphabet][1]
    # 격자 바깥으로 나가지 않는 경우 진행
    if 0 <= n1 < N and 0 <= n2 < N:
        if alphabet in ('U', 'D'):
            if board[p1][p2] == '.':
                board[p1][p2] = '|'
            elif board[p1][p2] == '-':
                board[p1][p2] = '+'

            if board[n1][n2] == '.':
                board[n1][n2] = '|'
            elif board[n1][n2] == '-':
                board[n1][n2] = '+'
            p1, p2 = n1, n2
        else:
            if board[p1][p2] == '.':
                board[p1][p2] = '-'
            elif board[p1][p2] == '|':
                board[p1][p2] = '+'
            if board[n1][n2] == '.':
                board[n1][n2] = '-'
            elif board[n1][n2] == '|':
                board[n1][n2] = '+'
            p1, p2 = n1, n2
# 목판 위에 패인 조각도의 혼적을 출력
for b in board:
    print(''.join(b))