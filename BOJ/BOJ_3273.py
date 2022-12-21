from itertools import combinations
import sys

n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
ans = 0

combs = list(combinations(numbers, 2))
for comb in combs:
    if sum(comb) == x:
        ans += 1

print(ans)