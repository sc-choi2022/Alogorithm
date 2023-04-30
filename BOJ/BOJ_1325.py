from collections import deque
import sys

def bfs(num):
    global cnt, number
    tmp = 1
    queue = deque([num])
    visit = [0] * (N+1)
    visit[num] = 1

    while queue:
        current = queue.popleft()

        for i in hackable[current]:
            if not visit[i]:
                queue.append(i)
                visit[i] = 1
                tmp += 1
    if tmp > cnt:
        cnt = tmp
        number = [num]
    elif tmp == cnt:
        number.append(num)

# 컴퓨터의 개수 N, 신뢰하는 관계의 수 M
N, M = map(int, sys.stdin.readline().split())
hackable = [[0] for _ in range(N+1)]

cnt, number = 0, []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    # hackable[A].append(B)
    hackable[B].append(A)

for j in range(1, N):
    bfs(j)

number.sort()
print(*number)