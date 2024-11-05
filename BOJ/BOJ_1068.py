import sys

# 트리의 노드의 개수 N
N = int(sys.stdin.readline())
# 부모노드를 저장한 배열 parents
parents = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(N)]

for i in range(N):
    if parents[i] == -1:
        continue
    graph[parents[i]].append(i)
# 지우는 노드의 번호 num
num = int(sys.stdin.readline())
