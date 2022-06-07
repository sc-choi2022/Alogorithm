# 상담가능한 일수 N
N = int(input())
# N번째 일에 상담 시간을 담을 리스트 T
T = [0 for _ in range(N+1)]
# N번째 일에 금액을 담을 리스트 P
P = [0 for _ in range(N+1)]

# N개의 줄에 Ti와 Pi가 주어지는 데 이를 리스트 T와 P에 할당
for i in range(N):
    T[i], P[i] = map(int, input().split())

# 최대 이익을 구하기 위해 사용할 리스트 dp
dp = [0] * (N + 1)

for j in range(N-1, -1, -1):
    # N일 안에 해결할 수 있는 경우
    if T[j] + j <= N:
        # j일의 상담금액이 추가된 금액과 dp[j+1]의 금액 중
        # 큰 값을 dp[j]에 할당
        dp[j] = max(P[j] + dp[j + T[j]], dp[j + 1])
    # N일을 초과하는 경우에는 상담이 불가능하므로 j+1의 금액을 j에 할당
    else:
        dp[j] = dp[j + 1]

# 백준이가 얻을 수 있는 최대 이익을 출력
print(dp[0])