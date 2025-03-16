import sys

# 보드의 크기 N, M 체스판의 크기 K
N, M, K = map(int, sys.stdin.readline().split())
# 보드의 상태를 저장하는 배열 board
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

answer = 0