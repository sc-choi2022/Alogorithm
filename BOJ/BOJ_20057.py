import sys

N = int(sys.stdin.readline())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

direction = {0: (0, -1), 1:(1, 0), 2:(0, 1), 3:(-1, 0)}