import sys
# 규칙에 따라 값을 구하여 D에 추가해주는 함수 dfs
def dfs(number):
    # number가 이미 D에 있다면
    if number in D:
        # number의 위치를 찾아 그 위치 이전까지의 D의 길이를 출력 후 return
        print(D.index(number))
        return
    # number가 D에 없다면 D를 추가
    D.append(number)
    # number로 만들어지는 최종 숫자 next
    next = 0
    # number가 0보다 클때 까지 while문 진행
    while number > 0:
        # %를 이용하여 일의 자리 수를 temp변수에 할당하고
        temp = number % 10
        # next에 temp의 P제곱을 더해준다.
        next += temp ** P
        # number는 //를 통해 재설정한다.
        number //= 10
    # while문을 활용하여 만든 next를 변수로 dfs 실행
    dfs(next)

# D의 시작 수 A, 제곱위치의 수 P
A, P = map(int, sys.stdin.readline().split())

# A부터 규칙에 따라 숫자를 담을 리스트 D
D = []

# D의 첫 숫자 A를 매게변수로 넣어 dfs 실행
dfs(A)