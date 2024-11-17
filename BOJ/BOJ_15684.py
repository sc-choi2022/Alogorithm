import sys

def plus(num):
    for pi in range(M):
        ci, cj = lader[pi]
        garo[ci][cj] = 1
        used[pi] = 1
        if sum(used) == num:
            play()
        


def play():
    global flag

    for ii in range(H):
        for jj in range(N):
            continue

# 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치 개수 H
N, M, H = map(int, sys.stdin.readline().split())
lader = [(0, 0) for _ in range(M)]
used = [0] * M
garo = [[0]*N for _ in range(H)]

for l in range(M):
    a, b = map(int, sys.stdin.readline().split())
    lader[l] = (a-1, b-1)

for num in range(1, 4):
    plus(num)