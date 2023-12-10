import sys

# 명렬의 개수 N
N = int(sys.stdin.readline())
# 스택 현황을 저장하는 배열 stack
stack = []

for _ in range(N):
    # 주어지는 명령 order
    order = sys.stdin.readline().rstrip()

    if len(order) > 2:
        stack.append(int(order[2:]))
    elif order == '2':
        print(stack.pop() if stack else -1)
    elif order == '3':
        print(len(stack))
    elif order == '4':
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)