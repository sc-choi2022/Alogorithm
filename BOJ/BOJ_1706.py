import sys

# 퍼즐의 길이 R, C
R, C = map(int, sys.stdin.readline().split())
words = [list(sys.stdin.readline().rstrip()) for _ in range(R)]