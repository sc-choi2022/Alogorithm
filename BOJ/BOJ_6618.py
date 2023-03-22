from collections import deque
import sys

# 헛간의 개수 N, 길의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 헛간 barn의 길들의 정보를 담을 배열 barn
barn = [[] for _ in range(N+1)]
# 헛간까지의 거리를 담을 배열 visit
visit = [-1] * (N+1)
visit[1] = 0

for i in range(M):
    A_i, B_i = map(int, sys.stdin.readline().split())
    barn[A_i].append(B_i)
    barn[B_i].append(A_i)

queue = deque()
queue.append(1)

while queue:
    site = queue.popleft()

    for i in range(2, N+1):
        if i in barn[site] and visit[i] == -1:
            visit[i] = visit[site] + 1
            queue.append(i)
# 최대거리 maximum
maximum = max(visit)
# 숨어야 하는 헛간 번호, 그 헛간까지의 거리, 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력
print(visit.index(maximum), maximum, visit.count(maximum))