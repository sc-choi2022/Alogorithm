import sys

# 체크포인트의 수 N
N = int(sys.stdin.readline())
# 체크포인트를 담을 배열 checkpoint
checkpoint = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 체크포인트 사이의 거리를 담을 배열 distance
distance = [0] * N