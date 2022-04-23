import sys
sys.stdin = open('input.txt')

for case in range(1, 10+1):
    N = int(input())
    # 계산식을 equation 변수에 할당
    equation = input()

    # 후위 표기법으로 만들기
    # 활용할 스택과 결과 값을 담을 리스트 stack, answer
    stack = []
    answer = []

    # 계산식의 각 값에 대한 for문
    for eq in equation:
        # 숫자라면 answer에 추가
        if eq.isdigit():
            answer.append(eq)
        # 숫자가 아닌 경우 우선 순위에 따라 진행
        else:
            if eq == '(':
                stack.append(eq)
            elif eq == ')':
                temp = stack.pop()
                # )의 경우 스택의 top이 ( 일때까지 answer에 추가한다.
                while temp != '(':
                    answer.append(temp)
                    temp = stack.pop()
            elif eq == '*':
                # stack이 비어있지 않고 top의 값이 *와 /일 때 answer에 top값 추가
                while len(stack)>0 and stack[-1] == '*' or stack[-1] == '/':
                    answer.append(stack.pop())
                stack.append(eq)
                # stack이 비어있지 않고 top의 값이 +와 -일 때 answer에 top값 추가
            elif eq == '+':
                while len(stack)>0 and stack[-1] != '(':
                    answer.append(stack.pop())
                stack.append(eq)
    for _ in range(len(stack)):
        answer.append(stack.pop())

    # 후위 표기법 계산
    c_stack = []
    for i in range(len(answer)):
        if answer[i].isdigit():
            c_stack.append(int(answer[i]))
        elif answer[i] == '+':
            a = c_stack.pop()
            b = c_stack.pop()
            c_stack.append(a+b)
        elif answer[i] == '*':
            a = c_stack.pop()
            b = c_stack.pop()
            c_stack.append(a*b)
    print(f'#{case} {c_stack[0]}')
