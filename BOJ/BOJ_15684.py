from collections import deque
import sys

def plus(num):
    global answer
    for pi in range(M):
        ci, cj = lader[pi]
        garo[ci][cj] = 1
        used[pi] = 1
        if sum(used) == num:
            if play():
                return num
        plus(num)
        used[pi] = 0

def play():
    for jj in range(N):
        now = jj
        for ii in range(H):
            if garo[ii][jj]:
                now += 1
            elif now > 0 and garo[ii][now-1]:
                now -= 1
        if now != jj:
            return False
    return True

# 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치 개수 H
N, M, H = map(int, sys.stdin.readline().split())
lader = [(0, 0) for _ in range(M)]
used = [0] * M
garo = [[0]*N for _ in range(H)]
answer = 0

for l in range(M):
    a, b = map(int, sys.stdin.readline().split())
    lader[l] = (a-1, b-1)

for num in range(1, 4):
    plus(num)