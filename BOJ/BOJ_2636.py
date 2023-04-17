import sys

# 세로와 가로의 길이 N, M
N, M = map(int, sys.stdin.readline().split())

# 치즈의 위치가 담긴 배열 cheeses
cheeses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
