def bfs(i, j):
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