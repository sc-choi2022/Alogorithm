import sys

A, K = map(int, sys.stdin.readline().split())
cnt = 0

while True:
    if A == K:
        print(cnt)
    if K%2 == 0 and K >= 2*A:
        K = K//2
    else:
        K -= 1
    cnt += 1