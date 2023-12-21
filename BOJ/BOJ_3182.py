import sys

def dfs():
    return
#
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    # 선배의 대답 answer
    answer = int(sys.stdin.readline())
    graph[answer].append(i)

for j in range(1, N+1):
    tmp = dfs(j)

print(result)