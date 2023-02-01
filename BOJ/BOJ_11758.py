import sys

# 점 P1, P2, P3의 정보를 담을 배열 P
P = [tuple(map(int, sys.stdin.readline().split())) for _ in range(3)]

# CCW(counter clock wise) 외적
ccw = (P[0][0] * P[1][1] + P[1][0] * P[2][1] + P[2][0] * P[0][1]) - (P[1][0] * P[0][1] + P[2][0] * P[1][1] + P[0][0] * P[2][1])

# 반시계 방향
if ccw > 0:
    print(1)
# 시계 방향
elif ccw < 0:
    print(-1)
# 일직선
else:
    print(0)