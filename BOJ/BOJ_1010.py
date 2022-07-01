import sys
# 테스트케이스 개수
T = int(sys.stdin.readline())

for _ in range(T):
    K, N = map(int, sys.stdin.readline().split())
    # N와 K를 활용하여 permutation을 구하는 방법으로 다리의 개수를 구하려고 한다.
    number = 1
    multiply = N
    # 분자의 값을 N부터 N-K+1까지 팩토리얼로 곱한다.
    while True:
        if multiply == (N - K):
            break
        number *= multiply
        multiply -= 1
    divide = K
    # 분모의 값을 K부터 2까지 나눈다.
    while True:
        # 나누는 값이 1이거나 0이되어 Zero division Error가 발생한 수 경우 break
        if divide <= 1:
            break
        number //= divide
        divide -= 1
    # 계산을 마치고 number을 출력
    print(number)