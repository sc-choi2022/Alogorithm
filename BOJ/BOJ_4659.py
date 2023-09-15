import sys

while True:
    # 주어지는 패스워드 password
    password = sys.stdin.readline().rstrip()
    if password == 'end':
        break
    # password의 길이 L
    L = len(password)
    # 연속되는 자음 혹은 모음의 개수를 저장하는 배열 lst
    lst = [1]*L
    # 모음을 저장하는 배열 vowel
    vowel = ['a', 'e', 'i', 'o', 'u']
    # 패스워드의 가능 여부를 저장하는 flag
    flag = False
    # 모음여부를 저장하는 check, 모음의 개수를 저장하는 변수 cnt
    check = True if password[0] in vowel else False
    cnt = 1 if password[0] in vowel else 0

    for i in range(1, L):
        # 패스워드 조건을 벗어나는 경우
        if flag:
            break
        # password[i]의 모음 여부 tmp
        tmp = True if password[i] in vowel else False
        cnt += 1 if password[i] in vowel else 0
        # 모음 혹은 자음이 연속되는 경우
        if check == tmp:
            lst[i] = lst[i-1] + 1
        # check값을 tmp값으로 갱신
        check = tmp
        # 같은 알파벳이 연속되는 경우
        if password[i-1] == password[i]:
            # 연속되는 것이 가능한 알파벳인 경우
            if password[i] == 'e' or password[i] == 'o':
                continue
            else:
                flag = True
        # 모음이 3개 혹은 자음이 3개 연속으로 오는 경우
        if lst[i] == 3:
            flag = True
    # 모음을 포함하지 않는 경우
    if not cnt:
        flag = True

    # '예제 출력'의 형태에 기반하여 품질을 평가
    print(f'<{password}> is ', end='')
    print('not acceptable.' if flag else 'acceptable.')