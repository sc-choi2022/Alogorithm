import sys

def find(N):
    if parents[N] != N:
        parents[N] = find(parents[N])
    return parents[N]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 행성의 수 N
N = int(sys.stdin.readline())
# 행성의 연결정보를 저장하는 배열 planet
planet = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

parents = [i for i in range(N+1)]
# 간선의 정보를 저장하는 배열 edges
edges = []
for i in range(1, N):
    for j in range(i):
        edges.append((i, j, planet[i][j]))
edges.sort(key=lambda x:x[2])

answer = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)