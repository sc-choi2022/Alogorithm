import sys

def move(si, sj):
    global sand

    ai, aj = -1, -1

    remain = 0
    for mi in range(-2, 3):
        for mj in range(-2, 3):
            return 


N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

direction = {0: (0, -1), 1:(1, 0), 2:(0, 1), 3:(-1, 0)}
sand = 0