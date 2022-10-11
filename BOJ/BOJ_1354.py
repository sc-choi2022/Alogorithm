import sys
from collections import defaultdict
# AN의 값이 이미 존재하는 확인하고 dp[N]을 return하는 함수 check
def check(N):
    # (N ≥ 1) 조건을 만족하지 않는다면 1 return
    if N <= 0:
        return 1
    if dp[N]:
        return dp[N]
    dp[N] = check((N//P)-X) + check((N//Q)-Y)
    return dp[N]

# 주어지는 N, P, Q, X, Y
N, P, Q, X, Y = map(int, sys.stdin.readline().split())
dp = defaultdict(int)

# AN의 값인 dp[N]을 함수 check로 출력
print(check(N))