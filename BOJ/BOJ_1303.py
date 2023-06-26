import sys

# 전쟁터의 가로 크기 N, 세로 크기 M
N, M = map(int, sys.stdin.readline().split())
# 병사의 상태를 담을 배열 army
army = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(M)]