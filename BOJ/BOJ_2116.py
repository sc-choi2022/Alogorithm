import sys

# 주사위의 개수 N
N = int(sys.stdin.readline())

for _ in range(N):
    # 주사위 각 면에 적혀진 숫자를 저장하는 배열 numbers
    numbers = list(map(int, sys.stdin.readline().split()))
    