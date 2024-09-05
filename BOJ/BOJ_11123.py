import sys

# 테스트 케이스의 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 그리드의 높이 H, 너비 W
    H, W = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().rstrip()) for _ in range(H)]