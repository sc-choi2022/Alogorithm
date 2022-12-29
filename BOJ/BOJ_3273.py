from itertools import combinations
import sys

# 수열의 크기 n
n = int(sys.stdin.readline())
# 수열을 담을 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))
# 쌍의 합의 조건인 x
x = int(sys.stdin.readline())
# 문제의 조건을 만족하는 쌍의 개수 ans 0으로 초기화
ans = 0

# numbers의 모든 쌍을 담은 combs
combs = list(combinations(numbers, 2))

for comb in combs:
    # combs의 쌍 comb가 합이 x을 만족하는 경우 ans 1 증가
    if sum(comb) == x:
        ans += 1
# ans을 출력
print(ans)