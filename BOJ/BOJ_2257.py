import sys

# 원소의 질량을 저장하는 딕셔너리 mass
mass = {'H': 1, 'C': 12, 'O': 16}
# 화학식 formula
formula = sys.stdin.readline().rstrip()
stack = []

for f in formula:
    if f.isalpha():
        stack.append(mass[f])
    elif f == '(':
        stack.append(f)
    elif f == ')':
        # 묶인 괄호에 원자 질량의 합 tmp
        tmp = 0

        while True:
            if stack[-1] == '(':
                stack.pop()
                stack.append(tmp)
                break
            else:
                tmp += stack.pop()
    else:
        stack[-1] *= int(f)

# 화학식량을 출력
print(sum(stack))