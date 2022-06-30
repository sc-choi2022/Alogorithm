import sys
# 테스트 케이스 수
T = int(sys.stdin.readline())

for _ in range(T):
    # 조규현의 좌표 x1, y1와 류재명의 예측 거리 r1, 백승환의 좌표 x2, y1와 류재명의 예측 거리 r1
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    # 조규현과 백승환 사이의 거리
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    # 조규현과 백승환이 같은 위치와 거리예측을 갖을 경우 -1 출력
    if distance == 0 and r1 == r2:
        print(-1)
    # 각 위치를 기준으로 r1, r1을 반지름으로 하는 원을 그렸을 때 만나는 점이 하나라면 1 출력
    elif abs(r1 - r2) == distance or (r1 + r2) == distance:
        print(1)
    # 각 위치를 기준으로 r1, r1을 반지름으로 하는 원을 그렸을 때 만나는 점이 두개라면 2 출력
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    # 그 외의 경우는 류재명의 위치를 구할 수 없으므로 0 출력
    else:
        print(0)