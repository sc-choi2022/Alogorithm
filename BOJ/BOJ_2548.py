import sys

# 자연수의 개수 N
N = int(sys.stdin.readline())
# N개의 자연수를 정렬
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

# N이 홀수인 경우
if N%2:
    print(numbers[N//2])
# N이 짝수인 경우
else:
    print(numbers[N//2-1])