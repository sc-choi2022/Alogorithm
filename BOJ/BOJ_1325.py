from collections import deque
import sys

def bfs(start):
    queue = deque([start])
    visit = [0] * (N+1)
    visit[start] = 1
    tmp = 1

    while queue:
        current = queue.popleft()

        for c in trust[current]:
            if not visit[c]:
                queue.append(c)
                visit[c] = 1
                tmp += 1
    return tmp

# 컴퓨터의 개수 N, 신뢰하는 관계의 수 M
N, M = map(int, sys.stdin.readline().split())
# 신뢰 정보를 저장하는 배열 trust
trust= [[] for _ in range(N+1)]
# 해킹할 수 있는 컴퓨터의 최대수 cnt, cnt만큼 해킹 가능한 컴퓨터 배열 computer
cnt, computer = 1, []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    trust[B].append(A)

for j in range(1, N+1):
    number = bfs(j)
    if number > cnt:
        cnt = number
        computer.clear()
        computer = [j]
    elif number == cnt:
        computer.append(j)

print(*computer)