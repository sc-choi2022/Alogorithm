from copy import deepcopy
import sys

def backtracking(lst):
    if len(lst) == N - 1:
        operators.append(deepcopy(lst))
        return
    lst.append(' ')
    backtracking(lst)
    lst.pop()

    lst.append('+')
    backtracking(lst)
    lst.pop()

    lst.append('-')
    backtracking(lst)
    lst.pop()

# 테스트케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    operators = []
    # 자연수 N
    N = int(sys.stdin.readline())
    backtracking([])

    numbers = [i for i in range(1, N+1)]

    for operator in operators:
        equation = ''
        for j in range(N-1):
            equation += str(numbers[j]) + operator[j]
        equation += str(numbers[-1])
        if eval(equation.replace(' ', '')) == 0:
            print(equation)
    print()