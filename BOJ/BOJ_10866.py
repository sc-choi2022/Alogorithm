import sys
from collections import deque
# 명령의 수 N
N = int(sys.stdin.readline())
# dq 덱(deque) 생성
dq = deque()
# N개의 명령에 대한 for문
for _ in range(N):
    # 명령을 리스트로 받는다.
    words = list(sys.stdin.readline().split())
    # push_front라면 dq의 앞에 word[1]을 추가
    if words[0] == 'push_front':
        dq.appendleft(words[1])
    # push_back라면 dq의 뒤에 word[1]을 추가
    elif words[0] == 'push_back':
        dq.append(words[1])
    # pop_front라면 dq의 가장 앞에 있는 값을 빼서 출력, 정수가 없다면 -1 출력
    elif words[0] == 'pop_front':
        print(dq.popleft() if dq else -1)
    # pop_back라면 dq의 가장 뒤에 있는 값을 빼서 출력, 정수가 없다면 -1 출력
    elif words[0] == 'pop_back':
        print(dq.pop() if dq else -1)
    # size라면 dq에 들어있는 정수의 개수를 출력
    elif words[0] == 'size':
        print(len(dq))
    # empty라면 dq가 비어있는 경우 1을 그렇지 않은 경우 0을 출력
    elif words[0] == 'empty':
        print(0 if dq else 1)
    # front라면 dq의 가장 앞에 있는 값을 출력 정수가 없다면 -1 출력
    elif words[0] == 'front':
        print(dq[0] if dq else -1)
    # back라면 dq의 가장 뒤에 있는 값을 출력 정수가 없다면 -1 출력
    elif words[0] == 'back':
        print(dq[-1] if dq else -1)

# 코드 수정 후
from collections import deque
import sys

# 명령의 수 N
N = int(sys.stdin.readline())
queue = deque([])

for _ in range(N):
    # 명령 order, 필요한 경우 숫자 number
    order, *number = list(sys.stdin.readline().rstrip().split())

    if order == 'push_front':
        queue.appendleft(int(number[0]))
    elif order == 'push_back':
        queue.append(int(number[0]))
    elif order == 'pop_front':
        print(queue.popleft() if queue else -1)
    elif order == 'pop_back':
        print(queue.pop() if queue else -1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        print(0 if queue else 1)
    elif order == 'front':
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)