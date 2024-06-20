from collections import deque
import sys

# 바꾸려하는 문자 A, B
A, B = map(int, sys.stdin.readline().split())
# 전체 문자의 수 N, 치환 가능한 문자싼의 수 M
N, M = map(int, sys.stdin.readline().split())

# 치환 가능한 문자쌍을 저장하는 배열 change
change = [[] for _ in range(N+1)]

for _ in range(M):
    # 치환 가능한 문자쌍 a, b
    a, b = map(int, sys.stdin.readline().split())
    change[a].append(b)
    change[b].append(a)

visit = [-1]*(N+1)
visit[A] = 0
queue = deque([A])

while queue:
    current = queue.popleft()

    if current == B:
        break

    for next in change[current]:
        if visit[next] == -1:
            visit[next] = visit[current] + 1
            queue.append(next)

# A를 B로 바꾸기 위해 필요한 최소 치환 횟수를 출력
# 치환이 불가능한 경우 -1 출력
print(visit[B])