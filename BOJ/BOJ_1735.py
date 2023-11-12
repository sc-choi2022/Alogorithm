import sys

def gcd(numerator, denominator):
    while numerator%denominator:
        mod = numerator%denominator
        numerator = denominator
        denominator = mod
    return denominator

# 분자 A 분모 B
A, B = map(int, sys.stdin.readline().split())
# 분자 C 분모 D
C, D = map(int, sys.stdin.readline().split())

number = gcd(A*D+B*C, B*D)
print((A*D+B*C)//number, B*D//number)