import math, sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

a = S.count('C')
b = len(S) - a

print(math.ceil(a/(b+1)))