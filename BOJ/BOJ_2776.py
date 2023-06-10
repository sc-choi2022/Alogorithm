import sys

# 테스트케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 수첩 1에 적어 놓은 정수의 개수 N와 N개의 숫자를 담은 set number1
    N = int(sys.stdin.readline())
    numbers1 = set(map(int, sys.stdin.readline().split()))
    # 수첩 2에 적어 놓은 정수의 개수 M, M개의 숫자를 담을 배열 numbers2
    M = int(sys.stdin.readline())
    numbers2 = list(map(int, sys.stdin.readline().split()))

    # ‘수첩2’에 적혀있는 순서대로, 각각의 수에 대하여, ‘수첩1’에 있으면 1을, 없으면 0을 출력
    for number in numbers2:
        if number in numbers1:
            print(1)
        else:
            print(0)