import sys

# 신호등의 개수 N, 도로의 길이 L
N, L = map(int, sys.stdin.readline().split())

# 도로의 끝까지 이동하는데 걸리는 시간 time
time = 0

for _ in range(N):
    # 신호등의 위치 D, 빨간색이 지속되는 시간 R, 초록색이 지속되는 시간 G
    D, R, G = map(int, sys.stdin.readline().split())