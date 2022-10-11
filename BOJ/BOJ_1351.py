import sys
from collections import defaultdict
# AN의 값이 이미 존재하는 확인하고 dp[N]을 return하는 함수 check
def check(N):
    if dp[N]:
        return dp[N]
    dp[N] = check(N//P) + check(N//Q)
    return dp[N]

# 주어지는 N, P, Q
N, P, Q = map(int, sys.stdin.readline().split())

# index위치에 Ai 값을 저장하는 dp
dp = defaultdict(int)
# A0값을 dp[0]에 1을 저장
dp[0] = 1

# AN의 값인 dp[N]을 함수 check로 출력
print(check(N))