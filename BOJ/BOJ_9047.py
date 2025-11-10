from itertools import combinations
import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 네자리 수 N
    N = list(map(int, sys.stdin.readline().rstrip()))