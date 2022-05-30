# 테스트 케이스의 수가 주어지지 않았기 떄문에 while문
while True:
    # 첫번째 숫자 a, 두번째 숫자 b
    a, b = map(int, input().split())
    # ZeroDivisionError 제거
    if a == 0 and b == 0:
        break
    # 첫 번째 숫자가 두 번째 숫자의 약수인 경우 factor 출력
    if b % a == 0:
        print('factor')
    # 첫 번째 숫자가 두 번째 숫자의 배수인 경우 multiple 출력
    elif a % b == 0:
        print('multiple')
    # 위 두 조건에 맞지 않는 경우 neither 출력
    else:
        print('neither')