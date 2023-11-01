import sys

# 테스트 케이스의 번호 case
case = 0
while True:
    # 주어지는 데이터 S
    S = list(sys.stdin.readline().rstrip())
    # 테스트 케이스 번호 1 증가
    case += 1
    # 입력의 마지막 줄인 경우 break
    if S[0] == '-':
        break

    stack = []
    # 문자열을 안정적으로 바꾸는데 필요한 연산 수 cnt
    cnt = 0
    for i in range(len(S)):
        # 빈 배열 stack에 닫는 괄호를 추가하는 경우
        # 닫는 괄호를 여는 괄호로 변경하는 연산 수행
        # cnt 1증가
        if not stack and S[i] == '}':
            cnt += 1
            stack.append('{')
        # 안정적인 문자 완성되는 경우
        elif stack and S[i] == '}':
            stack.pop()
        else:
            stack.append(S[i])
    # 남은 여는 괄호의 수의 절반을 닫는 괄호롤 바꾸는 연산 횟수만큼 cnt 증가
    cnt += len(stack)//2
    # 테스트 케이스 번호와 입력으로 주어진 문자열을 안정적으로 바꾸는데 필요한 최소 연산의 수를 출력
    print(f'{case}. {cnt}')