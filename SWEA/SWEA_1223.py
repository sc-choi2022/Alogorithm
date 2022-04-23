import sys
sys.stdin = open('input.txt')

for case in range(1, 10+1):
    # 문자열 계산식의 길이 n
    n = int(input())
    # 문자열 계산식을 담은 리스트 lst
    lst = input()
    # 바로 ans에 더해질 수 없는 값을 담을 리스트 stack
    stack = []
    # 만들어진 후위표기식을 담을 문자열 ans
    ans = ''

    # lst의 모든 값을 확인하기 위한 for문
    for ls in lst:
        # 우선순위가 높은 *이라면 stack에 추가
        if ls == '*':
            stack.append(ls)
        # *보다 우선순위가 낮은 +의 경우
        elif ls == '+':
            # stack이 비워질 때까지 and에 stack.pop을 더한다.
            while stack:
                ans += stack.pop()
            # stack에 ls추가
            stack.append(ls)
        else:
            # 피연산자는 ans에 더한다.
            ans += ls
    # stack에 남은 연산자들을 ans에 더한다.
    while stack:
        ans += stack.pop()
    # pop을 사용하기 위해 후위표기식을 리스트 post에 담는다.
    post = list(ans)

    # post가 빌때까지
    while post:
        # 가장 앞의 값을 변수 temp에 할당
        temp = post.pop(0)
        # 숫자라면 stack에 int값으로 추가
        if temp == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        # 숫자가 아니라면 숫자 2개를 pop하여 +를 수행후 stack에 다시 추가
        elif temp == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        else:
            stack.append(int(temp))

    # 테스트케이스와 stack[0] 값을 출력
    print(f'#{case} {stack[0]}')