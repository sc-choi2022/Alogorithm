import sys

def gcd(A, B):
    mod = A%B
    while mod > 0:
        A = B
        B = mod
        mod = A%B
    return B

# 두 자연수 A와 B
A, B = map(int, sys.stdin.readline().split())
# A와 B의 최대공약수를 출력
print('1' * gcd(A, B))