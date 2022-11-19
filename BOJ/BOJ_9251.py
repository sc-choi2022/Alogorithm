from itertools import combinations
import sys

S1 = ' ' + sys.stdin.readline().strip()
S2 = ' ' + sys.stdin.readline().strip()
dp = [[0] * len(S2) for _ in range(len(S1))]

for i in range(1, len(S1)):
    for j in range(1, len(S2)):
        if S1[i] == S2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])