import sys

# 도시의 개수 N
N = int(sys.stdin.readline())
# 버스의 개수 M
M = int(sys.stdin.readline())
# 도시 사이의 정보를 담을 배열 info
info = [[0]*(N + 1) for _ in range(N + 1)]

for _ in range(M):
    # 버스의 시작 도시 A, 도착도시 B, 한 번 타는데 필요한 비용 C
    A, B, C = map(int, sys.stdin.readline().split())
    info[A][B] = C