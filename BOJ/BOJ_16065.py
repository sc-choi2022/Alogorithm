import sys

# length of the base sequence
N = int(sys.stdin.readline())
# N numbers that forming the base sequence
numbers = list(map(int, sys.stdin.readline().split()))
# 1st number of (N+1)th non-negative sequence, num
num = 0
# range (minNum~maxNum)
minNum, maxNum = 0, int(1e8)
for i in range(N):
    num = numbers[i] - num
    # even
    if not i%2:
        maxNum = min(maxNum, num)
    else:
        minNum = max(minNum, -num)
# number of non-negative integer sequences
if maxNum >= minNum:
    print(maxNum-minNum+1)
# none at all satisfying this conditions
else:
    print(0)