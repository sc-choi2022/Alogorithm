import sys

# 테스트케이스 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 입력한 문자열 L
    L = sys.stdin.readline().rstrip()

    # 스택을 활용하고 커서를 적용하기 위한 stack1, stack2
    stack1 = []
    stack2 = []
    for l in L:
        # < 이고 stack1이 비어있지 않은 경우
        if l == '<' and stack1:
            stack2.append(stack1.pop())
        # > 이고 stack2이 비어있지 않은 경우
        elif l == '>' and stack2:
            stack1.append(stack2.pop())
        # 알파벳 혹은 숫자인 경우 stack1에 append
        elif l.isalpha() or l.isdigit():
            stack1.append(l)
        # 백스페이스이면서 stack1이 비어있지 않은 경우
        elif l == '-' and stack1:
            stack1.pop()
    # 강산이의 비밀번호를 출력
    print(''.join(stack1 + list(reversed(stack2))))