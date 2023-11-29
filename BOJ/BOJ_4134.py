import sys

def isPrime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 정수 N
    N = int(sys.stdin.readline())
    while True:
        if isPrime(N):
            print(N)
            break
        else:
            N += 1