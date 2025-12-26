from copy import deepcopy
import sys

def find():
    cnt = 0
    for fi in range(1, N):
        for fj in range(1, M):
            if board[fi][fj] == '*':
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = fi+di, fj+dj
    return

# 격자판의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 격자판의 상태 board
board = [sys.stdin.readline().rstrip() for _ in range(N)]
tmp = deepcopy(board)
visite = [[0]*N for _ in range(M)]

# 필요한 십자가의 수 K
K = 0

direct = {0:(0, 1), 1:(1, 0), 2:(0, -1), 3:(-1, 0)}