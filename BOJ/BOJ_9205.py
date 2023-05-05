import sys

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 편의점의 개수 N
    N = int(sys.stdin.readline())
    # 락 페스티벌 좌표
    x, y = map(int, sys.stdin.readline().split())
    CVS = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    