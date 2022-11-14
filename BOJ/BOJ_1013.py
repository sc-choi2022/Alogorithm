import re, sys

T = int(sys.stdin.readline())

for _ in range(T):
    sign = sys.stdin.readline().strip()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(sign)
    if m:
        print('YES')
    else:
        print('NO')

