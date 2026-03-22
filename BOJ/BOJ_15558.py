from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
info = ['0'+sys.stdin.readline().rstrip() for _ in range(2)]
visit = [[0]*(N+1) for _ in range(2)]
visit[0][1] = 1

queue = deque([(0, 1, 1)])

while queue:
    line, num, sec = queue.popleft()
    for n_line, n_num in [(line, num+1), (line, num-1), (line^1, num+K)]:
        if n_num > N:
            print(1)
            exit()
        if 0 <= n_line <= N and info[n_line][n_num] == '1' and n_num > sec and not visit[n_line][n_num]:
            queue.append((n_line, n_num, sec+1))
            visit[n_line][n_num] = 1

print(0)