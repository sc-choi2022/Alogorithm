import sys

# 주어지는 문자열 S
S = list(sys.stdin.readline().rstrip()[::-1])

# 문자열의 0의 개수 cnt
cnt = S.count('0')
# 문자열 S에서 없애야하는 0과 1의 개수 zero, one
zero, one = cnt//2, (len(S) - cnt)//2

# 0을 제거하는 while문
while zero:
    S.pop(S.index('0'))
    zero -= 1
# 문자열을 원래 순서 돌려놓는다.
S = S[::-1]

# 1을 제거하는 while문
while one:
    S.pop(S.index('1'))
    one -= 1

# 가능한 문자열 중 사전순으로 가장 빠른 것을 출력
print(''.join(S))