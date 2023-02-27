import sys

# 거스름돈 액수 N
N = int(sys.stdin.readline())

five = N // 5
two = (N % 5) // 2

if (N % 5) % 2:
    five -= 1
    two += 3

if five == -1:
    print(-1)
else:
    print(five + two)

# dp