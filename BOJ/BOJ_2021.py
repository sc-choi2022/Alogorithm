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

queue = deque([start])
visit[start] = 1
# 목적지 도달 여부를 확인하는 변수 flag
flag = False

while queue:
    # 현재 역 current
    current = queue.popleft()

    if current == end:
        if start == end:
            # 출발지와 목적지가 동일한 경우
            print(0)
        else:
            print(visit[current]-2)
        flag = True
        break

    for lin in info[current]:
        # 방문한 노선이 아닌 경우
        if line_visit[lin]:
            continue
        line_visit[lin] = 1
        for i in lines[lin]:
            if visit[i]:
                continue
            visit[i] = visit[current] + 1
            queue.append(i)
# 목적지 도달이 불가능한 경우
if not flag:
    print(-1)