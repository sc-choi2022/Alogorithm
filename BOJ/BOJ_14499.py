import sys

# 지도의 세로 크기 N, 가로 크기 M, 주사위를 놓는 좌표 x, y, 명령의 개수 K
N, M, x, y, K = map(int, sys.stdin.readline().split())
# 지도의 수를 저장하는 배열 numbers
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 주사위 윗면,  바닥면의 숫자를 저장하는 변수 top, bottom
top, bottom = 0, 0
# 주사위 옆면의 숫자를 저장하는 배열 dice
dice = [0, 0, 0, 0]
# 명령에 따라 이동하는 방향을 저장하는 딕셔너리 direct
direct = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

# K개의 명령을 저장하는 배열 orders
orders = list(map(int, sys.stdin.readline().split()))
for order in orders:
    di, dj = direct[order]
    ni, nj = x + di, y + dj
    # (ni, nj)가 지도를 벗어나지 않는 경우
    if 0 <= ni < N and 0 <= nj < M:
        if order == 1:
            top, bottom, dice[0], dice[2] = dice[0], dice[2], bottom, top
        elif order == 2:
            top, bottom, dice[0], dice[2] = dice[2], dice[0], top, bottom
        elif order == 3:
            top, bottom, dice[1], dice[3] = dice[1], dice[3], bottom, top
        else:
            top, bottom, dice[1], dice[3] = dice[3], dice[1], top, bottom

        # 이동한 칸에 쓰여 있는 수가 0인 경우
        if numbers[ni][nj] == 0:
            numbers[ni][nj] = bottom
        # 이동한 칸에 쓰여 있는 수가 0이 아닌 경우
        else:
            bottom = numbers[ni][nj]
            numbers[ni][nj] = 0
        # 주사위가 상단에 쓰여 있는 값을 출력
        print(top)
        # 주사위의 위치를 갱신
        x, y = ni, nj