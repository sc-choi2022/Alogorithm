import sys
from collections import defaultdict, deque

# 정수 N
N = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph[tmp[0]].append(tmp[2])

M = int(sys.stdin.readline())