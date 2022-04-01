def DFS(n):
    global add, answer
    if n == N:
        if answer > add:
            answer = add
        return

    if answer <= add:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            add += arr[n][i]
            DFS(n+1)
            visited[i] = 0
            add -= arr[n][i]

T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    add = 0
    answer = 99 * 15
    visited = [0]*N

    DFS(0)
    print(f'#{case} {answer}')
