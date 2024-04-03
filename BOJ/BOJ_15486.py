import sys

# 퇴사까지 남을 일수 N
N = int(sys.stdin.readline())

# 상담을 완료하는데 걸리는 기간 T와 금액 P를 저장하는 배열 appointments
appointments = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
# i번째 날부터 상담을 했을 때 얻을 수 있는 가장 큰 금액을 저장하는 배열 dp
dp = [0]*N

for i in range(N-1, -1, -1):
    # i+1일의 상담 시간 T, 금액 P
    T, P = appointments[i]

    if i == N-1:
        # 상담 시간이 1일인 경우에만 가능
        if T == 1:
            dp[i] = P
    # 마지막 날에 상담이 끝나는 경우
    elif i+T == N:
        dp[i] = max(dp[i+1], P)
    # 남은 기간내에 상담이 가능한 경우
    elif i+T < N:
        dp[i] = max(dp[i+1], dp[i+T]+P)
    # 남은 기간내에 상담이 불가능한 경우
    elif i+T > N:
        dp[i] = dp[i+1]
# 얻을 수 있는 최대 이익을 출력
print(max(dp))