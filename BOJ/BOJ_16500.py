import sys

S = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
L = len(S)
dp = [0] * L
dp[0] = 1

for _ in range(N):
    A = sys.stdin.readline().rstrip()