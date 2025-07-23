import sys

# 게임판의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 게이판의 점의 색을 저장하는 배열 dots
dots = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

# 방향을 저장하는 딕셔너리 D
D = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
si, sj = 0, 0