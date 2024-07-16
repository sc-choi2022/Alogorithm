import sys

def dfs(tmp):
    if len(tmp) == M:
        print(*tmp)
        return
    check = 0
    for i in range(N):
        if not visit[i] and check != numbers[i]:
            visit[i] = 1
            tmp.append(numbers[i])
            check = numbers[i]
            dfs(tmp)
            visit[i] = 0
            tmp.pop()

# N개의 자연수 중에서 M개를 고르는 기준이 되는 자연수 N, M
N, M = map(int, sys.stdin.readline().split())
# N개의 자연수를 저장하는 배열 numbers
numbers = sorted(list(map(int, sys.stdin.readline().split())))
visit = [0]*N

dfs([])