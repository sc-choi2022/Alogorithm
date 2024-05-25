import sys

def dfs(idx, left, right, e):
    return

# 음이 아닌 정수로 이루어진 수식 equation
equation = list(sys.stdin.readline().rstrip())
L = len(equation)
results = set()
tmp = ''
for i in range(1, L):
    if equation[i] == '(':
        continue

results = sorted(list(results))
for result in results:
    print(result)