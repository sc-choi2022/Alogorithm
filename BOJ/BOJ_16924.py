import sys

def find():
    for fi in range(1, N):
        for fj in range(1, M):
            if board[fi][fj] == '*':
                while True:
                    continue
    return

# 격자판의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 격자판의 상태 board
board = [sys.stdin.readline().rstrip() for _ in range(N)]

# 필요한 십자가의 수 K
K = 0