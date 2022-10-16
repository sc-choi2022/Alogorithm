import sys
from itertools import product

# 금민수를 확인하는 범위가 되는 A, B
A, B = map(int, sys.stdin.readline().split())

lenA, lenB = len(str(A)), len(str(B))

cnt = 0

for i in range(lenA, lenB + 1):
    numbers = list(product([4, 7], repeat=i))
    for num in numbers:
        N = int(''.join(map(str, num)))
        if A <= N <= B:
            cnt += 1
print(cnt)