import sys

# 2진수
bi = sys.stdin.readline().rstrip()
# 2진수를 8진수로 변환한 값을 출력
print(oct(int(bi, 2))[2:])