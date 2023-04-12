from collections import deque
import sys

# 부피 A, B, C
A, B, C = map(int, sys.stdin.readline().split())
visit = [[0]*201 for _ in range(201)]
answer = [0 for _ in range(201)]

queue = deque()
queue.append((0, 0, C))

while queue:
    a, b, c = queue.popleft()

    if visit[a][b] == 1:
        continue
    visit[a][b] = 1

    if a == 0:
        answer[c] = 1
    # A -> B:
    if a+b > B:
        queue.append((a+b-B, B, c))
    else:
        queue.append((0, a+b, c))

    # A -> C
    if a + c > C:
        queue.append((a+c-C, b, C))
    else:
        queue.append((0, b, a+c))

    # B -> C
    if b + c > C:
        queue.append((a, b+c-C, C))
    else:
        queue.append((a, 0, b+c))

    # B -> A
    if b+a > A:
        queue.append((A, b+a-A, c))
    else:
        queue.append((b+a, 0, c))

    # C -> B
    if c+b > B:
        queue.append((a, B, c+b-B))
    else:
        queue.append((a, c+b, 0))

for i in range(201):
    if answer[i]:
        print(i, end=' ')