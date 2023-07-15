import sys

def java2C():
    print(lst[0], end='')
    for j in range(1, L):
        if lst[j].isupper():
            print('_', end='')
            lst[j] = lst[j].lower()
        print(lst[j], end='')

def C2java():
    for j in range(1, L):
        if lst[j] == '_':
            lst[j] = ''
            if j+1 < L:
                lst[j+1] = lst[j+1].upper()
    print(''.join(lst))

# 변수명을 담을 배열 lst
lst = list(sys.stdin.readline().rstrip())
# lst의 길이 L
L = len(lst)

# 조건 1: 대문자, 조건 2: _ 존재 여부
# java인 경우 조건1 True, 조건 2 False, 첫문자 소문자
# C++인 경우 조건 1 False, 조건 2 True
flag1, flag2 = False, False
for i in range(L):
    if lst[i].isupper():
        flag1 = True
    elif lst[i] == "_":
        flag2 = True
if (flag1 and flag2) or (not flag1 and not flag2):
    print('Error!')
elif flag1 and not flag2:
    java2C()
else:
    C2java()