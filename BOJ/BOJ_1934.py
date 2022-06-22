import math
import sys
# 테스트 케이스 수
T = int(sys.stdin.readline())

for _ in range(T):
    # 최소공배수를 구해야하는 수 A, B
    A, B = map(int, sys.stdin.readline().split())
    # print(math.lcm(A, B))

    # 유클리드 호제법을 활용하기 위해
    # 첫 나눗셈을 진행한다.
    # 나머지는 remainder, 나눠지는 수는 number
    remainder = max(A,B) % min(A,B)
    number = min(A, B)
    while True:
        # 나머지가 0이되면 최대 공약수인 number를 활용하여 최대공약수 출력
        # while문을 break
        if remainder == 0:
            print(number * A//number * B//number)
            break
        # number, remainder를 재 정의한다.
        number, remainder = remainder, number % remainder