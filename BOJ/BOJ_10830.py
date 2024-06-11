import sys

# 행렬 A의 크기 N, 제곱하는 수 B
N, B = map(int, sys.stdin.readline().split())
# 행렬 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
