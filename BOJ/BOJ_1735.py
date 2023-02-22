import sys

def gcd(numerator, denominator):
    while numerator % denominator:
        mod = numerator % denominator
        numerator = denominator
        denominator = mod
    return denominator

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

g = gcd(a*d+b*c, b*d)
print((a*d+b*c)//g, (b*d)//g)
