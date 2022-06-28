import sys
# 소수 여부를 확인하는 함수 prime
def prime(number):
    # number가 1이면 False return
    if number == 1:
        return False
    # i가 number % i == 0이면 약수이므로 소수가 아니므고 False return
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    # for문에서 return되지 않았으면 True return
    return True

# 테스트 케이스 수 T
T = int(sys.stdin.readline())
for _ in range(T):
    # 주어지는 짝수 N
    N = int(sys.stdin.readline())
    # 제곱근이 a, b일 때 두 소수의 차이가 가장 작을 수 있으므로
    # a,b N//2으로 초기화
    a, b = N//2, N//2
    # a는 1 감소를 할 것이므로 소수가 아닌 자연수 1가 되기 전까지 while 실행
    while a > 1:
        # a와 b의 소수 여부를 확인하고 출력
        if prime(a) and prime(b):
            print(a, b)
            break
        # a 혹은 b가 소수가 아니라면 a 1 감소 b 1 증가
        else:
            a -= 1
            b += 1