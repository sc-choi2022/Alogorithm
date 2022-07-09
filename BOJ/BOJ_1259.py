# 0이 나오기 전까지 진행하는 while문
while True:
    # 숫자 N을 slicing을 활용하기 위해 string 값으로 받는다.
    N = input()
    # 만약 N이 0이라면 break
    if N == '0':
        break
    # 팰린드롭수가 맞다면 yes 출력
    if N == N[::-1]:
        print('yes')
    else:
        # 아니라면 no 출력
        print('no')