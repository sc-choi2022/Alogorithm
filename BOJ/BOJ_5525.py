import sys
# PN의 정보 N
N = int(sys.stdin.readline())
# 문자열 S의 길이 M
M = int(sys.stdin.readline())
# 문자열 S
S = sys.stdin.readline().strip()

start, cnt, ans = 0, 0, 0

while start < (M - 1):
    if S[start:start + 3] == 'IOI':
        cnt += 1
        start += 2
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        start += 1
        cnt = 0
print(ans)