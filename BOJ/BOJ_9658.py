import sys

# 두 사람이 완벽하게 게임을 진행한다.
# 돌의 개수 N
N = int(sys.stdin.readline())
# 남은 돌의 개수가 N가 있을 때 이기는 사람을 저장하는 배열 dp
# True: 상근, False: 창영
dp = [False]*1001
# 4개부터 시작하는 for문 이전의 초기값을 저장
# 완벽하게 게임이 진행되었을 때 돌이 2개 남는 경우 상근이 이긴다.
dp[2] = True

for i in range(4, N+1):
    # i번째가 상근이의 차례가 된다면,
    # i-1, i-3, i-4번째는 창영이의 차례가 된다.
    # dp[i-1], dp[i-3], dp[i-4]에서 상근이 모두 이기는 경우 창영이가 이긴다.
    if not dp[i-1] or not dp[i-3] or not dp[i-4]:
        dp[i] = True
# 상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력
print('SK' if dp[N] else 'CY')