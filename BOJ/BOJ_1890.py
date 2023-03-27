import sys

# 판의 크기 N
N = int(sys.stdin.readline())
# NxN의 게임판 game
game = [lit(map(int, sys.stdin.readline().split())) for _ in range(N)]

