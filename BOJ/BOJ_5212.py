from copy import deepcopy
import sys

# 지도의 크기 R, C
R, C = map(int, sys.stdin.readline().split())
# 지도의 정보를 저장하는 배열 zido
zido = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
# 50년이 지난 후 지도 next
next = deepcopy(zido)
# 50년이 지난 후 지도의 범위 (pi, pj), (pii, pjj)
pi, pii, pj, pjj = R-1, 0, C-1, 0

for i in range(R):
    for j in range(C):
        # 섬인 경우
        if zido[i][j] == 'X':
            # 섬의 위치 (i, j) 인접한 바다의 개수 tmp
            tmp = 0
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    if zido[ni][nj] == '.':
                        tmp += 1
                else:
                    tmp += 1
            # 현재 땅이 잠기는 경우
            if tmp > 2:
                next[i][j] = '.'
            # 현재 땅이 남는 경우 50년이 지난 후 섬의 범위 재설정
            else:
                pi = min(pi, i)
                pii = max(pii, i)
                pj = min(pj, j)
                pjj = max(pjj, j)

# 50년 후의 지도를 출력
for p in range(pi, pii+1):
    print(''.join(next[p][pj:pjj+1]))