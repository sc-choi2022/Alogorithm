import sys
# 주어지는 5개의 고유번호의 숫자
a, b, c, d, e = map(int, sys.stdin.readline().split())
# 주어진 조건에 맞게 검증수를 출력
print((a**2 + b**2 + c**2 + d**2 + e**2) % 10)