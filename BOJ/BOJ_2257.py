import sys

# 원소의 질량을 저장하는 딕셔너리 mass
mass = {'H': 1, 'C': 12, 'O': 16}

formula = sys.stdin.readline().rstrip()
stack = []

for f in formula:
    if f.isalpha():
        stack.append(mass[f])
    elif f == '(':
        stack.append(f)
    else:
        tmp = 0