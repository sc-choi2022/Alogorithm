from collections import deque
import sys

def bfs():
    queue = deque()

N, K = map(int, sys.stdin.readline().split())
info = [sys.stdin.readline().rstrip() for _ in range(K)]