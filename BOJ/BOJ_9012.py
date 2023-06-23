import sys

# 테스트 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    tests = sys.stdin.readline().rstrip()

    for test in tests:
        if stack and (stack[-1] == '(' and test == ')'):
            stack.pop()
        else:
            stack.append(test)
    if not stack:
        print('YES')
    else:
        print('NO')

# 함수
import sys

def check():
    for test in tests:
        if stack and (stack[-1] == '(' and test == ')'):
            stack.pop()
        elif not stack and test == ')':
            return 'NO'
        else:
            stack.append(test)
    if not stack:
        return 'YES'
    else:
        return 'NO'

# 테스트 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    tests = sys.stdin.readline().rstrip()
    print(check())