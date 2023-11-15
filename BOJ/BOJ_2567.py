import sys

# 색종이의 수 N
N = int(sys.stdin.readline())

for _ in range(N):
    # 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리 A
    # 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리 B
    A, B = map(int, sys.stdin.readline().split())