import sys

# 정점의 개수 N
N = int(sys.stdin.readline())
# 간선의 정보를 저장하는 배열 edges
edges = [(0, 0)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
tree = [[] for _ in range(N+1)]

# 질의의 개수 Q
Q = int(sys.stdin.readline())

for _ in range(Q):
    # 질의 t, k
    t, k = map(int, sys.stdin.readline().split())

    if t == 1:
        continue
    else:
        continue