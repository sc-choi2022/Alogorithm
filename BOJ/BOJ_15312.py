import sys
from collections import defaultdict

alphabet = defaultdict(int)
number = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
for i in range(26):
    alphabet[chr(65+i)] = number[i]

A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())
L = len(A)
AB = [[0]*(2*L) for _ in range(2*L-1)]
for j in range(L):
    AB[0][2*j] = alphabet[A[j]]
    AB[0][2*j+1] = alphabet[B[j]]

for ii in range(1, 2*L-1):
    for jj in range(ii, 2*L):
        AB[ii][jj] = (AB[ii-1][jj-1] + AB[ii-1][jj])%10

print(str(AB[2*L-2][2*L-2])+str(AB[2*L-2][2*L-1]))