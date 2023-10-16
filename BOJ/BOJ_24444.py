from collections import deque
import sys
N, M, R = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N + 1)

def bfs(graph, start, visited):
    return