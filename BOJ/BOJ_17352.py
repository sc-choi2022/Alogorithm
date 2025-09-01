import sys

def find(x):
    if x == island[x]:
        return x
    island[x] = find(island[x])
    return island[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        island[y] = x
    else:
        island[x] = y

N = int(sys.stdin.readline())
island = [i for i in range(N+1)]

for _ in range(N-2):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

for i in range(2, N+1):
    if find(1) != find(i):
        print(1, i)
        break