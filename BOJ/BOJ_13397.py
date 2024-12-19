import sys

def divide(num):
    num0, num1 = numbers[0], numbers[0]

# 1차원 배열에 저장된 수의 개수 N, 구간의 최대개수 M
N, M = map(int, sys.stdin.readline().split())

# N개의 수가 들어있는 1차원 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))

# 최댓값의 최솟값
answer = max(numbers)

left, right = 0, max(numbers)

while left <= right:
    middle = (right-left)//2
