from collections import deque
import sys
# 수빈이의 위치 N, 동생의 위치 K
N, K = map(int, sys.stdin.readline().split())
visit = [0] * 100001

queue = deque()
queue.append(N)
visit[N] = 1
while queue:
    site = queue.popleft()
    if site == K:
        print(visit[site]-1)
        break

    for next in (2*site, site+1, site-1):
        if 0 <= next < 100001 and visit[next] == 0:
            if next == 2*site:
                visit[next] = visit[site]
                queue.appendleft(next)
            else:
                visit[next] = visit[site] + 1
                queue.append(next)