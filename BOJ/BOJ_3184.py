from collections import deque
import sys

# 두 정수 R, C
R, C = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]