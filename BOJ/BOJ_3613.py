import sys

# Java
# 첫 단어는 소문자, 다음 단어부터는 첫 문자만 대문자로 쓴다.
# 모든 단어를 붙여쓴다.
# javaIdentifier, longAndMnemonicIdentifier

# C++
# 소문자만 사용
# 단어구분은 _으로 이용
# c_identifier, long_and_mnemonic_identifier

# 1. 언어 형식 확인
# 2. 반대 형식으로 변수명을 출력
# 둘 다 아닌 경우 Error 출력

# 주어지는 변수명 name
name = sys.stdin.readline().rstrip()

if name[-1] == '_' or name[0] == '_' or '__' in name or name[0].isupper():
    print('Error!')
else:
    # check = [0, 0] Jave, C+= 여부
    check = [0, 0]

    for n in name:
        if n.isupper():
            check[0] = 1
        elif n == '_':
            check[1] = 1
        if sum(check) == 2:
            print('Error!')
            exit()

    # C++
    if check[1]:
        word = name.split('_')
        print(word[0], end='')
        for i in range(1, len(word)):
            print(word[i][0].upper()+word[i][1:], end='')
    # Java
    else:
        print(name[0], end='')
        tmp = ''
        for i in range(1, len(name)):
            if name[i].isupper():
                print(tmp+'_'+name[i].lower(), end='')
                tmp = ''
            else:
                tmp += name[i]
        if tmp:
            print(tmp)