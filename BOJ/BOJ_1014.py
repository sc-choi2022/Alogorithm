def dfs():
    return

# 테스트 케이스 C
C = int(input())

for _ in range(C):
    # N행 M열의 N, M
    N, M = map(int, input().split())
    seat = [list(input()) for _ in range(N)]

    ans = 0

    cor_map = [[0]*N for _ in range(M)]