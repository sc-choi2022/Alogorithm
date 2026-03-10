import sys

# 일변수 다항식
E = sys.stdin.readline().rstrip()

if E[:2] == '-x':
    E = E.replace('-x', '-1x')

# E의 미분한 결과를 출력
if 'x' in E:
    if E[0] == 'x':
        print(1)
    else:
        print(list(map(str, E.split('x')))[0])
else:
    print(0)