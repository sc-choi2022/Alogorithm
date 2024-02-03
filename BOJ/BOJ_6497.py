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

    parent = [i for i in range(M+1)]
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    edges.sort(key=lambda x: x[2])

    # 연결되지 않아 절약되는 비용 answer
    answer = 0
    for a, b, c in edges:
        if find(a) != find(b):
            union(a, b)
        else:
            answer += c

    # 절약할 수 있는 최대 비용을 출력
    print(answer)