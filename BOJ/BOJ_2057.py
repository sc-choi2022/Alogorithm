import sys

# 정수 N
N = int(sys.stdin.readline())
# 팩토리얼을 저장하는 배열 factorial
factorial = [1, 1] + [0]*19
for i in range(2, 21):
    factorial[i] = factorial[i-1]*i