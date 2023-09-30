import sys

N, M = map(int, sys.stdin.readline().split(':'))
n, m = N, M

for i in range(1, N+1):
    if n%i == 0 and m%i == 0:
        n //= i
        m //= i
print(f'{n}:{m}')