import sys

# 정수의 개수 N
N = int(sys.stdin.readline())
# N개의 정수를 저장하는 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
# 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력
print(numbers[0], numbers[-1])