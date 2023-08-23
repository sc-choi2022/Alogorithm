import sys

dp = [0, 1, 2]

while True:
    # 범위 값인 두 정수 a, b
    a, b = map(int, sys.stdin.readline().split())
    # 입력의 마지막 줄인 경우
    if not a and not b:
        break