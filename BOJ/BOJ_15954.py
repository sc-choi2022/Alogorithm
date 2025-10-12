from decimal import Decimal
from math import sqrt
import sys

def solution(A):
    sums = [0 for _ in range(N+1)]
    sq_sums = sums[:]
    for i in range(1, N+1):
        sums[i] = sums[i-1] + A[i-1]
        sq_sums[i] = sq_sums[i-1] + A[i-1]**2
    min_var = Decimal('INF')
    for j in range(K, N+1):
        for l in range(N-j+1):
            m = Decimal(sums[l+j] - sums[l]) / j
            var = Decimal(sq_sums[l+j] - sq_sums[l]) / j - m*m
            min_var = min(min_var, var)
    return min_var.sqrt()

# 인형의 개수 N, 연속된 개수 K
N, K = map(int, sys.stdin.readline().split())
# 인형을 선호하는 사람의 수 numbers
numbers = list(map(int, sys.stdin.readline().split()))

# 선택된 인형들을 선호하는 사람의 수의 표준 편차 answer
answer = Decimal('inf')
# answer 출력
print(solution(numbers))