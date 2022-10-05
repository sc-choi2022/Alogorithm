import sys
from itertools import combinations
from math import lcm
# 주어지는 다섯개의 수를 담은 리스트 numbers
numbers = list(map(int, sys.stdin.readline().split()))
# 3개를 뽑는 모든 경우를 담은 리스트 lst
lst = list(combinations(numbers, 3))
ans = 1000000

for l in lst:
    # 각 경우의 a, b, c에 대해 최소공배수를 찾아 ans을 갱신
    a, b, c = l[0], l[1], l[2]
    ans = min(ans, lcm(lcm(a, b),c))
# ans 출력
print(ans)