import sys

def dfs()

# 사무실의 세로 크기 N, 가로 크기 M
N, M = map(int, sys.stdin.readline().split())
# 사무실의 정보 room
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]