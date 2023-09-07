import sys

# 테스트 케이스 T
T = int(sys.stdin.readline())
# 방향을 저장하는 배열 directions
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(T):
    # 이동 좌표의 가로 좌표, 세로좌표를 저장하는 set garo, sero
    garo, sero = {0,}, {0,}
    # 초기 거북이의 위치와 방향 ti, tj, d
    ti, tj, d = 0, 0, 0
    # 명령들의 문자열 orders
    orders = sys.stdin.readline().rstrip()

    for order in orders:
        if order == 'F':
            ti += directions[d][0]
            tj += directions[d][1]
        elif order == 'B':
            ti -= directions[d][0]
            tj -= directions[d][1]
        elif order == 'L':
            d = (d-1)%4
        else:
            d = (d+1)%4
        garo.add(ti)
        sero.add(tj)
    # garo와 sero의 좌표를 배열로 정렬
    G, S = sorted(list(garo)), sorted(list(sero))

    # 거북이가 이동한 영역을 모두 포함하는 가장 작은 직사각형의 넓이를 출력
    print((G[-1]-G[0])*(S[-1]-S[0]))