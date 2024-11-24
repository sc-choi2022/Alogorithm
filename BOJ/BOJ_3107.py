import sys

# IPv6주소 IPv6
IPv6 = sys.stdin.readline().rstrip().split(':')

result = ['0000'] * 8
flag = False
for i in range(8):
    if IPv6[i] == '' and IPv6[i+1] == '':
        flag = True
        break
    result[i] = '0'*(4-len(IPv6[i])) + IPv6[i]
if flag:
    for j in range(1, 8):
        if IPv6[-j] == '' and IPv6[-j-1] == '':
            break
        result[-j] = '0'*(4-len(IPv6[-j])) + IPv6[-j]

print(':'.join(result))