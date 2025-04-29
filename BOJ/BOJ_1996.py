import sys

# 지뢰찾기의 크기 N
N = int(sys.stdin.readline())
# 지뢰찾기의 지도 zido
zido = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# 출력하는 지뢰 찾기 map answer
answer = [[0]*N for _ in range(N)]

for zi in range(N):
    for zj in range(N):
        if zido[zi][zj] != '.':
            zido[zi][zj] = int(zido[zi][zj])
            answer[zi][zj] = '*'
            for di, dj in (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1):
                ni, nj = zi+di, zj+dj
                if 0 <= ni < N and 0 <= nj < N and answer[ni][nj] != '*':
                    answer[ni][nj] += zido[zi][zj]

# 지뢰는 '*'로 출력하며. 10 이상인 경우는 'M'(Many)으로 출력
for ai in range(N):
    for aj in range(N):
        if answer[ai][aj] != '*' and answer[ai][aj] >= 10:
            answer[ai][aj] = 'M'
        print(answer[ai][aj], end='')
    print()