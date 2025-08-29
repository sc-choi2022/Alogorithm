import sys



N = int(sys.stdin.readline())
island = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(N-2):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

for i in range(2, N+1):
    if find(1) != find(i):
        print(1, i)
        break