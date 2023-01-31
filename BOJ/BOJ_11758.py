import sys

# 점 P1, P2, P3
P1 = list(map(int, sys.stdin.readline().split()))
P2 = list(map(int, sys.stdin.readline().split()))
P3 = list(map(int, sys.stdin.readline().split()))

# CCW(counter clock wise) 외적
ccw = (P1[0] * P2[1] + P2[0] * P3[1] + P3[0] * P1[1]) - (P2[0] * P1[1] + P3[0] * P2[1] + P1[0] * P3[1])

# 반시계 방향
if ccw > 0:
    print(1)
# 시계 방향
elif ccw < 0:
    print(-1)
# 일직선
else:
    print(0)