import sys

# 유클리드 호제법
def gcd(A, B):
    while B != 0:
        A, B = B, A%B
    return A

# 두 자연수 A와 B
A, B = map(int, sys.stdin.readline().split())
# A와 B의 최대공약수를 출력
print('1' * gcd(A, B))