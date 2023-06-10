import sys

# 테스트케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 수첩 1에 적어 놓은 정수의 개수 N
    N = int(sys.stdin.readline())
    numbers1 = set(map(int, sys.stdin.readline().split()))
    # 수첩 2에 적어 놓은 정수의 개수 M, M개의 입력
    M = int(sys.stdin.readline())
    numbers2 = list(map(int, sys.stdin.readline().split()))

    for number in numbers2:
        if number in numbers1:
            print(1)
        else:
            print(0)