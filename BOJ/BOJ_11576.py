import sys

# 진법 A, 진법 B
A, B = map(int, sys.stdin.readline().split())
# A진법으로 나타낸 숫자의 자리수의 개수 M
M = int(sys.stdin.readline())
# A진법을 이루고 숫자를 저장하는 배열 numbers
numbers = reversed(list(map(int, sys.stdin.readline().split())))

ten = 0