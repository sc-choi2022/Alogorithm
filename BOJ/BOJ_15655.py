import sys

def dfs(tmp):
    if len(tmp) == M:
        print(*tmp)
        return

    for i in range(N):
        tmp.append(numbers[i])
        dfs(tmp)
        tmp.pop()

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
dfs([])