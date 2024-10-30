import sys
sys.setrecursionlimit(10**5)

def dfs(node):
    visit[node] = 1

    for next in graph[node]:
        if not visit[next]:
            visit[next] = visit[node] + 1
            dfs(next)
        else:
            print(next)

# 테스트케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 노드의 개수 N
    N = int(sys.stdin.readline())
    # 노드의 정보를 저장하는 배열 graph
    graph = [[] for _ in range(N+1)]

    for __ in range(N-1):
        # 부모노드 A, 자식노드 B
        A, B = map(int, sys.stdin.readline().split())
        graph[B].append(A)
    # 공통 조상을 구하는 두 노드 n1, n2
    n1, n2 = map(int, sys.stdin.readline().split())
    n1, n2 = min(n1, n2), max(n1, n2)

    if n1 == n2:
        print(n1)
    else:
        visit = [0] * (N+1)
        dfs(n1)
        dfs(n2)