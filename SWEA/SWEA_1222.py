import sys
sys.stdin = open('input.txt')

for case in range(1, 10 + 1):
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
        # 만약 숫자라면 바로 문자열 ans에 더해진다.
        if ls.isdecimal():
            ans += ls
        # 아닌 경우
        else:
            # stack안에 값이 있다면 그 값을 ans에 더하고 stack에 ls를 추가한다.
            if stack:
                ans += stack.pop()
                stack.append(ls)
            # stack이 비어있다면 stack에 ls를 추가
            else:
                stack.append(ls)
    # stack에 남은 값을 ans에 더해 후위 표기식 완성
    ans += stack.pop()
    # pop을 사용하기 위해 후위표기식을 리스트 post에 담는다.
    post = list(ans)

    # post가 빌때까지
    while post:
        # 가장 앞의 값을 변수 temp에 할당
        temp = post.pop(0)
        # 숫자라면 stack에 int값으로 추가
        if temp.isdecimal():
            stack.append(int(temp))
        # 숫자가 아니라면 숫자 2개를 pop하여 +를 수행후 stack에 다시 추가
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
    # 테스트케이스와 stack[0] 값을 출력
    print(f'#{case} {stack[0]}')