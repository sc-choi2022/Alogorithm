import sys

# 한 더미의 카드의 개수 N
N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

dp = [[0]*N for _ in range(N)]

for i in range(1, N):
    for j in range(1, N):
        if A[i] == B[j]:
            continue

print(dp[-1][-1])