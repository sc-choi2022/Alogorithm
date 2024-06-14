import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 두 이진수 N, M
    N, M = sys.stdin.readline().rstrip().split()
    # 이진수 N에서 바꿔야하는 0의 개수 zero, 1의 개수 one
    zero, one = 0, 0

    for i in range(len(N)):
        if N[i] != M[i]:
            if N[i] == '1':
                one += 1
            else:
                zero += 1

    # 두 수의 비트 우정지수를 출력
    print(max(zero, one))