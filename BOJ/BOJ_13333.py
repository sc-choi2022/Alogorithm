import sys

N = int(sys.stdin.readline())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

M = numbers[-1]
Q = 0

for i in range(M, 1, -1):
    tmp = list(filter(lambda x: x >= i, numbers))
    if len(tmp) >= i:
        Q = i
        break
print(Q)