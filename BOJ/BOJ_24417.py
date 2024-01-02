import sys

N = int(sys.stdin.readline())

x, y = 1, 1
for _ in range(N-2):
    y, x = (x+y)%1000000007, y

print(y, N-2)