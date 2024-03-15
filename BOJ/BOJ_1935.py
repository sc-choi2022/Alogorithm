import sys

# 피연산자의 개수 N
N = int(sys.stdin.readline())
# 후위 표기식 equation
equation = list(sys.stdin.readline().rstrip())
# 피연산자의 대응되는 숫자를 저장하는 딕셔너리 number
number = dict()
# 피연산자를 딕셔너리 number에 저장
for i in range(65, 65+N):
    number[chr(i)] = int(sys.stdin.readline())

stack = []
for e in equation:
    if e.isalpha():
        stack.append(number[e])
    else:
        b = stack.pop()
        a = stack.pop()
        if e == '+':
            stack.append(a+b)
        elif e == '-':
            stack.append(a-b)
        elif e == '*':
            stack.append(a*b)
        else:
            stack.append(a/b)

# 계산 결과를 소숫점 둘째 자리까지 출력
print('{:.2f}'.format(stack.pop()))