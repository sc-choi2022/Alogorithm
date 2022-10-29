import sys, math

# 자연수 A, B
A, B = map(int, sys.stdin.readline().split())

div = B // A
a, b = 1, div
for i in range(1, div//2 + 1):
    if not div % i:
        c = i
        d = div//i
        if math.gcd(c, d) != 1:
            continue
        if a + b > c + d:
            a = c
            b = d
print(a*A, b*A)