import sys
# 수열 A의 크기 N
N = int(sys.stdin.readline())

A = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0]*N
maximum = max(A)

for i in range(N):
    cnt = 0
    up = 1
    for j in range(i):
        if A[j] < A[i]:
            cnt += 1
    for jj in range(i+1, N):
        if A[j] > A[i]:
            cnt += 1


print(dp)