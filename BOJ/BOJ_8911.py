import sys

# 테스트 케이스 T
T = int(sys.stdin.readline())
# 방향을 저장하는 배열 directions
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(T):
    # 좌표 수가 작은 위치의 기준좌표 si, sj
    si, sj = 0, 0
    # 좌표 수가 큰 위치의 기준좌표 ei, ej
    ei, ej = 0, 0
    # 초기 거북이의 위치와 방향 ti, tj, d
    ti, tj, d = 0, 0, 0
    # 명령들의 문자열 orders
    orders = sys.stdin.readline().rstrip()
    lotation_x, location_y = [], []

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
        # 방향이 0인 경우
        if not d:
            ej = max(ej, tj)
        elif d == 1:
            ei = max(ei, ti)
        elif d == 2:
            sj = min(sj, tj)
        else:
            si = min(si, ti)
    # 거북이가 이동한 영역을 모두 포함하는 가장 작은 직사각형의 넓이를 출력
    print(abs(ei-si)*abs(ej-sj))