import sys
sys.setrecursionlimit(10**8)

def fish():
    return

def move():
    return

R, C, M = map(int, sys.stdin.readline().split())
board = [[0]*C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    