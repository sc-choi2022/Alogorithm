import sys

def bfs(si, sj):
    return

# 영역의 세로의 길이 R, 세로의 길이 C
R, C = map(int, sys.stdin.readline().split())
# 울타리, 늑대, 양이 있는 공간의 정보를 저장하는 배열 area
area = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
# 살아남은 늑대의 수 V, 양의 수 K
V, K = 0, 0
visit = [[0]*C for _ in range(R)]