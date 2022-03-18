import sys
sys.stdin = open('input.txt')

# 계산을 하기위해 후위표기식으로 리스트 equation에 담는다.
def postorder(node): #후위표기식
    if 0<node<=N:
        postorder(left[node])
        postorder((right[node]))
        equation.append(tree[node])

for case in range(1, 10 + 1):
    N = int(input())
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    tree = [0] * (N + 1)
    equation = []
    for i in range(N):
        tmp = list(input().split())
        # tmp의 길이에 따라 left, right, tree에 값을 추가
        if len(tmp) == 4:
            left[int(tmp[0])] = int(tmp[2])
            right[int(tmp[0])] = int(tmp[3])
            tree[int(tmp[0])] = tmp[1]
        elif len(tmp) == 2:
            tree[int(tmp[0])] = int(tmp[1])

    # 후위표기법으로 받아서 계산하기
    postorder(1)

    # 스택을 활용하여 후위표기법을 계산
    stack = []
    for numb in equation:
        if numb not in ['+', '-', '*', '/']:
            stack.append(numb)
        else:
            b = stack.pop()
            a = stack.pop()
            if numb == '+':
                stack.append(a + b)
            elif numb == '-':
                stack.append(a - b)
            elif numb == '*':
                stack.append(a * b)
            elif numb == '/':
                stack.append(a / b)

    # stack에 남은 수를 정수형태로 ans에 할당
    ans = int(stack[0])
    # 테스트케이스 수와 ans 출력
    print(f'#{case} {ans}')
