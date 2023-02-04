from collections import deque
import sys

# 큐의 크기 N, 뽑아내려고 하는 수의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 뽑아내려는 M개의 위치를 담은 배열 orders
orders = list(map(int, sys.stdin.readline().split()))

# 회전하는 양방향 순환 큐 queue
queue = deque([x for x in range(1, N + 1)])

# 출력할 좌우 이동 횟수 cnt
cnt = 0

for order in orders:
    # 1번 연산이 가능한 경우
    if queue[0] == order:
        queue.popleft()
    # 2번, 3번 연산이 필요한 경우
    else:
        while order in queue:
            # 찾아야하는 위치 idx
            idx = queue.index(order)
            # 2번 연산이 필요한 경우
            if idx < len(queue) - idx:
                queue.append(queue.popleft())
            # 3번 연산이 필요한 경우
            else:
                queue.appendleft(queue.pop())
            # 횟수 1 증가
            cnt += 1
            # 1번 연산으로 제거 가능한 경우
            if queue[0] == order:
                queue.popleft()
# 2번, 3번 연산의 최솟값을 출력
print(cnt)