import sys

# 돌의 개수 N
N = int(sys.stdin.readline())
dp = [0] * 1001
# idx개수의 돌에서 이기는 사람을 저장
dp[1], dp[2], dp[3], dp[4] = 'SK', 'CY', 'SK', 'SK'

for i in range(5, N+1):
    for stone in (1, 3, 4):
        if dp[i-stone] == 'CY':
            dp[i] = 'SK'
            break
        dp[i] = 'CY'
# 상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력
print(dp[N])