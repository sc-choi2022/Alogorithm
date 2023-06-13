import sys

# 체스판의 세로 길이 N, 가로 길이 M
N, M = map(int, sys.stdin.readline().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, (M-1)//2+1))
elif M <= 6:
    print(min(4, M))
else:
    print(M-2)