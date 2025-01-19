import sys

# 정수 N
N = int(sys.stdin.readline())
graph = [[] for _ in range(26)]

for _ in range(N):
    a, b = map(str, sys.stdin.readline().split(' is '))

M = int(sys.stdin.readline())