import sys

def dfs(v):
    for k in range(N):
        if visit[k] == 0 and S[v][k] == 1:
            visit[k] = 1
            dfs(k)

N = int(sys.stdin.readline())
visit = [0] * N

S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    dfs(i)
    for j in range(N):
        if visit[j] == 1:
            print(1, end='')
        else:
            print(0, end='')
    print()
    visit = [0] * N