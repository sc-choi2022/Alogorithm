import sys

# 주어지는 괄호열 brackets
brackets = sys.stdin.readline().rstrip()
stack = []
answer = 0

tmp = 1
for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append(brackets[i])
        tmp *= 2
    elif brackets[i] == '[':
        stack.append(brackets[i])
        tmp *= 3
    elif brackets[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        elif brackets[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        elif brackets[i-1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)