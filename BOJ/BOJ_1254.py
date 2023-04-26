import sys

# 문자열 S
S = sys.stdin.readline().rstrip()
# 문자열 S의 길이 N
N = len(S)

for i in range(N):
    if S[i::] == S[i:][::-1]:
        # 가장 짧은 팰린드롬의 길이를 출력
        print(N + i)
        break