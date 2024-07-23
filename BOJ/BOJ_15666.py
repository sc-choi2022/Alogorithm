import sys

def dfs(tmp):
    if len(tmp) == M:
        print(*tmp)
        return

    prev = 0
    for j in range(N):
        if prev != numbers[j]:
            prev = numbers[j]
            if not tmp:
                dfs([numbers[j]])
            elif tmp and tmp[-1] <= numbers[j]:
                dfs(tmp+[numbers[j]])

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

dfs([])