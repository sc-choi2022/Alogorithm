import sys, math

N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

Ds = [set(abs(A[i]-S) for i in range(N))]
D = min(Ds)

for i in range(N):
    continue

print(D)