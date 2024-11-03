from collections import deque
import sys

# 도시의 개수 N, 버스 노선의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 도시의 이동시간을 저장하는 배열 graph
graph = [[] for _ in range(N+1)]

for _ in range(M):
    # 시작도시 A, 도착도시 B, 이동시간 C
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))

visit = [0] * (N+1)
time = [0] * (N+1)
queue = deque([1])
visit[1] = 1

while queue:
    current = queue.popleft()

    for next, t in graph[current]:
        if not visit[next]:
            visit[next] = 1
            time[next] = time[current] + t
            if t <= 0:
                queue.appendleft(next)
            else:
                queue.append(next)
print(visit)
print(time)