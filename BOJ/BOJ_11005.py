import sys

tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 10진법 수 N, 바꿀 B진법
N, B = map(int, sys.stdin.readline().split())
# 10진법 수 N을 B진법으로 저장할 변수 ans
ans = ''

while N != 0:
    ans += str(tmp[N % B])
    N //= B
# 10진법 수 N을 B진법 출력
print(ans[::-1])