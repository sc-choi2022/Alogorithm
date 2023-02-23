import sys

# 모눈종이의 크기 H, W
H, W = map(int, sys.stdin.readline().split())
# 스티커의 수 N
N = int(sys.stdin.readline())

for _ in range(N):
    # 스티커의 크기 R, C
    R, C = map(int, sys.stdin.readline().split())