import sys

def check():
    return

# 문자열 string
string = list(sys.stdin.readline().rstrip())
# 폭발 문자열 boom
boom = sys.stdin.readline().rstrip()
# 폭발 문자열의 길이 N
N = len(boom)
stack = []

for s in string:
    stack.append(s)
    # stack의 마지막 N개의 문자가 boom과 동일할 경우 N번 pop() 실행
    if ''.join(stack[-N:]) == boom:
        for _ in range(N):
            stack.pop()

# 남은 문자열이 있는 경우
if stack:
    print(''.join(stack))
# 남은 문자열이 없는 경우
else:
    print('FRULA')