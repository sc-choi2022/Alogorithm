import sys
from collections import deque
# 사다리의 수 N
N, M = map(int,sys.stdin.readline().split())
game = [0] * 101
visit = [0] * 101
cnt = [0] * 101

for i in range(N):
    x, y = map(int,sys.stdin.readline().split())
    game[x] = y

for j in range(M):
    u, v = map(int,sys.stdin.readline().split())
    game[u] = v

queue = deque()
# 1번 칸에서 시작
queue.append(1)
visit[1] = 1

while queue:
    temp = queue.popleft()

    for i in range(1, 6+1):
        next = temp + i
        if next <= 100 and visit[next]:
            if game[next]:
                next = game[next]
            if visit[next] == 0:
                visit[next] = 1
                cnt[next] = cnt[temp] + 1
                queue.append(next)
    if cnt[next]:
        break
print(cnt[next])