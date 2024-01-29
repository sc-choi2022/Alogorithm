import sys

def find(N):
    if parent[N] != N:
        parent[N] = find(parent[N])
    return parent[N]

def union(a, b):
    a, b = find(a), find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    # 집의 수 M, 길의 수 N
    M, N = map(int, sys.stdin.readline().split())

    if (M, N) == (0, 0):
        break
    