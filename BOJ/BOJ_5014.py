from collections import deque
import sys

def bfs(start):
    queue = deque([start])
    visit[start] = 0

    while queue:
        current = queue.popleft()

        for next in (current + U), (current - D):
            if 0 < next <= F and visit[next] == -1:
                visit[next] = visit[current] + 1
                if next == G:
                    return
                queue.append(next)

# 스타트링크의 층수 F, 강호의 위치 S, 스타트링크의 위치 G, 위로 U층, 아래로 D층 이동
F, S, G, U, D = map(int, sys.stdin.readline().split())

visit = [-1] * (F+1)
bfs(S)
# S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값을 출력한다.
# 만약, 엘리베이터로 이동할 수 없을 때는 "use the stairs"를 출력
print(visit[G] if visit[G] != -1 else 'use the stairs')