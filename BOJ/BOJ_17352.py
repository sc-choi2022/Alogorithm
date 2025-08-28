import sys



N = int(sys.stdin.readline())
island = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(N-2):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)