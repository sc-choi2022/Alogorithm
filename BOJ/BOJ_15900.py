import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    visit[node] = 1
    for next in graph[node]:
        if not visit[next]:
            depth[next] = depth[node] + 1
            dfs(next)

# 트리의 정점 개수 N
N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
visit = [0] * N
depth = [0] * N
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# 루트노드에서 함수 dfs 실행
dfs(0)
# 게임의 총 움직인 횟수를 저장하는 변수 result
result = 0
for i in range(1, N):
    # 리프노드인 경우 움직인 횟수를 result 더한다.
    if len(graph[i]) == 1:
        result += depth[i]

# 게임을 이길 수 있으면 Yes, 아니면 No를 출력
if result%2:
    print('Yes')
else:
    print('No')