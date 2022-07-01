import sys
# 이항계수를 구하는 자연수 N, 정수 K
N, K = map(int, sys.stdin.readline().split())

# K가 0보다 작거나 K가 N보다 크다면 0을 출력
if K < 0 or K > N:
    print(0)
else:
    # 이항계수의 규칙에 따라 계산하기 위해 계산 전 변수 number를 1로 초기화
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
    # 계산을 마치고 number을 10007로 나눈 값을 출력
    print(number%10007)