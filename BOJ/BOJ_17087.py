import sys

def GCD(a, b):
    while b:
        mod = b
        b = a%b
        a = mod
    return a

N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

Ds = list(set(abs(A[i]-S) for i in range(N)))
D = min(Ds)

for i in range(N):
    D = GCD(Ds[i], D)

print(D)