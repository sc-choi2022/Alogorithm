from collections import deque
import sys

dequeue = deque()

N = int(sys.stdin.readline())

for _ in range(N):
    # 주어지는 명령어
    order = sys.stdin.readline().rstrip()

    if len(order) > 2:
        if order[0] == '1':
            dequeue.appendleft(int(order[2:]))
        else:
            dequeue.append(int(order[2:]))
    elif order == '3':
        print(dequeue.popleft() if dequeue else -1)
    elif order == '4':
        print(dequeue.pop() if dequeue else -1)
    elif order == '5':
        print(len(dequeue))
    elif order == '6':
        print(0 if dequeue else 1)
    elif order == '7':
        print(dequeue[0] if dequeue else -1)
    else:
        print(dequeue[-1] if dequeue else -1)