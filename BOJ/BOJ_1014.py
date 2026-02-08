import sys

# 테스트 케이스 C
C = int(input())

for _ in range(C):
    # N행 M열의 N, M
    N, M = map(int, sys.stdin.readline().split())
    seat = [list(sys.stdin.readline()) for _ in range(N)]

    ans = 0

    cor_map = [[0]*N for _ in range(M)]