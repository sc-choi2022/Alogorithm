import sys

# 배열의 크기 N, M, 연산의 수 R
N, M, R = map(int, sys.stdin.readline().split())
# 배열을 저장하는 graph
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]