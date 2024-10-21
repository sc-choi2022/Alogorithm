import sys

# 테스트 케이스의 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 달력의 마지막 해의 정수 M, N, 구해야하는 해의 값 x, y
    M, N, x, y = map(int, sys.stdin.readline().split())
    # 구해야하는 k번째 해를 나타내는 변수 K
    K = -1

    tmp = x
    while tmp <= M*N:
        if not (tmp-y)%N:
            K = tmp
            break
        tmp += M

    # 정수 K 출력
    print(K)