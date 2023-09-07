from copy import deepcopy
import sys

# 격자판의 크기 R, C, 폭탄 설치 후 확인 시간 N초
R, C, N = map(int, sys.stdin.readline().split())
# 폭탄의 초기 정보 info
info = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
# 폭탄의 시간을 저장하는 배열 bombs
bombs = [[0]*C for _ in range(R)]
for bi in range(R):
    for bj in range(C):
        if info[bi][bj] == 'O':
            bombs[bi][bj] = 2

for i in range(N-1):
    # 폭탄의 위치를 deepcopy한 배열 tmp
    tmp = deepcopy(bombs)
    # 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치
    if not i%2:
        for i in range(R):
            for j in range(C):
                if not bombs[i][j]:
                    tmp[i][j] = 2
                else:
                    tmp[i][j] = bombs[i][j] - 1
    # 3초가 지난 폭탄이 칸을 파괴
    else:
        for i in range(R):
            for j in range(C):
                if bombs[i][j] == 1:
                    tmp[i][j] = 0
                    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < R and 0 <= nj < C:
                            tmp[ni][nj] = 0
    # 폭탄의 상태 반영
    bombs = tmp
# bombs의 정보에 따라
# R개의 줄에 N초가 지난 후의 격자판 상태를 출력
for pi in range(R):
    for pj in range(C):
        if bombs[pi][pj]:
            print('O', end='')
        else:
            print('.', end='')
    print()