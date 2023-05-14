from collections import deque
import sys

def dfs(node, cnt):
    visit[node] = 1
    for i in country[node]:
        if not visit[i]:
            cnt = dfs(i, cnt + 1)
    return cnt

# 테스트케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 국가의 수 N와 비행기의 종류 M
    N, M = map(int, sys.stdin.readline().split())
    # country
    country = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        country[a].append(b)
        country[b].append(a)

    cnt = 0
    visit = [0] * (N+1)
    visit[1] = 0
    print(dfs(1, 0))