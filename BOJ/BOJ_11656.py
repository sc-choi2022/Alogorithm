import sys

S = sys.stdin.readline().strip()
N = len(S)
lst = [0] * N

for i in range(N):
    lst[i] = S[i:]

lst.sort()
for l in lst:
    print(l)