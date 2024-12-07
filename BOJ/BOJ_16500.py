import sys

# 문자열 S
S = sys.stdin.readline().rstrip()
# 문자열 S의 길이 L
L = len(S)
# 단어 목록 A의 단어개수 N
N = int(sys.stdin.readline())
# 단어 목록 A
A = [sys.stdin.readline().rstrip() for _ in range(N)]
dp = [0] * (L+1)
dp[0] = 1

for i in range(L):
    if dp[i] == 0:
        continue

    for a in A:
        l = len(a)
        if S[i:i+l] == a:
            dp[i+l] = 1

# A에 포함된 문자열로 S를 만들 수 있으면 1, 없으면 0을 출력
print(dp[L])