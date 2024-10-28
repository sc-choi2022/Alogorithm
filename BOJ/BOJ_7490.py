import sys

def backtracking(idx, eq):
    if idx == N-1:
        equations.append(eq+numbers[idx])
        return

    eq += numbers[idx]
    backtracking(idx+1, eq+' ')
    backtracking(idx+1, eq+'+')
    backtracking(idx+1, eq+'-')

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 자연수 N
    N = int(sys.stdin.readline())
    # 수식의 숫자를 저장하는 배열 numbers
    numbers = [str(i) for i in range(1, N+1)]
    equations = []
    backtracking(0, '')

    for equation in equations:
        # 수식의 값이 0인 경우
        if eval(equation.replace(' ', '')) == 0:
            print(equation)

    print()