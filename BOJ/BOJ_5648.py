import sys

N, *numbers = sys.stdin.read().split()

# 원소를 거꾸로 뒤집고 오름차순으로 정렬
for i in range(int(N)):
    numbers[i] = int(numbers[i][::-1])
numbers = sorted(list(numbers))

for number in numbers:
    print(number)