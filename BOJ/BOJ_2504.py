import sys

# 주어지는 괄호열 brackets
brackets = sys.stdin.readline().rstrip()
stack = []
# 괄호열의 값을 저장하는 변수 answer
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
        # 올바르지 않은 괄호열인 경우
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

#  올바르지 못한 괄호열인 경우 0 출력
if stack:
    print(0)
# answer 출력
else:
    print(answer)