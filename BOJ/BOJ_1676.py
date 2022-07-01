import sys
from math import factorial

N = int(sys.stdin.readline())
ans = 0
number = factorial(N)

# 0의 개수는 10으로 나누어지는 횟수이므로 10으로 나누어질 때마다 ans 1증가 후
while True:
    # 나누어지지 않는다면 break
    if number % 10:
        break
    ans += 1
    number //= 10
# ans 출력
print(ans)