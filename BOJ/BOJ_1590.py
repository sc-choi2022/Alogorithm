import sys

# 버스의 개수 N, 터미널에 도착하는 시간 T
N, T = map(int, sys.stdin.readline().split())
# 버스의 정보 B
B = [tuple(map(int, sys.stdin.readline())) for _ in range(N)]