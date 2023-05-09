import sys

def place():
    global air1, air2
    for pi in range(R):
        for pj in range(C):
            if PM[pi][pj] == -1:
                air1 = (pi, pj)
                air2 = (pi+1, pj)
                return

def spread():
    dust = []
    for si in range(C):
        for sj in range(R):
            if PM[si][sj] > 0:
                dust.append((si, sj))

    for di, dj in dust:
        cnt = 0
        for dii, djj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = di + dii, di + djj
            if 0 <= ni < R and 0 <= nj < C and PM[ni][nj] != -1:
                cnt += 1
                PM[ni][nj] += int(PM[di][dj]//5)
        PM[di][dj] -= int(PM[di][dj]//5) * cnt

def clear():
    for i in range(air1[0]-1, 0, -1):
        PM[i][0] = PM[i-1][0]
    for j in range(C-2):
        PM[0][j] = PM[0][j+1]
    for ii in range(air1[0]-1):
        PM[ii][C-1] = PM[ii+1][C-1]
    for jj in range(C-1, 1, -1):
        PM[air1[0]][jj] = PM[air1[0]][jj-1]

    for ri in range(air2[0])

# R×C인 격자판의 T초
R, C, T = map(int, sys.stdin.readline().split())
# 미세먼지 상태를 담을 배열 PM
PM = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 공기청정기의 위치
air1, air2 = (0, 0),  (0, 0)
place()

for _ in range(T):
    spread()
    clean()