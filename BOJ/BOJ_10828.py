import sys
N = int(sys.stdin.readline())

# stack 리스트 생성
stack = []
# N개의 word를 받아서 스택을 처리
for i in range(N):
    word = sys.stdin.readline().split()
    # push 명령
    if word[0] == 'push':
        stack.append(word[1])
    # top 명령
    elif word[0] == 'top':
        if stack:
            print(stack[-1])
        # stack이 비어있다면
        else:
            print(-1)
    # size 명령
    elif word[0] == 'size':
        print(len(stack))
    # empty 명령
    elif word[0] == 'empty':
        if len(stack) == 0:
            print(1)
        # 비어있지 않다면
        elif len(stack) != 0:
            print(0)
    # pop 명령
    elif word[0] == 'pop':
        if stack:
            print(stack.pop())
        # stack이 비어있다면
        else:
            print(-1)

# 코드 수정 후
import sys

# 명령의 수 N
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    order, *number = list(sys.stdin.readline().rstrip().split())
    if order == 'push':
        stack.append(int(number[0]))
    elif order == 'pop':
        print(stack.pop() if stack else -1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)