import sys

# 지름길의 개수 N과 고속도로의 길이 D
N, D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append((i+1, 1))

for j in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    if end > D:
        continue
    graph[start].append((end, length))