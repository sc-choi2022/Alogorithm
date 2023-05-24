import sys

# 이어지는 마지막 수 N, 구하는 K번째 자리
N, K = map(int, sys.stdin.readline().split())

answer = 0
# 이어쓸 수 있는 숫자의 자리수 digit
digit = 1
# 각 자리수의 숫자는 9에 10의 제곱수 digit을 곱한만큼 존재
# 이를 활용할 수 nine을 9로 초기화
nine = 9

while K > digit*nine:
    K -= digit*nine
    answer += nine
    digit += 1
    nine *= 10

answer += (K-1) // digit + 1

if answer > N:
    print(-1)
else:
    print(str(answer)[(K-1)%digit])