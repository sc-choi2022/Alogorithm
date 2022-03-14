import sys
sys.stdin = open('sample_input.txt')

# 테스트 케이스 수
T = int(input())
for case in range(1, T+1):
    # 문자열을 받을 리스트 info
    info = list(input())
    # 괄호를 담을 스택 리스트 stack
    stack = []

    # 답 ans 초기화
    ans = 0

    # 문자열의 길이만큼 for문
    for i in range(len(info)):
        # 문자가 ( 혹은 { 일 경우 stack에 추가
        if info[i] == '(' or info[i] == '{':
            stack.append(info[i])
        # 문자가 ) 혹은 } 일 경우
        elif info[i] == ')' or info[i] == '}':
            # 스택이 비어있지 않고, stack의 top이 짝이 맞는 괄호라면 stack.pop()
            if stack != [] and info[i]==')' and stack[-1] =='(':
                stack.pop()
            elif stack !=[] and info[i]=='}' and stack[-1] =='{':
                stack.pop()
            # 그 외의 경우는 멈춘다.
            else:
                break
        # 만약 for문이 마지막까지 도달했고, stack이 비어있다면 ans에 1 할당
        if i == len(info)-1 and stack == []:
            ans = 1
    # 테스트 케이스 번호와 답 출력
    print(f'#{case} {ans}')