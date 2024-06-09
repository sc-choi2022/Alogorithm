import sys

# 원소의 개수 N, 원소를 저장하는 numbers
N, *numbers = sys.stdin.read().split()

# 원소를 거꾸로 뒤집고 오름차순으로 정렬
for i in range(int(N)):
    numbers[i] = int(numbers[i][::-1])
numbers = sorted(list(numbers))

# 오름차순으로 정렬하고 출력
for number in numbers:
    print(number)