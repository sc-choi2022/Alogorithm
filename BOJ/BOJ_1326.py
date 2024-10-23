from collections import deque
import sys

# 징검다리의 개수 N
N = int(sys.stdin.readline())
# 징검다리에 쓰여있는 숫자를 저장하는 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))
# 징검다리의 시작위치 a, 도착위치 b
a, b = map(int, sys.stdin.readline().split())
visit = [-1] * N
visit[a-1] = 0

queue = deque([a-1])
while queue:
    now = queue.popleft()
    num = numbers[now]
    for i in range(num, N, num):
        if 0 <= now+i < N and visit[now+i] == -1:
            queue.append(now+i)
            visit[now+i] = visit[now]+1
        if 0 <= now-i < N and visit[now-i] == -1:
            queue.append(now-i)
            visit[now-i] = visit[now] + 1

# a번 징검다리에서 b번 징검다리 이동하는 최소 횟수 출력
# 갈 수 없는 경우 -1 출력
print(visit[b-1])