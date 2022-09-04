def bfs(i, j):

    for di, dj in (0, -1), (-1, -1), (-1, 1), (0, 1):
        ni, nj = di + i, dj + j
        if 0 <= ni < N and 0 <= nj < M and seat[ni][nj] == 'C':
            return False
    return True

# 테스트 케이스 C
C = int(input())

for _ in range(C):
    # N행 M열의 N, M
    N, M = map(int, input().split())
    seat = [list(input()) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(M):
            if seat[i][j] == '.' and bfs(i, j):
                seat[i][j] = 'C'
                ans += 1
    print(ans)