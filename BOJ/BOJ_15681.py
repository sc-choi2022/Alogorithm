import sys

# 정점의 수 N, 루트의 번호 R, 쿼리의 수 Q
N, R, Q = map(int, sys.stdin.readline().split())

for _ in range(N-1):
    # 간선의 정보 u, v
    u, v = map(int, sys.stdin.readline().split())

for _ in range(Q):
    U = int(sys.stdin.readline())