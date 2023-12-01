import sys

# 돌의 개수 N
N = int(sys.stdin.readline())
dp = [0]*(N+1)

for i in range(N+1):
    flag = False
    for stone in (1, 3, 4):
        if i-stone <= 0:
            break
        if dp[i-stone]:
            flag = True
            break
    if not flag:
        dp[i] = 1
print('CY' if dp[N] else 'SK')