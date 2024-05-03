import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

answer = 0
tmp = sum(A)

for i in range(N-1):
    tmp -= A[i]
    answer += A[i] * tmp

print(answer)