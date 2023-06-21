import sys

# 날짜의 일의 자리 숫자 N
N = int(sys.stdin.readline())

# 5대의 자동차 번호의 일의 자리 숫자
numbers = list(map(int, sys.stdin.readline().split()))

# 10부제를 위반하는 차량의 대수 출력
print(numbers.count(N))