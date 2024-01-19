import sys

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y:
        x %= y
        x, y = y, x
    return x

N, M = map(int, sys.stdin.readline().split(':'))
# N과 M의 최대공약수 G
G = gcd(N, M)
# 최대 공약수로 약분하여 출력
print(f'{N//G}:{M//G}')