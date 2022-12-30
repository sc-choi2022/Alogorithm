import sys

# 두개의 문자열 S1, S2
S1 = ' ' + sys.stdin.readline().rstrip()
S2 = ' ' + sys.stdin.readline().rstrip()

# dp을 활용할 배열 dp
dp = [[0]*(len(S2)) for _ in range(len(S1))]

for i in range(1, len(S1)):
    for j in range(1, len(S2)):
        # 부분수열이 가능한 알파벳인 경우
        if S1[i] == S2[j]:
            # dp에 반영 i - 1행과 j - 1열의 값에 1을 더한다.
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            # 가장 긴 부분수열을 구하는 것이므로 이전 부분수열중 가장 큰 값을 i행 j열에 저장
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# 두 문자열의 LCS의 길이를 출력
print(dp[-1][-1])