from collections import deque
import sys

def check(sentence, lines):
    cnt = 0

    i = 0
    while sentence:
        if lines[i] and sentence[0] == L[0]:
            lines[i].popleft()
            sentence.popleft()
            cnt = 0
        else:
            if cnt == N:
                return False
            cnt += 1
        i = (i+1)%N

    E = 0
    for j in range(N):
        if not len(lines[j]):
            E += 1

    if not sentence and E == N:
        return True
    else:
        return False

# 앵무새의 수 N
N = int(sys.stdin.readline())

L = [deque(map(str, sys.stdin.readline().split())) for _ in range(N)]
S = deque(list(sys.stdin.readline().rstrip().split()))

if check(S, L):
    print('Possible')
else:
    print('Impossible')