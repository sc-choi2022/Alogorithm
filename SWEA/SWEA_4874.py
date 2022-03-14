import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    info = list(input().split())
    sign = ['+', '-', '*', '/']
    stack = []

    ans = 'error'
    # info의 모든 값에 대해
    for i in range(len(info)):
        if info[i]=='.':
            if len(stack) == 1:
                print(f'#{case} {stack[0]}')
            else:
                print(f'#{case}', 'error')
        # sign에 속하지 않는다면 숫자이기 때문에 int로 형변환 후 stack에 추가
        elif info[i] not in sign:
            stack.append(int(info[i]))
        # stack에 최소 2개 있어야 연산이 가능
        elif len(stack) >= 2:
            # pop으로 꺼낸 값을 temp1, temp2에 할당하여 사칙연산 하고 stack에 추가
            temp1 = stack.pop()
            temp2 = stack.pop()
            # info[i] 값에 따라 사칙연산 진행 후 stack에 추가
            if info[i] == '+':
                stack.append(temp2 + temp1)
            elif info[i] == '-':
                stack.append(temp2 - temp1)
            elif info[i] == '*':
                stack.append(temp2 * temp1)
            elif info[i] == '/':
                stack.append(int(temp2 // temp1))
        # 그 외의 경우 error 출력하고 for문 탈출
        else:
            print(f'#{case}', 'error')
            break
