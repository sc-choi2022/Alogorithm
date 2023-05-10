import sys

def place():
    global air1, air2
    for pi in range(R):
        if PM[pi][0] == -1:
            air1 = pi
            air2 = pi + 1
            return

def spread():
    tmp = [[0]*C for _ in range(R)]

    for di in range(R):
        for dj in range(C):
            if PM[di][dj] != 0 and PM[di][dj] != -1:
                cnt = 0
                for dii, djj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = di + dii, dj + djj
                    if 0 <= ni < R and 0 <= nj < C and PM[ni][nj] != -1:
                        cnt += 1
                        tmp[ni][nj] += PM[di][dj]//5
                tmp[di][dj] += PM[di][dj] - PM[di][dj]//5 * cnt
    tmp[air1][0], tmp[air2][0] = -1, -1
    return tmp

def clean():
    for i in range(air1-1, 0, -1):
        PM[i][0] = PM[i-1][0]
    for j in range(C-1):
        PM[0][j] = PM[0][j+1]
    for ii in range(air1):
        PM[ii][C-1] = PM[ii+1][C-1]
    for jj in range(C-1, 1, -1):
        PM[air1][jj] = PM[air1][jj-1]
    PM[air1][1] = 0

    for ri in range(air2+1, R-1):
        PM[ri][0] = PM[ri+1][0]
    for rj in range(C-1):
        PM[R-1][rj] = PM[R-1][rj+1]
    for rii in range(R-1, air2, -1):
        PM[rii][C-1] = PM[rii-1][C-1]
    for rjj in range(C-1, 0, -1):
        PM[air2][rjj] = PM[air2][rjj-1]
    PM[air2][1] = 0

# R×C인 격자판의 T초
R, C, T = map(int, sys.stdin.readline().split())
# 미세먼지 상태를 담을 배열 PM
PM = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 공기청정기의 위치
air1, air2 = 0, 0
# 공기청정기의 위치를 저장하는 함수 place
place()

for _ in range(T):
    # 미세먼지의 확산하는 함수 spread의 반환값을 PM으로 저장
    PM = spread()
    # 공기청정기를 작동하는 함수 clean
    clean()
# T초가 지난 후 구사과 방에 남아있는 미세먼지의 양
answer = 0
for P in PM:
    answer += sum(P)
# 미세먼지의 양을 출력
print(answer+2)