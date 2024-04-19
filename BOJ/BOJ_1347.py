import sys

# 적은 내용의 길이 N
N = int(sys.stdin.readline())
# 적은 내용 memo
memo = sys.stdin.readline().rstrip()
# 움직이는 곳을 확인하는 배열 miro
miro = [['#']*(2*N+1) for _ in range(2*N+1)]

# 범위를 정하는 기준 (i1, j1), (i2, j2)
i1, j1, i2, j2 = N, N, N, N
# 현재 위치 si, sj
si, sj = N, N
miro[si][sj] = '.'

# 방향을 저장하는 딕셔너리 direction
direction = {0: (0, 1), 1:(1, 0), 2:(0, -1), 3:(-1, 0)}
# 현재의 방향 D
D = 1

for order in memo:
    # L과 R의 경우 움직임에 따라 방향 변경
    if order == 'L':
        D = (D-1)%4
    elif order == 'R':
        D = (D+1)%4
    # 앞으로 움직이는 경우
    else:
        si += direction[D][0]
        sj += direction[D][1]
        # 미로 지도에 반영
        miro[si][sj] = '.'
        # 범위를 재설정
        i1, j1 = min(i1, si), min(j1, sj)
        i2, j2 = max(i2, si), max(j2, sj)

# 미로 지도를 출력
for i in range(i1, i2+1):
    print(''.join(miro[i][j1:j2+1]))