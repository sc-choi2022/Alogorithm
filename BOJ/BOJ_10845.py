import sys
# 명령의 수 N
N = int(sys.stdin.readline())
# 저장하는 큐 queue
queue = []

for _ in range(N):
    # 명령을 받아 list로 받는다.
    word = list(sys.stdin.readline().split())
    # push인 경우
    if len(word) == 2:
        if word[0] == 'push':
            queue.append(word[1])
    # 명령어가 1개인 경우
    else:
        # pop
        if word[0] == 'pop':
            print(queue.pop(0) if queue else -1)
        # size
        elif word[0] == 'size':
            print(len(queue))
        # empty
        elif word[0] == 'empty':
            print(0 if queue else 1)
        # front
        elif word[0] == 'front':
            print(queue[0] if queue else -1)
        # back
        elif word[0] == 'back':
            print(queue[-1] if queue else -1)