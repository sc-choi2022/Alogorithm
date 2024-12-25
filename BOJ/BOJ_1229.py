import sys

# 정수 N
N = int(sys.stdin.readline())
numbers = []
i, j = 1, 1

while True:
    if i*j <= N:
        numbers.append(i*j)
        i += 1
        j += 2
    else:
        break

dp = [0]
for i in range(N):
    tmp = float('inf')