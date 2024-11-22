from collections import deque
import sys

def trace(k, visited):
    if k == 0:
        return
    trace(visited[k], visited)
    print(k-visited[k], end=' ')

# 금민수의 합으로 나타내야하는 정수 N
N = int(sys.stdin.readline())
gold = []

for i in range(2, 200):
    bi = []
    s = ''
    tmp = i
    while tmp:
        bi.append(tmp%2)
        tmp //= 2
    for j in range(len(bi)-1, -1, -1):
        if j == len(bi)-1:
            continue
        if bi[j] == 0:
            s += '4'
        else:
            s += '7'
    gold.append(int(s))

visit = [-1] * 1000001
queue = deque([0])

while queue:
    now = queue.popleft()
    if now == N:
        break
    for ii in range(len(gold)):
        next = now + gold[ii]
        if next > N:
            continue
        if visit[next] == -1:
            visit[next] = now
            queue.append(next)

if visit[N] == -1:
    print(-1)
else:
    trace(N, visit)