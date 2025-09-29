from collections import deque
import sys

def check(sentence, lines):
    cnt = 0

    return 

# 앵무새의 수 N
N = int(sys.stdin.readline())

L = [deque(map(str, sys.stdin.readline().split())) for _ in range(N)]
S = list(sys.stdin.readline().rstrip().split())

if check(S, L):
    print('Possible')
else:
    print('Impossible')