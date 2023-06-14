import sys

# 테스트케이스 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 날의 수 N
    N = int(sys.stdin.readline())
    # 주가를 담은 배열 stocks
    stocks = list(map(int, sys.stdin.readline().split()))
    idx = 0
    numbers = stocks[::]
    numbers.sort(reverse=True)
    answer = 0
