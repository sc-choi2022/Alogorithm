import sys

# 두 문자열 S1, S2
S1 = sys.stdin.readline().rstrip()
S2 = sys.stdin.readline().rstrip()
# 문자열 S1, S2의 길이 L1, L2
L1, L2 = len(S1), len(S2)

# LCS를 저장하는 배열 dp
dp = [['']*L2 for _ in range(L1)]

for i in range(1, L1):
    for j in range(1, L2):
        if S1[i] == S2[j]:
            dp[i][j] = dp[i-1][j-1] + S1[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

# LCS의 길이 출력
print(len(dp[L1][L2]))
# LCS의 길이가 0이 아닌 경우 LCS를 출력
if len(dp[L1][L2]):
    print(dp[L1][L2])