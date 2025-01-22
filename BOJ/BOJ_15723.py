import sys
from collections import defaultdict, deque

def bfs(start, end):
    queue = deque([start])

    while queue:
        x = queue.popleft()

        if x == end:
            return True

        for node in graph[x]:
            queue.append(node)
    return False

# 정수 N
N = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph[tmp[0]].append(tmp[2])

M = int(sys.stdin.readline())

for _ in range(M):
    lst = list(map(int, sys.stdin.readline().split()))

    if bfs(lst[0], lst[1]):
        print('T')
    else:
        print('F')