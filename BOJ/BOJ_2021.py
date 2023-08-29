from collections import deque
import sys

# 역의 개수 N, 노선의 개수 L
N, L = map(int, sys.stdin.readline().split())
# 역의 방문 정보를 저장하는 배열 visit, 노선의 방문 정보를 저장하는 배열 line_visit
visit, line_visit = [0]*(N+1), [0]*(L+1)
# 노선의 정보를 저장하는 배열 lines
lines = [list(map(int, sys.stdin.readline().split()))[:-1] for _ in range(L)]
# 각 역의 노선 정보를 저장하는 배열 info
info = [[] for _ in range(N+1)]

for l in range(L):
    for station in lines[l]:
        info[station].append(l)

# 시작역 start, 도착역 end
start, end = map(int, sys.stdin.readline().split())
if start == end:
    print(0)
else:
    queue = deque()
    visit[start] = 1
    flag = False

    while queue:
        # 현재 역 current
        current = queue.popleft()
        # 도착역에 도달한 경우
        if current == end:
            print(visit[current]-2)
            flag = True
            break

        for i in info[current]:
            if line_visit[i]:
                continue
            line_visit[i] = 1
            for st in lines[i]:
                if visit[st]:
                    continue
                visit[st] = visit[current] + 1
                queue.append(st)
    if not flag:
        print(-1)