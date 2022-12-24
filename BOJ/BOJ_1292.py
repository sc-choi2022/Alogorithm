import sys

# 구간의 시작과 끝을 나타내는 정수 A, B
A, B = map(int, sys.stdin.readline().split())
# 수열을 만들 배열 numbers
numbers = []

# for문을 통해 구간의 수열을 생성
for i in range(1, B + 1):
    for j in range(i):
        numbers.append(i)

# 구간에 속하는 숫자의 합을 출력
print(sum(numbers[A - 1:B]))