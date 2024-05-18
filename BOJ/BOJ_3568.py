import sys

# 기본 변수명 variable, 주어지는 선언문 declarations
variable, *declarations = sys.stdin.readline().rstrip().split()

for declaration in declarations:
    declaration = declaration.replace(',', '').replace(';', '')
    alphabet, tmp = '', ''
    for d in declaration:
        if d.isalpha():
            alphabet += d
        else:
            tmp += d

    tmp = tmp[::-1].replace('][', '[]')
    # 입력으로 주어진 변수 선언문을 문제의 조건에 맞게 변형한 뒤, 한 줄에 하나씩 출력
    print(variable+tmp, alphabet+';')