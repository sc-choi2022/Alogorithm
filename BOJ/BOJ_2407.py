import sys
# 팩토리얼 함수 fact
def fact(N, end):
    if N == end:
        return 1
    else:
        return N * fact(N-1, end)

# 조합 nCm의 n, m
n, m = map(int, sys.stdin.readline().split())

# 조합의 결과를 출력
print(fact(n, 1) // (fact(n-m, 1)*fact(m,1)))