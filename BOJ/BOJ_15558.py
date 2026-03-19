from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
info = ['0'+sys.stdin.readline().rstrip() for _ in range(2)]
visit = [[0]*(N+1) for _ in range(2)]
visit[0][1] = 1

queue = deque([(0, 1, 1)])

while queue:
    line, num, sec = queue.popleft()
    for n_line, n_num in []:
        if n_num > N:
            print(1)