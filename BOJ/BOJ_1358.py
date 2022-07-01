import sys

# 너비 W, 높이 H, 기준점 X, Y, 위치 정보를 제공하는 선수의 수 P
W, H, X, Y, P = map(int, sys.stdin.readline().split())

# 출력하는 명수 cnt
cnt = 0

for _ in range(P):
    # 선수의 위치 x, y
    x, y = map(int, sys.stdin.readline().split())
    # 반지름 R
    R = H * 0.5
    # 왼쪽 반원을 확인하기 위한 원과 선수 위치의 거리 d1
    d1 = ((X - x)**2 + ((Y + R) -y)**2)**0.5
    # 오른쪽 반원을 확인하기 위한 원과 선수 위치의 거리 d1
    d2 = (((X + W) - x)**2 + ((Y + R) - y)**2)**0.5
    # 왼쪽 원에 있는 경우, 오른쪽 원에 있는 경우, 사각형 안에 있는 경우 cnt 1 증가
    if (d1 <= R) or (d2 <= R) or (X <= x <= X + W and Y <= y <= Y + H):
        cnt += 1
# cnt 출력
print(cnt)