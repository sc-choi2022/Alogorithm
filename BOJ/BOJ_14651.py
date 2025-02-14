import sys

# 입력받은 자리 수 N
N = int(sys.stdin.readline())

if N == 1:
    print(0)
else:
    # 0, 1, 2만 가지고 만들 수 있는 N자리 3의 배수의 개수를 출력
    print((3**(N-2)*2) % 1000000009)