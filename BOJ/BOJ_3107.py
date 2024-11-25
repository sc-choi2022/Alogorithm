import sys

def restore(lst):
    L = len(lst)

    for i in range(L):
        lst[i] = '0'*(4-len(lst[i]))+lst[i]

# IPv6주소 IPv6
IPv6 = sys.stdin.readline().rstrip().split('::')
# 원래 IPv6 주소를 저장하는 변수 result
result = ''

# 2번째 규칙이 적용된 경우
if len(IPv6) == 2:
    pre, post = IPv6[0].split(':'), IPv6[1].split(':')
    restore(pre)
    restore(post)
    result = ':'.join(pre + ['0000']*(8-len(pre)-len(post)) + post)
# 1번째 규칙만 적용된 경우
else:
    IPv6 = IPv6[0].split(':')
    restore(IPv6)
    result = ':'.join(IPv6)
# result를 출력
print(result)