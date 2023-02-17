import sys

# 곡의 개수 A, 저작권이 있는 멜로디의 평균값 I
A, I = map(int, sys.stdin.readline().split())
# 적어도 몇 곡이 저작권이 있는 멜로디인지 출력
print((I - 1) * A + 1)