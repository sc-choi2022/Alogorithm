from decimal import Decimal
from math import sqrt
import sys

def solution(n, k):
    global answer

    S = [0] * (N+1)
    SQ = S[::]
    for i in range(1, N+1):
        S[i] = S[i-1] + numbers[i-1]
        SQ[i] = SQ[i-1] + numbers[i-1]**2

    for j in range(K, N+1):
        for k in range(N-K+1):
            M = Decimal(S[k+K]-S[k])/K
            V = Decimal(SQ[k+K]-SQ[k])/K - M*M
            answer = min(answer, V)
    return sqrt(answer)

# 인형의 개수 N, 연속된 개수 K
N, K = map(int, sys.stdin.readline().split())
# 인형을 선호하는 사람의 수 numbers
numbers = list(map(int, sys.stdin.readline().split()))

answer = Decimal('inf')
print(solution(numbers, K))