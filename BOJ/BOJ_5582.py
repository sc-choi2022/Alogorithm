import sys

# 문자열1, 문자열2인 string1, string2
string1 = sys.stdin.readline().rstrip()
string2 = sys.stdin.readline().rstrip()
# 문자열1의 길이 N1, 문자열2의 길이 N2
N1, N2 = len(string1), len(string2)
dp = [[0]*(N2+1) for _ in range(N1+1)]
answer = 0
for i in range(1, N1+1):
    for j in range(1, N2+1):
        if string1[i-1] == string2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
    answer = max(answer, max(dp[i]))

# 두 문자열에 모두 포함 된 부분 문자열 중 가장 긴 것의 길이를 출력
print(answer)