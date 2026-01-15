from itertools import product
import sys

# N자리수
N = int(sys.stdin.readline())
# 3개 숫자(0,1,2)만 가지고 만들수있는 문자열 P
P = list(map(int, list(map(''.join, list(product(('0', '1', '2'), repeat=N))))))

# 0, 1, 2만 가지고 만들 수 있는 N자리 3의 배수의 개수
answer = 0

# 3자리 수 인 3의 배수 구분하는 for문
for p in P:
    if p%3 == 0 and p//int('1'+'0'*(N-1)):
        answer += 1

# answer 출력
print(answer)