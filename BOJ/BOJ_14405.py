import sys

# 주어지는 문자열 S
S = sys.stdin.readline().rstrip()
# 문자열 S에서 pi, ka, chu를 제거
S = S.replace('pi', ' ')
S = S.replace('ka', ' ')
S = S.replace('chu', ' ')

# 문자열 S가 "pi", "ka", "chu"를 이어 붙여서 만들 수 있으면 "YES"를 아니면 "NO"를 출력
print('NO' if S.strip() else 'YES')