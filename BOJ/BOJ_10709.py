import sys
# 현재 구름의 위치에서 이후 구름의 움직음을 cloud에 저장하는 함수 move
def move(i, j):
    for mj in range(j+1, W):
        # 현재 구름이 있는 경우
        if sky[i][mj] == 'c':
            return
        # 구름이 이동할 수 있는 경우
        if sky[i][mj] == '.' and cloud[i][mj] == -1:
            cloud[i][mj] = cloud[i][mj-1] + 1

# 남북방향 H킬로미터, 동서방향 W킬로미터
H, W = map(int, sys.stdin.readline().split())
# 하늘의 구름 위치를 저장하는 배열 sky
sky = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
cloud = [[-1]*W for _ in range(H)]

for si in range(H):
    for sj in range(W):
        # 현재 구름이 있는 경우 cloud에 반영 후 move
        if sky[si][sj] == 'c':
            cloud[si][sj] = 0
            move(si, sj)
# H 행으로, 각 행에는 공백으로 구분된 W 개의 정수를 출력
for ii in range(H):
    print(*cloud[ii])