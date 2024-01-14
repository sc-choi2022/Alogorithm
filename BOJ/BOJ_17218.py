import sys

# 두 개의 문자열 S1, S2
S1 = list(sys.stdin.readline().rstrip())
S2 = list(sys.stdin.readline().rstrip())
# S1, S2의 길이 N, M
N, M = len(S1), len(S2)
dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if S1[i] == S2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

answer = ''
while dp[N][M]:
    if dp[N][M] == dp[N][M-1]:
        M -= 1
    elif dp[N][M] == dp[N-1][M]:
        N -= 1
    else:
        answer += S1[N-1]
        N -= 1
        M -= 1
# 주어진 두 문자열로 만든 비밀번호를 출력
print(answer[::-1])