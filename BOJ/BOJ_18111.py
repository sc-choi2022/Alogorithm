import sys

# 집터의 크기 N, M, 블록의 개수 B
N, M, B = map(int, sys.stdin.readline().split())
# 땅의 높이를 저장하는 배열 ground
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
