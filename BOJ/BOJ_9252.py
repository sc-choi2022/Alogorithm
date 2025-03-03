import sys

S1 = sys.stdin.readline().rstrip()
S2 = sys.stdin.readline().rstrip()
L1, L2 = len(S1), len(S2)
dp = [['']*L2 for _ in range(L1)]