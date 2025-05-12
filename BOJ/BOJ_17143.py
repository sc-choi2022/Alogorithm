import sys
sys.setrecursionlimit(10**8)

# 낚시
def fish():
    for fj in range(C):
    return 0

# 상어 이동
def move():
    global board
    tmp = [[0]*C for _ in range(R)]
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

# 낚시왕이 잡은 상어 크기의 합 answer 출력
answer = 0

for f in range(C):
    answer += fish(f)
    move()

print(answer)