import sys

# 버스의 개수 N, 터미널에 도착하는 시간 T
N, T = map(int, sys.stdin.readline().split())

for _ in range(N):
    S, I, C = map(int, sys.stdin.readline().split())