from collections import deque
import sys

# 앵무새의 수 N
N = int(sys.stdin.readline())

L = deque([])

if check and L == len(R):
    print('Impossible')
elif not check and L != len(R):
    print('Possible')