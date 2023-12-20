import sys

def dfs():
    return

# 맵의 크기 RxC, 거리의 길이 K
R, C, K = map(int, sys.stdin.readline().split())
# 맵의 내용을 저장하는 배열 graph
graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]