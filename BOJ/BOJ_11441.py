import sys

# 수의 개수 N
N = int(sys.stdin.readline())
# 수를 저장하는 배열 numbers
numbers = [0] + list(map(int, sys.stdin.readline().split()))
summation = [0] * (N+1)
summation[1] = numbers[1]
for i in range(2, N+1):
    summation[i] = summation[i-1] + numbers[i]

# 구간의 개수 M
M = int(sys.stdin.readline())
for _ in range(M):
    # 구간을 나타내는 L, R
    L, R = map(int, sys.stdin.readline().split())
    # 주어진 구간의 합을 출력
    print(summation[R]-summation[L-1])