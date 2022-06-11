import sys
from collections import deque

# deque를 활용하여 queue 생성
queue = deque()

for _ in range(int(sys.stdin.readline())):
    tmp = list(sys.stdin.readline().split())
    # push인 경우 두개의 문자열이 들어온다.
    if len(tmp) == 2:
        # queue에 두번제 문자열을 int로 변환하여 넣어준다.
        queue.append(int(tmp[1]))
    else:
        # pop일 때 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력
        if tmp[0] == 'pop':
            if queue:
                print(queue.popleft())
            # 큐에 들어있는 정수가 없는 경우에는 -1을 출력
            else:
                print(-1)
        # size일 때 큐에 들어있는 정수의 개수를 출력
        elif tmp[0] == 'size':
            print(len(queue))
        # empty일 때
        elif tmp[0] == 'empty':
            # 큐가 비어있지 않으면 0을 출력
            if queue:
                print(0)
            # 비어있다면 1 출력
            else:
                print(1)
        # front일때 큐의 가장 앞에 있는 정수를 출력
        elif tmp[0] == 'front':
            if queue:
                print(queue[0])
            # 큐에 들어있는 정수가 없는 경우에는 -1을 출력
            else:
                print(-1)
        # back일 때 큐의 가장 뒤에 있는 정수를 출력
        elif tmp[0] == 'back':
            if queue:
                print(queue[-1])
            # 큐에 들어있는 정수가 없는 경우에는 -1을 출력
            else:
                print(-1)