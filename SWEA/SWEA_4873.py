import sys
sys.stdin = open('sample_input.txt')

# 테스트 케이스
T = int(input())

for case in range(1, T+1):
    # 문자열의 각 문자를 담은 리스트 sen
    sen = list(input())
    # 중복없이 담을 스택 리스트 stack
    stack = []

    # 문자열의 문자에 대해
    for s in sen:
        # 스택 리스트가 비어있다면 스택에 s추가
        if stack == []:
            stack.append(s)
        # 스택의 top과 s가 다르다면 스택에 s추가
        elif stack[-1] != s:
            stack.append(s)
        # 스택의 top과 s가 같다면 스택.pop()
        elif stack[-1] == s:
            stack.pop()
    # 테스트 케이스 번호와 스택리스트에 담긴 문자열의 길이 출력
    print(f'#{case} {len(stack)}')