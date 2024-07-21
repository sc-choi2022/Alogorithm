import sys

def dfs(tmp):
    if len(tmp) == M:
        print(*tmp)
        return
    check = 0
    for j in range(N):
        if check != numbers[j] and not visit[j] and (not tmp or tmp[-1] <= numbers[j]):
            visit[j] = 1
            check = numbers[j]
            dfs(tmp+[numbers[j]])
            visit[j] = 0

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
visit = [0] * N

dfs([])