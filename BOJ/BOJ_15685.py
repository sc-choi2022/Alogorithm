import sys

def curve(ci, cj):
    return 

# 드래곤 커브의 개수 N
N = int(sys.stdin.readline())
direct = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
# 드래곤 커브를 위해 사용할 배열 dragon
dragon = [[0]*101 for _ in range(101)]

for _ in range(N):
    # 드래곤 커브의 시작 점 (x, y), 시작 방향 d, 세대 g
    x, y, d, g = map(int, sys.stdin.readline().split())