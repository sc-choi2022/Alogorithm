import sys

# 주어지는 괄호
S = sys.stdin.readline().rstrip()
while '()' in S:
    S = S.replace('()', '')
# S를 올바른 괄호열으로 만들기 위해 앞과 뒤에 붙여야 할 괄호의 최소 개수를 출력
print(len(S))