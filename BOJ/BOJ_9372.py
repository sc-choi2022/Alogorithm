from collections import deque
import sys

def dfs(node, cnt):
    visit[node] = 1
    for c in country[node]:
        if not visit[c]:
            cnt = dfs(c, cnt + 1)
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

    visit = [0] * (N+1)
    print(dfs(1, 0))

# 모든 국가가 연결되어 있기 때문에 아래와 같은 방법도 정답이다.
import sys

# 테스트케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 국가의 수 N와 비행기의 종류 M
    N, M = map(int, sys.stdin.readline().split())

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
    print(N-1)