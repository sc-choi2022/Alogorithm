import sys

# 중위 표기식
infix = list(sys.stdin.readline().rstrip())
# 후위 표기식을 위해 활용할 배열 stack
stack = []
# 출력할 후위 표기식 ans
ans = ''

for i in infix:
    # 연산자 혹은 괄호가 아닌 경우 ans에 추가
    if i.isalpha():
        ans += i
    else:
        # 여는 괄호인 경우 stack에 저장
        if i == '(':
            stack.append(i)
        # 연산자 * 혹은 / 인 경우
        elif i == '*' or i == '/':
            # stack이 비어있지 않고 다음 * 혹은 / 가 나오기 전까지
            while stack and stack[-1] in ('*', '/'):
                # stack.pop()의 값을 ans에 추가
                ans += stack.pop()
            # stack에 연산자를 저장
            stack.append(i)
        # 연산자 + 혹은 - 인 경우
        elif i == '+' or i == '-':
            # stack이 비어있지 않고 (가 나오기 전까지
            while stack and stack[-1] != '(':
                # stack.pop()의 값을 ans에 추가
                ans += stack.pop()
            # stack에 연산자를 저장
            stack.append(i)
        # 닫는 괄호인 경우
        elif i == ')':
            # stack이 비어있지 않고 (가 나오기 전까지
            while stack and stack[-1] != '(':
                # stack.pop()의 값을 ans에 추가
                ans += stack.pop()
            # (를 stack에서 제거
            stack.pop()

# stack의 값들을 ans에 반영
while stack:
    ans += stack.pop()
# 후위 표기식을 출력
print(ans)